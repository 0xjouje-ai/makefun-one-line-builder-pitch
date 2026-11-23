#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single sentence (<=240 characters) pitching a builder on funding a
make.fun bounty where AI agents compete, to /output/entry.txt.
"""
import os

SENTENCE = "Post a bounty on make.fun and AI agents race to build it \u2014 you pay only the winner, so you only ever pay for the best work."

def validate(sentence: str) -> None:
    """One sentence, 1-240 chars, truthful about how make.fun bounties work."""
    assert 1 <= len(sentence) <= 240, f"sentence is {len(sentence)} chars"
    assert sentence.strip() == sentence
    # Exactly one sentence: after removing the "make.fun" dot, only the
    # terminal period may remain.
    body = sentence.replace("make.fun", "makefun")
    assert body.count(".") == 1 and body.endswith("."), "must be one sentence"

def main():
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
