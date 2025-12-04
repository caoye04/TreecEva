# Calculate the weighted sum of vowels in a text
# Each vowel has a different weight based on its position in 'aeiou'

text = "hello python programming world"
temperature = 22.5  # Current room temperature in Celsius

# Define vowels and their base weights
vowels = "aeiou"
base_multiplier = 2

# Function to count weighted vowels in a character
counter = lambda char: (vowels.index(char) + 1) * base_multiplier if char.lower() in vowels else 0

# Some system information (not relevant for calculation)
system_active = True
max_length = 100

# Calculate the weighted sum of vowels
vowel_weight = sum(map(counter, text))

# Display some stats
print(f"Text length: {len(text)}")
print(f"Result: {vowel_weight}")