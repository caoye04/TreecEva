def counter_func(text):
    count_vowels = lambda s: sum(1 for char in s if char in 'aeiou')
    vowel_tracker = count_vowels(text)
    consonant_check = len([c for c in text if c.isalpha() and c not in 'aeiou'])
    final_count = vowel_tracker * 2 - consonant_check
    return final_count

final_count = counter_func("abracadabra")
print(f"Result: {final_count}")