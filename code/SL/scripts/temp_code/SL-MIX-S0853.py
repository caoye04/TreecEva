from collections import Counter

input_text = "programming_challenge"
char_frequency = Counter(input_text)
# Calculate the count of unique characters
unique_chars = len(set(input_text))
print(f"Result: {unique_chars}")