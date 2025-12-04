from collections import Counter, defaultdict

def calculate_xor_checksum(values):
    # Calculate XOR checksum of all values
    checksum = 0
    for val in values:
        checksum ^= val
    return checksum

def calculate_signature(sequence):
    # Calculate a signature based on sequence properties
    if not sequence:
        return -1
    
    # Count occurrences of each element
    element_counts = Counter(sequence)
    
    # Find the most common element and its count
    most_common = element_counts.most_common(1)[0]
    
    # Calculate the signature
    return most_common[0] * most_common[1]

# Initialize data structures for analysis
raw_data = [5, 8, 3, 2, 5, 1, 5, 9, 5, 6, 3, 2, 5]
processed_values = []
filtered_values = defaultdict(list)

# Process the raw data
for idx, value in enumerate(raw_data):
    # Apply complex transformation
    transformed = (value * 2) % 10
    processed_values.append(transformed)
    
    # Track some metrics that won't be used
    if idx % 2 == 0:
        filtered_values['even_indices'].append(value)
    else:
        filtered_values['odd_indices'].append(value)

# Calculate some analytics that won't be used
analysis_results = {
    'max_value': max(raw_data),
    'min_value': min(raw_data),
    'range': max(raw_data) - min(raw_data),
    'average': sum(raw_data) / len(raw_data)
}

# Apply filtering criteria
threshold = 4
filtered_sequence = []
for value in raw_data:
    if value >= threshold:
        filtered_sequence.append(value)

# This is a misleading operation
misleading_result = calculate_xor_checksum(filtered_sequence)

# Extract every third element for another analysis (not used in final result)
extracted_elements = raw_data[::3]
extracted_signature = calculate_signature(extracted_elements)

# Calculate the signature of the filtered sequence
sequence_signature = calculate_signature(filtered_sequence)

# Some more distraction operations
if misleading_result > 10:
    alternative_signature = sequence_signature + 5
else:
    alternative_signature = sequence_signature - 3

# Print results
print(f"Analysis complete with {len(filtered_sequence)} filtered elements")
print(f"XOR Checksum: {misleading_result}")
print(f"Alternative signature: {alternative_signature}")
print(f"Result: {sequence_signature}")