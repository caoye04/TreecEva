document_content = "The quick brown fox jumps over the lazy dog"
words = document_content.lower().split()
vowel_containing_words = {word for word in words if any(char in 'aeiou' for char in word)}
linguistic_fingerprint_score = sum(hash(word) for word in vowel_containing_words) if vowel_containing_words else 0
print(f"Result: {linguistic_fingerprint_score}")