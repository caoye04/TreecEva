text_data = "PYTHON Programming Challenge: Analyze THIS text carefully"
word_list = text_data.lower().split()

# Main processing
character_count = sum(len(word) for word in word_list)
special_words = [word for word in word_list if word.startswith(('p', 'c'))]

# Intermediate calculations (some not used in final result)
temp_sum = len(special_words) * 3
vowel_count = sum(1 for char in text_data.lower() if char in 'aeiou')

# Core logic
processed_total = character_count - len(word_list)
adjustment_factor = 1.5 if len(special_words) > 2 else 1.2

# Distractor calculations
unused_value = vowel_count * 2 + temp_sum

# Final result
final_score = processed_total * adjustment_factor
print(f"Result: {final_score}")