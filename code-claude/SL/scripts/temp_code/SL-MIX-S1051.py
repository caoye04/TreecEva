# Analyzing character diversity in a text sample
text_sample = "programming languages use different syntax but share common concepts"
text_length = len(text_sample)

# Create a dictionary to track character frequencies
char_freq = {}
for char in text_sample:
    if char in char_freq:
        char_freq[char] = char_freq[char] + 1
    else:
        char_freq[char] = 1

# Filter out spaces for analysis
filtered_text = ""
for char in text_sample:
    if char != " ":
        filtered_text += char

# Count unique characters in the filtered text
unique_chars = len(set(filtered_text))

# Additional statistics
avg_freq = sum(char_freq.values()) / len(char_freq)
max_freq = max(char_freq.values())

print(f"Result: {unique_chars}")