"""MkDocs build hook: serve the /spec/ page from the canonical ard-spec repo.

The specification lives only in ards-project/ard-spec (spec/ard.md). There is no
spec file committed in this repo. On every build (and `mkdocs serve`) this hook
fetches the canonical file and injects it as a generated page (spec.md),
rewriting the source's repo-relative links to absolute GitHub URLs so they
resolve on the published site.

If the canonical repo can't be reached, a short placeholder linking to it is
served so the build never breaks.
"""
import posixpath
import re
import urllib.error
import urllib.request

from mkdocs.structure.files import File

SRC = "https://raw.githubusercontent.com/ards-project/ard-spec/main/spec/ard.md"
BLOB = "https://github.com/ards-project/ard-spec/blob/main/"
SRC_DIR_IN_REPO = "spec"  # dir of ard.md in the repo; relative links resolve here
LINK_RE = re.compile(r"\]\((?P<t>[^)]+)\)")

PLACEHOLDER = (
    "# ARD Specification\n\n"
    "The specification could not be fetched from its source repository at build "
    "time. Read it directly at "
    "[ards-project/ard-spec](https://github.com/ards-project/ard-spec/blob/main/spec/ard.md).\n"
)


def _rewrite(target: str) -> str:
    if re.match(r"^(https?:|mailto:|#)", target):
        return target
    return BLOB + posixpath.normpath(posixpath.join(SRC_DIR_IN_REPO, target))


def _fetch() -> str:
    with urllib.request.urlopen(SRC, timeout=20) as r:
        text = r.read().decode("utf-8")
    return LINK_RE.sub(lambda m: "](" + _rewrite(m.group("t")) + ")", text)


def on_files(files, config):
    try:
        content = _fetch()
    except (urllib.error.URLError, OSError):
        content = PLACEHOLDER
    files.append(File.generated(config, "spec.md", content=content))
    return files
