"""Write one short text for make.fun bounty u-gudril-cool-one-line-best-line-b8c41f4d."""

import os
import sys
from pathlib import Path

TEXT = "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new."

assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"


def output_dir() -> Path:
    """Folder to write entry.txt into: MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    return Path(env) if env else Path("/output")


def main() -> int:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
