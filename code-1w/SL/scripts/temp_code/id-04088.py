import itertools

# Simulated sensor array data from environmental monitoring stations
data_stream = [102, 115, 98, 203, 198, 256, 178, 165, 312, 45, 67, 89, 99, 101, 205, 210, 195, 188, 177, 166]

# Irrelevant calibration constants (distractor)
calibration_factors = [0.98, 1.02, 0.99, 1.01, 1.05]
decoys = {'x': 10, 'y': [i**2 for i in range(15)], 'z': sum([i * 0.5 for i in range(20)])}

# Misleading preprocessing path (dead code)
def legacy_normalize(arr):
    return [x / max(arr) for x in arr]  # Unused function

# Actual filtering logic buried among distractions
def extract_anomalies(sequence, limit):
    # Nested comprehension with slicing distraction
    windowed = [sequence[i:i+4] for i in range(0, len(sequence)-3)]
    peaks = []
    for window in windowed:
        if any(x > limit * 1.5 for x in window):  # Primary filter condition
            peaks.extend([x for x in window if x > limit])
    return list(set(peaks))  # Remove duplicates

# Decoy transformation chain
transform_chain = lambda lst: [v * 2 for v in lst if v % 2 == 0]
phantom_result = transform_chain(data_stream[:10])

# Real processing begins here — obscured by context
baseline_reference = sum(data_stream) / len(data_stream)
threshold = int(baseline_reference * 0.9)

# Complex filtering using itertools and conditional logic
filtered_data = [val for val in data_stream 
                  if val > threshold and 
                  val not in [data_stream[0], data_stream[-1]]]

# Additional red herring: unused generator expression
idle_pairs = list(itertools.combinations([x for x in filtered_data if x < 200], 2))

# Core diagnostic computation hidden in abstraction
def process_readings(readings, cutoff):
    # Bit manipulation decoy
    magic_mask = 0b101010
    masked_sum = sum(r ^ magic_mask for r in readings[:5])  # Distracting calculation
    
    # Actual logic: weighted contribution based on thresholds
    high_priority = [r for r in readings if r > cutoff + 50]
    medium_priority = [r for r in readings if cutoff <= r <= cutoff + 50]
    
    # Conditional expression mix
    adjustment = 1.25 if len(high_priority) > 2 else 0.85
    
    # Critical intermediate (misleading name)
    temp_score = sum(high_priority) * adjustment
    
    # Final computation buried in nested structure
    secondary_boost = 0
    for idx, val in enumerate(medium_priority):
        if idx % 2 == 0:
            secondary_boost += val * 0.1
    
    # Real answer derived here
    final_diagnostic = int(temp_score + secondary_boost)
    
    # Dead branch (never executed)
    if False:
        final_diagnostic *= 2  # Obvious decoy
    
    return final_diagnostic

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold)

# Output required result
print(f"Target result: {final_diagnostic}")