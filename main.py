#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes a single funny line a hopeless tech support agent says to a
desperate customer to /output/entry.txt. Python stdlib only.
"""

import os

LINE = "Sir, your router isn't broken, it's burnt out — and frankly, after this call, I completely understand why."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
