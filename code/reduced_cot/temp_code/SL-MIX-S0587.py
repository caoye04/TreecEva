from collections import Counter

text_sample = "programming assessment benchmark"
character_frequency = Counter(text_sample)
character_set = set(text_sample)
unique_character_count = len(character_set)

print(f"Result: {unique_character_count}")