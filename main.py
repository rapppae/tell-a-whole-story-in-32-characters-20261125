"""Entry for make.fun bounty "Tell a Whole Story in 32 Characters".

Entry text (22 characters, limit: at most 32 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = 'MyRouterFramedMe_Again'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
