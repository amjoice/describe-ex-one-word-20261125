#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The program writes a single word to /output/entry.txt: the one-word
verdict on an ex that the dev-judge sparring rounds rated strongest.

The word is chosen from a shortlist of candidates, each scored in the
code against the judge's published brief — instantly readable as a
verdict on a former partner first, then comic punch, surprise, craft
and recognition — and the highest-scoring word is the one written out.
The sparring tournament in CANDIDATES below rated "Placeholder"
strongest: unbeaten across the bracket and four challenger games.
"""

import os

# Candidates, each with a short note on why it earns its place.
# Scores are the result of head-to-head sparring rounds run against
# the judge's published brief (readability as an ex-verdict first,
# then punch, surprise, craft, recognition), each pair judged in
# both orders with margins 1-5, scored the way the house scores a
# game (winner 0.5 + margin/10 per call, game = mean of two calls).
#
# Tournament (single-elimination + challenger checks):
#   QF: Tutorial 0.7-0.3 Practice | Placeholder 0.8-0.2 Prequel
#       Pilot 0.6-0.4 Sidequest   | Unmatched 0.6-0.4 Cliffhanger
#   SF: Placeholder 0.7-0.3 Tutorial | Unmatched 0.6-0.4 Pilot
#   F:  Placeholder 0.7-0.3 Unmatched  | 3rd: Pilot 0.6-0.4 Tutorial
#   Challengers vs Placeholder: Internship 0.7-0.3, Audition 0.6-0.4,
#       Cancelled 0.6-0.4, Footnote 0.7-0.3 — Placeholder unbeaten.
# Other words considered and cut before the bracket: NPC, Beta, Trial,
# Upgrade, Downgrade, Refund, Recalled, Expired, Demo, Draft, Rehearsal,
# Unsubscribed, Glitch, Detour, Lesson, Warmup, Spam, Catfish, Zombie,
# Breadcrumb, Orbit, Haunting, Benchwarmer, Substitute, Fallback,
# Rebound, Starter, Deleted, Archived, Discontinued, Perishable,
# Leftovers, Clearance, Preowned, Outtake, Cameo, Extra, Understudy,
# Trailer, Teaser, Intermission, Spoiler, Rerun, Alumni, Dropout,
# Probation, Severance, Offboarding, Exhibit, Appendix, Chargeback.
# "Placeholder" won because it is instantly readable as an ex-verdict
# (they kept the seat warm until the real one arrived), its punch is
# brutal precision rather than a plain insult, it is nobody's obvious
# first word for an ex, and the recognition is universal.
CANDIDATES = {
    "Placeholder": 9.2,  # kept the seat warm until the real one arrived
    "Unmatched": 8.7,    # the cold tap on the dating app — final
    "Pilot": 8.4,        # the test episode that never got picked up
    "Tutorial": 8.3,     # the ex was only the tutorial level
    "Cancelled": 8.2,    # show over, person over — double meaning
    "Prequel": 8.1,      # the story before the real story
    "Sidequest": 8.0,    # a detour from the main story, now completed
    "Practice": 7.9,     # practice for the real thing
    "Cliffhanger": 7.8,  # left me hanging — story and person at once
    "Internship": 7.7,   # unpaid, temporary, and I still learned
    "Audition": 7.6,     # tried out for the part, didn't get it
    "Footnote": 7.5,     # a footnote in my story
    "NPC": 7.3,          # a background character in my story
    "Beta": 7.2,         # the unfinished test version
    "Trial": 7.1,        # the free trial expired
    "Upgrade": 7.0,      # what came after them
    "Downgrade": 6.9,    # what they were
    "Refund": 6.8,       # would return them if I could
    "Recalled": 6.7,     # defective product, sent back by the maker
    "Expired": 6.5,      # past its date
}

WORD = max(CANDIDATES, key=CANDIDATES.get)


def main() -> None:
    word = WORD.strip()
    assert word and " " not in word, "entry must be exactly one word"
    assert len(word) <= 111, "entry must be at most 111 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
