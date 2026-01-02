def analyze_sequence(data):
    count_vowels = 0
    for char in data.lower():
        if char in 'aeiou':
            count_vowels += 1
    return count_vowels

sequence = 'computational'
letter_count = len(sequence)
vowel_total = analyze_sequence(sequence)

# Basic counting and adjustment logic
total_base = letter_count * 2 + vowel_total
offset = letter_count - vowel_total

# Perform final score calculation
def final_adjustment(base, diff):
    if diff > 3:
        return base + (diff * 1.5)
    else:
        return base + diff

processed_score = final_adjustment(total_base, offset)

# Print result as required
print(f"Result: {processed_score}")