# Calculate the value of a word based on letter positions in the alphabet
# a=1, b=2, ..., z=26, ignoring non-alphabetic characters

def get_letter_values():
    # Create a dictionary mapping each letter to its position value
    return {chr(i + 97): i + 1 for i in range(26)}

original_word = "Hello123World!"
filtered_word = ""

# Remove non-alphabetic characters
for char in original_word:
    if char.isalpha():
        filtered_word += char

# Get letter position values
letter_values = get_letter_values()

# Calculate special prefix value (not used in final calculation)
prefix = filtered_word[:3].lower()
prefix_value = 0
for char in prefix:
    prefix_value += letter_values[char]
    
# Calculate the word value based on letter positions
word_value = sum(letter_values[char.lower()] for char in filtered_word)

# Display results
print(f"Filtered word: {filtered_word}")
print(f"Result: {word_value}")