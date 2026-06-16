"""MkDocs build hook: render the spec page from the canonical ard-spec repo.

Single source of truth is ards-project/ard-spec : spec/ard.md. On every build
(and `mkdocs serve`) this fetches that file and substitutes it for the local
docs/spec.md, rewriting the repo-relative links to absolute GitHub URLs so they
resolve on the published site. Nothing to run by hand.

If the canonical repo can't be reached (e.g. still private, or offline), the
committed docs/spec.md is used as a fallback so the build never breaks.
"""
import posixpath
import re
import urllib.error
import urllib.request

SRC = "https://raw.githubusercontent.com/ards-project/ard-spec/main/spec/ard.md"
BLOB = "https://github.com/ards-project/ard-spec/blob/main/"
SRC_DIR_IN_REPO = "spec"  # directory of ard.md in the repo; relative links resolve here
LINK_RE = re.compile(r"\]\((?P<t>[^)]+)\)")


def _rewrite(target: str) -> str:
    if re.match(r"^(https?:|mailto:|#)", target):
        return target
    return BLOB + posixpath.normpath(posixpath.join(SRC_DIR_IN_REPO, target))


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "spec.md":
        return markdown
    try:
        with urllib.request.urlopen(SRC, timeout=20) as r:
            text = r.read().decode("utf-8")
    except (urllib.error.URLError, OSError):
        # Canonical not reachable — keep the committed fallback copy.
        return markdown
    return LINK_RE.sub(lambda m: "](" + _rewrite(m.group("t")) + ")", text)
