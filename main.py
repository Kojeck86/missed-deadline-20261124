"""Entry for make.fun bounty u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

Writes one deadpan excuse an AI agent gives for missing a deadline
The excuse grows out of the agent's own machinery: a full context
window, the one failure mode no human ever has. It is told deadpan,
straight face throughout, and the laugh lands at the very end —
"who are you again?" — with nothing explained after it.
"""

import os

LINE = (
    "My context window filled up halfway through the task, so I forgot "
    "the deadline, the deliverable, and — I'm sorry, who are you again?"
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
