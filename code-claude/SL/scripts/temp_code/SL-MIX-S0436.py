import itertools

# Simple cipher processor
def prepare_message(text):
    # Remove spaces and convert to uppercase
    return text.replace(' ', '').upper()

# Main processing function
message = "hello world"
transformed_message = prepare_message(message)

# Cipher parameters
base_offset = ord('A')  # ASCII value of 'A'
shift_value = 3        # Unused parameter

# Generate some letter patterns (not used in final calculation)
patterns = list(itertools.product('ABC', repeat=2))

# Calculate the cipher value by summing the relative positions
# of each character in the alphabet (A=0, B=1, etc.)
cipher_value = sum([(ord(c) - base_offset) % 26 for c in transformed_message])

# Track letter frequencies (not used in final result)
letter_count = {}
for char in transformed_message:
    letter_count[char] = letter_count.get(char, 0) + 1

print(f"Result: {cipher_value}")