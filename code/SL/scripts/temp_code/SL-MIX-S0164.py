def char_counter(text):
    vowels = 'aeiouAEIOU'
    temp_text = text.strip().lower()
    vowel_count = sum(1 for char in temp_text if char in vowels)
    consonant_filter = lambda s: sum(1 for c in s if c.isalpha() and c not in vowels)
    consonant_count = consonant_filter(temp_text)
    final_count = vowel_count * 2 - consonant_count
    return final_count

text_sample = "   Programming Tasks Evaluation   "
final_count = char_counter(text_sample)
print(f"Result: {final_count}")