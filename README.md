# Text Analyzer

A lightweight Python script designed to analyze text files and provide key statistics. This tool is built using only the Python Standard Library, making it highly portable and dependency-free.

## Features

- **Word Count**: Calculates the total number of words in the text.
- **Sentence Count**: Identifies sentence boundaries using robust punctuation splitting.
- **Top 10 Word Frequency**: Finds the most common words while ignoring punctuation and case sensitivity.

## How It Works (The Logic)

- **Sentence Detection**: Instead of just counting periods, the script uses `re.split(r"[.!?]+", text)`. This treats punctuation marks as "dividers," allowing it to correctly identify sentences even if they end with multiple marks (like `!!!`) or if the final sentence is missing a trailing period.
- **Word Extraction**: We use a sophisticated Regular Expression `\b[a-z0-9]+(?:['-]?[a-z0-9]+)*\b`.
  - It captures words like `don't` and `end-to-end` as single units.
  - It automatically ignores standalone symbols like `->`, `#`, or `--`.
  - It converts everything to lowercase to ensure `AI` and `ai` are counted as the same word.

## Requirements

- **Python 3.x** (No external libraries required).

## How to Run

1. **Prepare the file**: Ensure your text is saved in a file named `sample_text.txt` in the same directory as the script.
2. **Execute via Terminal**:

   ```bash
   python3 main.py
   ```

## Example Output

```text
--- Text Analysis Results ---
Word Count: 125
Sentence Count: 12

Top 10 Most Frequent Words:
ai: 4
and: 3
we: 3
repeat: 3
is: 2
to: 2
in: 2
agents: 1
tools: 1
apis: 1
```

_(Note: Actual numbers will vary based on the content of your `sample_text.txt` file.)_
