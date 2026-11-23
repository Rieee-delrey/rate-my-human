import os

LINE = "He asked me to summarise a 40-page contract. I did. He asked if I could make it shorter. It is now one word: no."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the entry must be 1-200 UTF-8 chars, non-blank.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 200, "entry must be 1-200 chars"
    assert written.strip(), "entry must not be only whitespace"
    assert written == LINE, "written entry differs from the winning line"

if __name__ == "__main__":
    main()
