# Analyzing text for unique characters in specific positions
text = "Hello Python Programming World!"
filtered_text = ""

# Remove spaces and convert to lowercase
for char in text:
    if char != " ":
        filtered_text += char.lower()
        
# Count total characters in the filtered text
char_count = len(filtered_text)

# Extract every other character starting from the beginning
# and count unique characters
unique_chars = len(set(filtered_text[::2]))

# Calculate average ASCII value for comparison
avg_ascii = sum(ord(c) for c in filtered_text) / char_count

print(f"Result: {unique_chars}")