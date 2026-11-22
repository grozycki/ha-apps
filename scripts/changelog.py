#!/usr/bin/env python3
"""Work with an app's CHANGELOG.md in the Keep a Changelog format.

Commands:
  release CHANGELOG VERSION DATE  Move the Unreleased entries under a new
                                  version heading. Fails if Unreleased is empty.
  notes CHANGELOG VERSION         Print the entries of one version.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

UNRELEASED = "## [Unreleased]"
HEADING = re.compile(r"^## \[(?P<name>[^\]]+)\]", re.MULTILINE)


class ChangelogError(Exception):
    """The changelog cannot be used for the requested operation."""


@dataclass(frozen=True)
class Section:
    name: str
    start: int  # offset of the heading line
    body_start: int  # offset just after the heading line
    end: int  # offset of the next heading, or end of text


def sections(text: str) -> list[Section]:
    matches = list(HEADING.finditer(text))
    result: list[Section] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        line_end = text.find("\n", match.start())
        body_start = len(text) if line_end == -1 else line_end + 1
        result.append(Section(match.group("name"), match.start(), body_start, end))
    return result


def find(text: str, name: str) -> Section:
    for section in sections(text):
        if section.name == name:
            return section
    raise ChangelogError(f"no section [{name}]")


def release(text: str, version: str, date: str) -> str:
    if any(section.name == version for section in sections(text)):
        raise ChangelogError(f"section [{version}] already exists")
    unreleased = find(text, "Unreleased")
    body = text[unreleased.body_start : unreleased.end].strip()
    if not body:
        raise ChangelogError("the Unreleased section is empty")
    return (
        text[: unreleased.start]
        + f"{UNRELEASED}\n\n## [{version}] - {date}\n\n{body}\n\n"
        + text[unreleased.end :]
    )


def notes(text: str, version: str) -> str:
    section = find(text, version)
    return text[section.body_start : section.end].strip() + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    commands = parser.add_subparsers(dest="command", required=True)

    release_parser = commands.add_parser("release")
    release_parser.add_argument("changelog", type=Path)
    release_parser.add_argument("version")
    release_parser.add_argument("date")

    notes_parser = commands.add_parser("notes")
    notes_parser.add_argument("changelog", type=Path)
    notes_parser.add_argument("version")

    args = parser.parse_args(argv)
    path: Path = args.changelog
    text = path.read_text(encoding="utf-8")

    try:
        if args.command == "release":
            path.write_text(release(text, args.version, args.date), encoding="utf-8")
        else:
            sys.stdout.write(notes(text, args.version))
    except ChangelogError as error:
        print(f"{path}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
