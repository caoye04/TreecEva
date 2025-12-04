from collections import Counter

# Analyzing bit patterns in sensor readings
sensor_data = [(12, 5), (8, 3), (15, 7), (8, 3), (4, 2)]

# Extract values and apply bitwise operations
bit_patterns = []
for primary, secondary in sensor_data:
    # Combine readings using XOR
    combined = primary ^ secondary
    bit_patterns.append(combined)

# Count frequency of each unique bit pattern
bit_frequencies = Counter(bit_patterns)

# Store number of unique bit patterns
unique_count = len(bit_frequencies)

# Calculate sum of all patterns for verification
total = sum(bit_patterns)

print(f"Result: {unique_count}")