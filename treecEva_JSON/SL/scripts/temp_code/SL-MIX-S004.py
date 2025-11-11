text = "abcabdabcabc"

# Step 1: Extract all 2-character substrings
substrings = []
for i in range(len(text) - 1):
    substr = text[i:i+2]
    substrings.append(substr)

# Step 2: Count frequencies
freq_map = {}
for substr in substrings:
    if substr in freq_map:
        freq_map[substr] += 1
    else:
        freq_map[substr] = 1

# Step 3: Find top 2 most frequent patterns
sorted_patterns = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
top_patterns = sorted_patterns[:2]

# Calculate compression savings
total_occurrences = sum(count for pattern, count in top_patterns)
original_chars = total_occurrences * 2
compressed_chars = len(top_patterns) * 2 + total_occurrences
savings = original_chars - compressed_chars

# Step 4: Apply hash function
pattern_sum = sum(ord(p[0]) + ord(p[1]) for p, c in top_patterns)
compression_hash = (savings * 10 + pattern_sum) % 256

print(f"Result: {compression_hash}")