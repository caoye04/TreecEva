# Count unique characters in a filtered text
original_text = "Hello, Programming World!"
filter_vowels = True
include_spaces = False
all_vowels = "aeiouAEIOU"
filtered_text = ""

# Process the text
for char in original_text:
    # Skip vowels if filter is on
    if filter_vowels and char.lower() in all_vowels.lower():
        continue
    # Skip spaces if not included
    if not include_spaces and char.isspace():
        continue
    filtered_text += char

# Calculate statistics
char_count = len(filtered_text)
unique_count = len(set(filtered_text))
alpha_count = sum(1 for c in filtered_text if c.isalpha())

print(f"Original text: {original_text}")
print(f"Filtered text: {filtered_text}")
print(f"Result: {unique_count}")