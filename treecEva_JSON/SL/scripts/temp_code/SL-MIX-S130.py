recipe_names = ['Lasagna', 'Beef Wellington', 'Tiramisu', 'Caesar Salad']
vowel_set = {'a', 'e', 'i', 'o', 'u'}
total_vowel_count = 0
for name in recipe_names:
    lower_name = name.lower()
    for char in lower_name:
        if char in vowel_set:
            total_vowel_count += 1
print(f'Result: {total_vowel_count}')