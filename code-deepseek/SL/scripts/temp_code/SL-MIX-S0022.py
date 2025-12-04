text_data = "PyThOn_PrOgRaMmInG_2024"
lowercase_chars = text_data.lower()
vowel_count = sum(1 for char in lowercase_chars if char in 'aeiou')
consonant_count = sum(1 for char in lowercase_chars if char.isalpha() and char not in 'aeiou')
digit_chars = ''.join(char for char in text_data if char.isdigit())
number_value = int(digit_chars) if digit_chars else 0
computation_result = vowel_count * consonant_count + number_value
final_value = computation_result
print(f"Result: {final_value}")