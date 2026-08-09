from collections import Counter
import string

try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()

    cleaned_words = []

    for word in words:
        word = word.strip(string.punctuation).lower()
        if word:
            cleaned_words.append(word)

    word_frequency = Counter(cleaned_words)

    print("=" * 40)
    print("        WORD COUNT TOOL")
    print("=" * 40)

    print(f"Number of words      : {len(words)}")
    print(f"Number of lines      : {len(lines)}")
    print(f"Number of characters : {len(text)}")

    print("\nMost Common Words")
    print("-" * 40)

    for word, count in word_frequency.most_common(5):
        print(f"{word:<20} : {count}")

    print("\nWord Frequency Distribution")
    print("-" * 40)

    for word, count in word_frequency.items():
        print(f"{word:<20} : {count}")

except FileNotFoundError:
    print("Error: sample.txt file was not found.")
except Exception as e:
    print("An error occurred:", e)
