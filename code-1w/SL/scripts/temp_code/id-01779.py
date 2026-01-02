def calculate_efficiency(data, limit):
    filtered_data = [row[1:-1] for row in data if sum(row) < limit]
    flattened = [item for sublist in filtered_data for item in sublist]
    if not flattened:
        return 0.5
    avg = sum(flattened) / len(flattened)
    return avg * 0.9

# Simulate sensor profile matrix from thermal imaging
data_stream = [[12, 15, 14, 13, 16],
                [10, 11, 19, 12, 9],
                [14, 13, 12, 11, 10],
                [20, 21, 18, 17, 22]]

# Irrelevant transformation - red herring
doubled_stream = [[val * 2 for val in row] for row in data_stream]
sum_doubled = sum([sum(row) for row in doubled_stream])

# Threshold based on environmental conditions
threshold = 60
scaling_factor = 1.75

# Misleading intermediate calculation (dead-end)
baseline_offset = 0
for row in data_stream:
    if len(row) > 4:
        baseline_offset += row[0] * 0.1

# Core processing with slicing and conditional logic
profile_matrix = [
    [x for x in row if x % 2 == 1] if sum(row) > 50 else [x for x in row if x % 2 == 0]
    for row in data_stream
]

# Another distraction: character encoding simulation (no effect)
text_tag = "THERMAL_DIAG_01"
encoded_tag = ''.join(chr(ord(c) + 1) for c in text_tag)
checksum = sum([ord(c) for c in encoded_tag]) % 100

# Key computational step
thermal_capacity = calculate_efficiency(profile_matrix, threshold) * scaling_factor

# Print final result as required
print(f"Target result: {thermal_capacity}")