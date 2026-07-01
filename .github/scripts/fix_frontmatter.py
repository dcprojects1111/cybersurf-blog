#!/usr/bin/env python3
"""Normalise Jekyll post front matter so images render.

Jekyll only parses YAML front matter when the opening `---` is on the first
line at column 0 with no indentation. n8n has been publishing posts with the
whole front-matter block indented (a leading space before `---`), which makes
Jekyll ignore `page.image` and skip the featured image.

This script scans a directory of markdown posts, de-indents the front-matter
block of any file that needs it, and rewrites the file. It prints which files
were changed and exits 0. It changes nothing when everything is already clean.

Usage:
    python fix_frontmatter.py [POSTS_DIR]   (default: _posts)
"""
import glob
import os
import sys


def fix_file(path):
    """De-indent the front-matter block. Return True if the file changed."""
    with open(path, encoding="utf-8") as fh:
        original = fh.read()
    lines = original.split("\n")

    # Front-matter fences are the first two lines that are just `---`
    # (ignoring surrounding whitespace), and the opener must be at the top.
    fences = [i for i, ln in enumerate(lines) if ln.strip() == "---"]
    if len(fences) < 2 or fences[0] > 1:
        return False

    start, end = fences[0], fences[1]
    block = lines[start:end + 1]
    dedented = [ln.lstrip(" \t") for ln in block]
    if dedented == block:
        return False

    lines[start:end + 1] = dedented
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return True


def main():
    posts_dir = sys.argv[1] if len(sys.argv) > 1 else "_posts"
    changed = []
    for path in sorted(glob.glob(os.path.join(posts_dir, "*.md"))):
        if fix_file(path):
            changed.append(os.path.basename(path))

    if changed:
        print(f"Fixed front matter on {len(changed)} post(s):")
        for name in changed:
            print(f"  - {name}")
    else:
        print("All posts already have clean front matter. Nothing to fix.")


if __name__ == "__main__":
    main()
