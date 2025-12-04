# Text processing utility to analyze alphanumeric content
text = "Hello, World! Python 3.9 is amazing."

# Extract only characters that meet certain criteria
lower_bound = ord('a')  # ASCII for 'a'
upper_bound = ord('z')  # ASCII for 'z'

# Apply initial transformation
transformed = text.lower()

# Filter out punctuation marks
punctuation = ",.!?;:()"
filtered_text = ''.join(char for char in transformed if char not in punctuation)

# Count characters meeting specific criteria
digit_count = len([c for c in filtered_text if c.isdigit()])

# Calculate the number of valid alphabetic characters
valid_count = sum(1 for c in filtered_text if c.isalpha())

# Alternative counting approach (not used)
space_count = filtered_text.count(' ')

print(f"Result: {valid_count}")