import itertools

def sequence_filter(data, threshold):
    """Filter values above threshold and return the filtered sequence."""
    return [x for x in data if x <= threshold]

# Dataset representing sensor readings from different monitoring stations
sensor_readings = [2, 5, 3, 8, 1, 4, 7, 6]

# Only consider readings below sensitivity threshold
sensitivity = 5
filtered_sequence = sequence_filter(sensor_readings, sensitivity)

# Calculate number of unique combinations (with replacement) of size 2
# from the filtered sequence
unique_combinations = len(list(itertools.combinations_with_replacement(filtered_sequence, r=2)))

# Some additional processing (not relevant to the answer)
temp_var = sum(filtered_sequence) / len(filtered_sequence)
weighted_avg = temp_var * 1.5

print(f"Result: {unique_combinations}")