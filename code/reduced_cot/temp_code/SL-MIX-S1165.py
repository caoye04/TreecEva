import itertools

cipher_text = "ABC"
decoding_map = {'A': 1, 'B': 2, 'C': 3}
transform = lambda x: x * 2

# Decode each character and apply transformation
decoded_values = [transform(decoding_map[char]) for char in cipher_text]

# Calculate sum of decoded values
decoded_sum = sum(decoded_values)

print(f"Result: {decoded_sum}")