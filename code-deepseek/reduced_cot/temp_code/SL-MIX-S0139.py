text_data = "programming language analysis framework implementation design"
words = text_data.split()

# Intermediate processing (somewhat relevant but not used in final calculation)
vowel_counts = {}
for word in words:
    vowels = set('aeiou')
    count = sum(1 for char in word.lower() if char in vowels)
    vowel_counts[word] = count

# Main calculation with distraction
word_lengths = [len(word) for word in words]
filtered_lengths = [length for length in word_lengths if length > 7]

# Distractor operation (seems relevant but doesn't affect result)
letter_frequency = {}
for word in words:
    for char in word:
        letter_frequency[char] = letter_frequency.get(char, 0) + 1

# Actual logic chain
sorted_lengths = sorted(word_lengths)
middle_index = len(sorted_lengths) // 2
median_length = sorted_lengths[middle_index] if len(sorted_lengths) % 2 == 1 else (sorted_lengths[middle_index - 1] + sorted_lengths[middle_index]) / 2

# Final calculation with intervention
word_set = set(words)
unique_word_count = len(word_set)
final_count = int(median_length * unique_word_count)

# Red herring calculation
character_total = sum(len(word) for word in words)

result = final_count
print(f"Result: {result}")