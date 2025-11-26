text_data = "Python programming involves various data structures and algorithms"
vowel_count = sum(1 for char in text_data if char.lower() in 'aeiou')
consonant_count = sum(1 for char in text_data if char.lower() not in 'aeiou' and char.isalpha())
total_chars = len(text_data)
space_count = text_data.count(' ')

# Some intermediate calculations that don't affect the final result
char_ratio = vowel_count / consonant_count if consonant_count > 0 else 0
word_count = len(text_data.split())
avg_word_length = total_chars / word_count if word_count > 0 else 0

# Main logic chain
filtered_vowels = sum(1 for char in text_data if char.lower() in 'aeiou' and char.isupper())
processed_count = vowel_count - filtered_vowels
factor = 3 if processed_count > 10 else 5
adjustment = consonant_count % 4

# Final calculation with some irrelevant operations mixed in
base_value = processed_count * 2
intermediate = base_value + adjustment
final_result = processed_count * factor - adjustment

print(f"Result: {final_result}")