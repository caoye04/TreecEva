text_data = "Programming paradigms include functional, object-oriented, and procedural approaches"

# Define lambda function for character filtering
count_specific = lambda text, chars: sum(1 for c in text if c in chars)

# Count vowels and spaces
vowel_count = count_specific(text_data, 'aeiouAEIOU')
space_count = count_specific(text_data, ' ')

# Some intermediate calculations (minimal distraction)
temp_sum = vowel_count + space_count
adjusted_count = temp_sum - 3

# Final result calculation
final_count = adjusted_count * 2
result = final_count

print(f"Target result: {result}")