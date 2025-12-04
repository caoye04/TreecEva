# Analyzing character frequency in a message
message = "hello world python programming"

# Extract unique characters from the message
unique_chars = set(message)

# Count occurrences of each character
char_counts = {}
for char in message:
    if char in char_counts:
        char_counts[char] = char_counts[char] + 1
    else:
        char_counts[char] = 1

# Find the top 3 most common characters
sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
most_common_chars = {char for char, count in sorted_chars[:3]}

# Calculate how many times the most common characters appear in the message
letter_frequency = sum(map(lambda x: 1 if x in most_common_chars else 0, message))

print(f"Result: {letter_frequency}")