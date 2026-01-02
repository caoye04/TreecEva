def analyze_text_patterns(input_text):
    # Count frequency of each alphabetic character (case-insensitive)
    char_freq = {}
    for char in input_text.lower():
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Extract counts sorted by character ASCII order
    sorted_counts = [char_freq[c] for c in sorted(char_freq)]
    
    # Compute weighted sum based on position in sorted list
    total_weighted_chars = 0
    for index, count in enumerate(sorted_counts):
        total_weighted_chars += index * count
    
    # Auxiliary variable: average frequency (not used in final result)
    avg_frequency = sum(sorted_counts) / len(sorted_counts) if sorted_counts else 0
    
    # Final computation
    total_weighted_chars = sum(index * char_count for index, char_count in enumerate(char_counts))
    
    return total_weighted_chars

# Input text for analysis
text_sample = "digital language models evaluate complex reasoning tasks"

counts = []
for ch in text_sample:
    if ch.isalpha():
        counts.append(ord(ch.lower()) - ord('a') + 1)

# Create frequency-based count list (one per unique letter, sorted)
seen = set()
char_counts = []
for c in text_sample.lower():
    if c.isalpha() and c not in seen:
        char_counts.append(text_sample.lower().count(c))
        seen.add(c)

# Sort counts by corresponding character
sorted_pairs = sorted(zip([c for c in seen], char_counts), key=lambda x: x[0])
char_counts = [count for _, count in sorted_pairs]

# Execute function-like logic block
result = analyze_text_patterns(text_sample)
print(f"Result: {result}")