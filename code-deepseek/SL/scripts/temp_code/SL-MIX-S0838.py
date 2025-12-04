def process_text(text):
    vowels = 'aeiouAEIOU'
    temp = [char for char in text if char.isalpha()]
    count_vowels = len([c for c in temp if c in vowels])
    count_consonants = len([c for c in temp if c not in vowels])
    difference = abs(count_vowels - count_consonants)
    final_count = difference * 3 if difference > 0 else 5
    return final_count

text_sample = "Programming is fascinating!"
final_count = process_text(text_sample)
print(f"Result: {final_count}")