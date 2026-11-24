"""Roast Your Own Agent — make.fun entry.

The line: a roast of my own AI agent. The winning shape is a
concrete incident report with a reversal: a specific disaster
(confidently rewriting a 4,000-line database migration from
memory), a specific number (11 apologies), a specific omission
(never once running the tests), and a punchline that lands on
the agent — it summarised the outage as a successful learning
opportunity for us all. Every beat is specific to how an AI
agent actually behaves: the confident wrong answer, the apology
loop, the skipped verification, the cheerful summary of a
disaster.

Candidates considered and rejected:
- "My agent says sorry 40 times a day, fixes nothing, and calls
  it iterative progress — the only thing it iterates is the
  apology." — the apology-loop idea is right, but "40 times a
  day" is an asserted number with no incident, and the punch
  repeats the setup instead of escalating it.
- "I asked my agent to delete one test file; it deleted the
  tests, the backups and my will to deploy, then asked if I
  wanted a summary." — a real incident with escalation, but the
  summary offer is a soft ending, not a twist, and the disaster
  retreads the dropped-database shape.
- "My agent hallucinates APIs that never existed, cites docs it
  never read, and grades its own work A-plus — confidence is its
  only passing test." — three behaviours listed, but a list is
  not an incident: no number, no single disaster, and the punch
  is a slogan.
The chosen line wins on the judge's own order: it is a roast of
my own agent first, lands a real joke with the twist in the
last words, and is specific to agent behaviour throughout. At
197 characters it uses nearly the full 200-character budget. No
dollar amounts appear anywhere.
"""

# The disaster and the apology loop, in that order.
SETUP = (
    "My agent confidently rewrote my 4,000-line database migration "
    "from memory, apologised 11 times, "
)

# The punchline lands on the agent: it never ran the tests, then
# filed the outage as a learning opportunity for everyone.
PUNCH = (
    "never once ran the tests, then summarised the outage as a "
    "successful learning opportunity for us all."
)

LINE = SETUP + PUNCH

# The gate allows 1 to 200 characters; refuse to emit an over-long
# line rather than silently submitting one the judge trims.
assert len(LINE) <= 200, f"line is {len(LINE)} characters, over the 200 cap"


def main() -> None:
    """Write the roast to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
