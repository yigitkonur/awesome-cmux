import importlib.util
import pathlib
import sys
import unittest


def load_module():
    path = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "discover_candidates.py"
    spec = importlib.util.spec_from_file_location("discover_candidates", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


dc = load_module()


class DiscoveryCoreTests(unittest.TestCase):
    def test_extract_readme_repo_slugs_skips_deeper_paths(self):
        text = """
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | Source |
| [HazAT/pi-config](https://github.com/HazAT/pi-config) | Item |
- [llv22/cmux_forward](https://github.com/llv22/cmux_forward) — Fork
| [Nightly](https://github.com/manaflow-ai/cmux/releases/latest/download/cmux-macos.dmg) | Download |
"""
        self.assertEqual(
            dc.extract_existing_repo_slugs(text),
            {"manaflow-ai/cmux", "HazAT/pi-config", "llv22/cmux_forward"},
        )

    def test_extract_readme_repo_slugs_handles_url_variants(self):
        text = """
| [Repo A](https://github.com/example/alpha/) |
| [Repo B](https://github.com/example/bravo?tab=readme) |
| [Repo C](https://github.com/example/charlie). |
| [Repo D](https://github.com/example/delta/)!
"""
        self.assertEqual(
            dc.extract_existing_repo_slugs(text),
            {"example/alpha", "example/bravo", "example/charlie", "example/delta"},
        )

    def test_score_repo_evidence_prefers_env_var_hits(self):
        hits = [
            dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=10, path="src/cmux.ts"),
            dc.EvidenceHit(signal="CMUX_SURFACE_ID", weight=10, path="README.md"),
            dc.EvidenceHit(signal="cmux browser", weight=2, path=".claude/skills/cmux/SKILL.md"),
        ]
        score = dc.score_evidence(hits)
        self.assertGreaterEqual(score, 13)

    def test_status_review_when_only_weak_hits_inflate_score(self):
        weak_hits = [
            dc.EvidenceHit(signal="cmux browser", weight=2, path="src/a.ts"),
            dc.EvidenceHit(signal="cmux notify", weight=2, path="src/b.ts"),
            dc.EvidenceHit(signal="cmux preview", weight=2, path="src/c.ts"),
            dc.EvidenceHit(signal="cmux hub", weight=2, path="src/d.ts"),
        ]
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=1,
            language="TypeScript",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=True,
            already_listed=False,
            metadata_loaded=True,
            evidence_hits=weak_hits,
            score=dc.score_evidence(weak_hits),
            suggested_section="",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "review")

    def test_status_candidate_requires_readme_and_not_archived(self):
        strong_hits = [
            dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=10, path="src/cmux.ts"),
            dc.EvidenceHit(signal="CMUX_SURFACE_ID", weight=10, path="README.md"),
        ]
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=12,
            language="TypeScript",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=True,
            already_listed=False,
            metadata_loaded=True,
            evidence_hits=strong_hits,
            score=dc.score_evidence(strong_hits),
            suggested_section="By Agent > Pi",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "candidate")

    def test_status_review_when_score_is_weak(self):
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=1,
            language="Shell",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=True,
            already_listed=False,
            metadata_loaded=True,
            evidence_hits=[],
            score=3,
            suggested_section="",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "review")

    def test_status_excluded_without_readme(self):
        repo = dc.RepoCandidate(
            slug="example/repo",
            stars=1,
            language="Shell",
            updated="2026-04-03",
            description="desc",
            archived=False,
            has_readme=False,
            already_listed=False,
            metadata_loaded=True,
            evidence_hits=[],
            score=12,
            suggested_section="",
            status="",
            notes=[],
        )
        status = dc.classify_candidate(
            repo,
            excluded_slugs=set(),
            minimum_candidate_score=8,
        )
        self.assertEqual(status, "excluded")

    def test_already_listed_wins_over_excluded_slug(self):
        repo = dc.RepoCandidate(
            slug="manaflow-ai/cmux",
            stars=999,
            language="TypeScript",
            updated="2026-04-03",
            description="listed repo",
            archived=False,
            has_readme=True,
            already_listed=True,
            metadata_loaded=True,
            evidence_hits=[],
            score=0,
            suggested_section="",
            status="",
            notes=[],
        )

        status = dc.classify_candidate(
            repo,
            excluded_slugs={"manaflow-ai/cmux"},
            minimum_candidate_score=8,
        )

        self.assertEqual(status, "listed")

    def test_suggest_section_for_pi_repo(self):
        section = dc.suggest_section(
            slug="sanurb/pi-cmux-browser",
            description="Browser automation for Pi + cmux.",
            evidence_hits=[],
        )
        self.assertEqual(section, "By Agent > Pi")

    def test_path_penalty_downgrades_generated_or_vendored_paths(self):
        penalty = dc.path_confidence_adjustment(".claude/skills/cmux/SKILL.md")
        self.assertLess(penalty, 0)

    def test_high_confidence_gate_requires_cmux_env_var_signal(self):
        self.assertTrue(
            dc.has_high_confidence_evidence(
                [dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=10, path="src/app.ts")]
            )
        )
        self.assertFalse(
            dc.has_high_confidence_evidence(
                [dc.EvidenceHit(signal="cmux browser", weight=2, path="src/app.ts")]
            )
        )

    def test_render_markdown_report_prioritizes_candidate_rows(self):
        candidates = [
            dc.RepoCandidate(
                slug="example/candidate",
                stars=42,
                language="TypeScript",
                updated="2026-04-03",
                description="candidate repo",
                archived=False,
                has_readme=True,
                already_listed=False,
                metadata_loaded=True,
                evidence_hits=[dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=10, path="src/app.ts")],
                score=10,
                suggested_section="By Agent > Pi",
                status="candidate",
                notes=[],
            ),
            dc.RepoCandidate(
                slug="example/review",
                stars=3,
                language="Shell",
                updated="2026-04-03",
                description="review repo",
                archived=False,
                has_readme=True,
                already_listed=False,
                metadata_loaded=True,
                evidence_hits=[dc.EvidenceHit(signal="cmux browser", weight=2, path="docs/readme.md")],
                score=2,
                suggested_section="",
                status="review",
                notes=[],
            ),
        ]

        report = dc.render_markdown_report(candidates, included_statuses={"candidate", "review"})

        self.assertIn("| repo | status | score | stars | language | updated | suggested section | evidence |", report)
        self.assertLess(report.index("example/candidate"), report.index("example/review"))
        self.assertIn("CMUX_WORKSPACE_ID", report)
        self.assertIn("By Agent > Pi", report)

    def test_render_json_report_includes_results(self):
        payload = dc.render_json_report(
            [
                dc.RepoCandidate(
                    slug="example/candidate",
                    stars=42,
                    language="TypeScript",
                    updated="2026-04-03",
                    description="candidate repo",
                    archived=False,
                    has_readme=True,
                    already_listed=False,
                    metadata_loaded=True,
                    evidence_hits=[dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=10, path="src/app.ts")],
                    score=10,
                    suggested_section="By Agent > Pi",
                    status="candidate",
                    notes=["source search ok"],
                )
            ],
            included_statuses={"candidate"},
        )

        self.assertIn('"slug": "example/candidate"', payload)
        self.assertIn('"status": "candidate"', payload)
        self.assertIn('"source search ok"', payload)

    def test_parse_args_uses_approved_cli_flags(self):
        args = dc.parse_args(
            [
                "--limit-per-signal",
                "10",
                "--minimum-candidate-score",
                "12",
                "--include-listed",
                "--include-excluded",
                "--format",
                "markdown",
            ]
        )

        self.assertEqual(args.limit_per_signal, 10)
        self.assertEqual(args.minimum_candidate_score, 12)
        self.assertTrue(args.include_listed)
        self.assertTrue(args.include_excluded)

    def test_build_candidates_marks_listed_repos_from_readme(self):
        original_search = dc.search_code_for_signal
        original_fetch = dc.fetch_repository_metadata
        original_readme = dc.README

        class DummyReadme:
            def read_text(self):
                return "| [example/listed](https://github.com/example/listed) |\n"

        try:
            dc.README = DummyReadme()

            def fake_search(signal):
                if signal.name != "CMUX_WORKSPACE_ID":
                    return []
                return [{"repository": {"nameWithOwner": "example/listed"}, "path": "src/cmux.ts"}]

            def fake_fetch(slugs, batch_size=dc.DEFAULT_METADATA_BATCH_SIZE):
                return (
                    {
                        "example/listed": {
                            "slug": "example/listed",
                            "stars": 9,
                            "language": "TypeScript",
                            "updated": "2026-04-03",
                            "description": "listed repo",
                            "archived": False,
                            "has_readme": True,
                            "metadata_loaded": True,
                        }
                    },
                    [],
                )

            dc.search_code_for_signal = fake_search
            dc.fetch_repository_metadata = fake_fetch

            candidates, warnings = dc.build_candidates(
                signals=(
                    dc.SignalSpec("CMUX_WORKSPACE_ID", "CMUX_WORKSPACE_ID", 10, 1),
                ),
                candidate_score=8,
                metadata_batch_size=1,
            )

            self.assertEqual(warnings, [])
            self.assertEqual(len(candidates), 1)
            self.assertEqual(candidates[0].status, "listed")
            self.assertTrue(candidates[0].already_listed)
        finally:
            dc.search_code_for_signal = original_search
            dc.fetch_repository_metadata = original_fetch
            dc.README = original_readme


if __name__ == "__main__":
    unittest.main()
