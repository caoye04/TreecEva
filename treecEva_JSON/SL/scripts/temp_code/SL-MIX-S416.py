from collections import Counter

document = "the quick brown fox jumps over the lazy dog the dog was really lazy"
words = document.split()
frequency = Counter(words)
checksum = sum(hash(word) * count for word, count in frequency.items())

Result = checksum
print(f"Result: {Result}")