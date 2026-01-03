import re
import sys
from collections import Counter


def analyze_text(text):
    """
    Analyzes the text to find word count, sentence count, and top 10 frequent words.
    """

    words_raw = text.split()  # split by whitespace to get words
    word_count = len(words_raw)

    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    sentence_count = len(sentences)

    word_pattern = r"\b[a-z0-9]+(?:['-]?[a-z0-9]+)*\b"
    cleaned_words = re.findall(word_pattern, text.lower())

    word_counts = Counter(cleaned_words)
    top_10 = word_counts.most_common(10)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10": top_10,
    }


def main():
    try:
        with open("sample_text.txt", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: sample_text.txt not found.")
        sys.exit(1)

    stats = analyze_text(text)

    print("--- Text Analysis Results ---")
    print(f"Word Count: {stats['word_count']}")
    print(f"Sentence Count: {stats['sentence_count']}")
    print("\nTop 10 Most Frequent Words:")
    for word, count in stats["top_10"]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
