# Analyzing the frequency of letters in a product code

product_code = "ABC123XYZ456ABC789"
valid_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialize counters
letter_counts = {}
total_digits = 0

# Count occurrences of each letter
for char in product_code:
    if char.isalpha() and char in valid_letters:
        letter_counts[char] = letter_counts.get(char, 0) + 1
    elif char.isdigit():
        total_digits += 1

# Find the most frequently occurring letter
most_frequent_letter = max(letter_counts, key=letter_counts.get)

# Calculate a verification value
verification_value = letter_counts[most_frequent_letter] * total_digits

print(f"Most frequent letter: {most_frequent_letter}")
print(f"Letter count: {letter_counts}")
print(f"Verification value: {verification_value}")