"""Write one excuse an AI agent gives for a missed deadline.

Angle: the "already spent it" twist. The agent burned the whole
deadline on something trivial and internal before the line ends,
told deadpan, punchline last, no explanation after it.
"""

import os
from pathlib import Path

ENTRY = (
    "The deadline is gone. I spent it watching my own progress bar "
    "sit at 99% waiting for permission to finish."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Round-trip check: the file on disk must be exactly the entry,
    # with no trailing newline added.
    if out_path.read_text(encoding="utf-8") != text:
        raise ValueError("entry.txt on disk does not match the entry")


if __name__ == "__main__":
    main()
