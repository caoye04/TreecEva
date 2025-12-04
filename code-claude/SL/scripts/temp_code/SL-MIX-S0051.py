# Function to analyze text files for character frequency and overlap

def get_char_frequency(text):
    # Count character occurrences (case-insensitive)
    return {c.lower(): text.lower().count(c.lower()) for c in set(text.lower())}

# Sample text snippets from two documents
doc1 = "Python programming is enjoyable and rewarding!"
doc2 = "Java programming can be challenging but rewarding."

# Calculate character frequencies
doc1_freq = get_char_frequency(doc1)
doc2_freq = get_char_frequency(doc2)

# Find common characters between documents
chars1 = set(doc1_freq.keys())
chars2 = set(doc2_freq.keys())
common_chars = chars1.intersection(chars2)

# Calculate unique characters in each document
unique_to_doc1 = chars1 - chars2
unique_to_doc2 = chars2 - chars1

# Potential similarity index (unused in final calculation)
potential_index = len(common_chars) / (len(chars1) + len(chars2) - len(common_chars))

# Calculate the average frequency of common characters in doc1
avg_freq_doc1 = sum(doc1_freq[char] for char in common_chars) / len(common_chars) if common_chars else 0

# Apply weighting to the overlapping characters
weight_factor = 1.5  # Arbitrary weight factor
weighted_overlap = len(common_chars) * weight_factor

# Track character positions for visualization (not used in final calculation)
char_positions = {}
for i, char in enumerate(doc1.lower()):
    if char not in char_positions:
        char_positions[char] = []
    char_positions[char].append(i)

# Calculate the overlapping characters (our target value)
overlapping_chars = len(common_chars)

# Compute a combined metric (not used in final calculation)
combined_metric = overlapping_chars * (1 - len(unique_to_doc1) / len(chars1))

# Calculate the total unique characters across both documents
total_unique = len(chars1.union(chars2))

# Display results
print(f"Document 1: {len(chars1)} unique characters")
print(f"Document 2: {len(chars2)} unique characters")
print(f"Total unique across both: {total_unique}")
print(f"Overlapping characters: {overlapping_chars}")

# Result: {overlapping_chars}