from collections import Counter

text_sample = "programming evaluation benchmark"
char_counter = Counter(text_sample.replace(" ", ""))

vowel_set = {'a', 'e', 'i', 'o', 'u'}
consonant_count = sum(1 for char in text_sample if char.isalpha() and char.lower() not in vowel_set)
vowel_count = sum(1 for char in text_sample if char.lower() in vowel_set)

unique_counts = {}
unique_counts["vowels"] = len(set(char for char in text_sample if char.lower() in vowel_set))
unique_counts["consonants"] = len(set(char for char in text_sample if char.isalpha() and char.lower() not in vowel_set))

final_count = unique_counts["vowels"] - unique_counts["consonants"]

print(f"Result: {final_count}")