data = "apple,banana,cherry,date,elderberry"
fruits = data.split(',')
fruit_counts = list(map(lambda x: len(x), fruits))
sorted_counts = sorted(fruit_counts)

# Processing logic
middle_index = len(sorted_counts) // 2
median_length = sorted_counts[middle_index]

# Distractor computations
fruit_lengths = [len(fruit) for fruit in fruits]
max_length = max(fruit_lengths)
avg_length = sum(fruit_lengths) / len(fruit_lengths)

# Core calculation
weighted_score = median_length * 3
vowel_bonus = sum(1 for fruit in fruits if fruit[0] in 'aeiou')
adjustment = vowel_bonus * 2

# Redundant operations
fruit_char_total = sum(len(fruit) for fruit in fruits)
dummy_operation = (fruit_char_total - max_length) // 2

final_score = weighted_score + adjustment
print(f"Result: {final_score}")