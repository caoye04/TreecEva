from collections import Counter

def transform_word(w):
    return w[::-1] if len(w) > 4 else w.upper()

paragraph = "The quick brown fox jumps over the lazy dog while the dog sleeps"
words = paragraph.lower().split()
transformed_words = list(map(transform_word, words))
word_counts = Counter(transformed_words)

vowel_count = sum(1 for word in transformed_words if word[0] in 'aeiou')
consonant_count = len(transformed_words) - vowel_count

score = vowel_count * 3 - consonant_count if consonant_count > vowel_count else vowel_count * 2
final_score = score + len(word_counts) if len(word_counts) > 10 else score - len(word_counts)

print(f"Result: {final_score}")