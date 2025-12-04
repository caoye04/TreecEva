from collections import Counter

message = "programming challenges are fun"
decoding_offset = 3

# Remove spaces for analysis
clean_message = message.replace(" ", "")

# Count letter frequencies
letter_frequency = Counter(clean_message)

# Find letters that appear exactly once
unique_letters = sum(1 for count in letter_frequency.values() if count == 1)

# Some additional information about the message
total_chars = len(clean_message)
avg_frequency = total_chars / len(letter_frequency) if letter_frequency else 0

# Decode a simple Caesar cipher (not relevant to the answer)
decoded = ''.join(chr((ord(c) - ord('a') + decoding_offset) % 26 + ord('a')) if c.isalpha() else c for c in message)

print(f"Result: {unique_letters}")