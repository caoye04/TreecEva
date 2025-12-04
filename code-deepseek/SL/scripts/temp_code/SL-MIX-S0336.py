from collections import Counter

# Analyze character frequency in a text sample
text_sample = "programming assessment benchmark"
char_frequency = Counter(text_sample)

# Identify characters that appear at least twice
frequent_chars = {char for char, count in char_frequency.items() if count >= 2}

# Convert characters to ASCII values and filter
ascii_values = [ord(char) for char in frequent_chars]
filtered_set = {value for value in ascii_values if value % 2 == 0}

# Calculate final result
scaling_factor = len(filtered_set)
result = sum(filtered_set) * scaling_factor

print(f"Target result: {result}")