# A simple text analyzer that counts character frequencies in a sample text

sample_text = "The quick brown fox jumps over the lazy dog."
sample_text = sample_text.lower()

# Initialize dictionaries for tracking
character_frequencies = {}
special_chars = {'.': 'period', ',': 'comma', '!': 'exclamation'}

# Process each character in the text
for char in sample_text:
    if char.isalpha() or char in special_chars:
        if char in character_frequencies:
            character_frequencies[char] += 1
        else:
            character_frequencies[char] = 1

# Calculate statistics
character_count = sum(character_frequencies.values())
unique_letters = len([c for c in character_frequencies if c.isalpha()])

# Display some information about the text
print(f"Sample text length: {len(sample_text)}")
print(f"Character count (excluding spaces): {character_count}")
print(f"Unique letters: {unique_letters}")

# Result: {character_count}