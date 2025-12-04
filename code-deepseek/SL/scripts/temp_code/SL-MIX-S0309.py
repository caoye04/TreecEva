vowels = ['a', 'e', 'i', 'o', 'u']
letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
vowels_set = set(vowels)
letters_set = set(letters)
processed_letters = letters_set.union({'x', 'y', 'z'})
final_count = len(processed_letters - vowels_set)
print(f"Result: {final_count}")