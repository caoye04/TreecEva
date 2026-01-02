data_stream = 'aaabbaaccaaeeeddaa'

# Count occurrences of 'a' in the stream
count_a = data_stream.count('a')

# Apply threshold filter: only keep sequences longer than 2 consecutive 'a's
consecutive_count = 0
max_consecutive = 0
for char in data_stream:
    if char == 'a':
        consecutive_count += 1
        max_consecutive = max(max_consecutive, consecutive_count)
    else:
        consecutive_count = 0

# Simulate data quality adjustment
if max_consecutive >= 3:
    adjusted_count = count_a - 2
else:
    adjusted_count = count_a

# Filter data based on pattern presence
filtered_data = [c for c in data_stream if c in 'ae']

# Scaling factor based on initial density
scaling_factor = 1.5

# Critical computation point
final_score = adjusted_count * scaling_factor + len(filtered_data)

print(f"Result: {final_score}")