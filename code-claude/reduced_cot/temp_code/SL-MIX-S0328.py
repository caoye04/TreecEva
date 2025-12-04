# Calculate the numerical value of a word based on letter positions
# where 'a'=1, 'b'=2, etc.

text = "programming"
capitalized = text.capitalize()
word = capitalized[:5]  # Extract first 5 letters

values = []
for char in word:
    if char.isalpha():
        # Calculate position value (a=1, b=2, etc.)
        position = ord(char.lower()) - ord('a') + 1
        values.append(position)
    else:
        values.append(0)

total_chars = len(text)
prefix_length = len(word)

# Calculate the word value
word_value = sum(values)

print(f"Result: {word_value}")