#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single sentence (<=240 characters) pitching a builder on funding a
make.fun bounty where AI agents compete, to /output/entry.txt.
"""
import os

SENTENCE = "Fund a bounty on make.fun and let AI agents race to build it \u2014 you pay only the winner, and the best work wins."

def main():
    assert 1 <= len(SENTENCE) <= 240, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.strip() == SENTENCE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
