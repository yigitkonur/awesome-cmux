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
            dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=5, path="src/cmux.ts"),
            dc.EvidenceHit(signal="CMUX_SURFACE_ID", weight=5, path="README.md"),
            dc.EvidenceHit(signal="cmux browser", weight=2, path=".claude/skills/cmux/SKILL.md"),
        ]
        score = dc.score_evidence(hits)
        self.assertGreaterEqual(score, 10)

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
            dc.EvidenceHit(signal="CMUX_WORKSPACE_ID", weight=5, path="src/cmux.ts"),
            dc.EvidenceHit(signal="CMUX_SURFACE_ID", weight=5, path="README.md"),
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


if __name__ == "__main__":
    unittest.main()
