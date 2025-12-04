# Analyzing text for vowel frequency in a specific section

text = "The quick brown fox jumps over the lazy dog"
start_idx = 4
end_idx = 19

# List of vowels to check against
vowels = "aeiou"

# Some preliminary text analysis
word_count = len(text.split())
letter_count = len([c for c in text if c.isalpha()])

# Extract the relevant section and count vowels
selected_text = text[start_idx:end_idx]
print(f"Selected text: '{selected_text}'")

# Count vowels in the selected text section
vowel_count = len([c for c in text[start_idx:end_idx] if c.lower() in vowels])

# Calculate percentage of vowels in the selected text
vowel_percentage = (vowel_count / len(selected_text)) * 100 if selected_text else 0

print(f"Result: {vowel_count}")