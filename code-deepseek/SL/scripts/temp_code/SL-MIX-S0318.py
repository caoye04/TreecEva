text_data = "PyThOnPrOgRaMmInG"
vowel_count = sum(1 for char in text_data if char.lower() in 'aeiou')
consonant_analysis = {char: ord(char) for char in text_data if char.isalpha()}
processed_chars = [c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text_data)]
case_pattern = ''.join(processed_chars)
char_frequency = {}
for char in case_pattern:
    if char.isalpha():
        char_frequency[char] = char_frequency.get(char, 0) + 1
vowel_distraction = vowel_count * 2 - len(text_data)
final_count = sum(char_frequency.values())
print(f"Result: {final_count}")