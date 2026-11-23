#!/usr/bin/env python3
"""Six Words, One Story — a whole life in six words.

Grandma is gone; her last recipe was not for food but for
forgiveness. Writes the story to /output/entry.txt.
"""
import os

STORY = "Grandma's last recipe called for forgiveness."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)

if __name__ == "__main__":
    main()
