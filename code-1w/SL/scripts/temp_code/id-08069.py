import math

# Simulate sensor data preprocessing with red herrings
def generate_noise(length, seed=42):
    # Irrelevant function - dead code path
    return [(seed * i + 7) % 100 for i in range(length)]

def deprecated_filter(data):
    # Unused legacy function - distractor
    return [x for x in data if x > 25]

# Core signal processing chain
raw_readings = [12, 34, 56, 78, 91, 15, 22, 64]
offset = 10
adjusted_signal = [val - offset for val in raw_readings]  # List comprehension

# Apply non-linear transformation (logarithmic compression)
compressed_signal = [math.log(x) if x > 0 else 0 for x in adjusted_signal]

# Redundant copy - misleading intermediate
backup_signal = compressed_signal.copy()

# Introduce irrelevant statistical analysis
mean_val = sum(adjusted_signal) / len(adjusted_signal)
variance_proxy = sum((x - mean_val) ** 2 for x in adjusted_signal) / len(adjusted_signal)

# Dummy normalization (not used later)
normalized_data = [x / (max(adjusted_signal) + 1e-9) for x in adjusted_signal]

# Threshold detection via conditional expression
active_segments = [1 if x > 20 else 0 for x in adjusted_signal]
segment_count = sum(active_segments)

# Transform step: apply square root to positive logs
transformed_data = [math.sqrt(x) if x > 0 else 0 for x in compressed_signal]

# Decoy recursive function (never called)
def recursive_sum(arr, n):
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Real processing begins here
threshold = 2.5

# Conditional logic with nesting and distractors
def process_signal(data, limit):
    count = 0
    temp_result = 0
    secondary_accum = 0  # Distractor accumulator
    
    for item in data:
        if item > limit:
            count += 1
            temp_result += item * 2
        else:
            # Misleading branch - looks important but secondary_accum unused
            secondary_accum += item / 2
            if item < 1.0:
                secondary_accum -= 0.1
    
    # Complex condition using boolean logic and comparison
    adjustment_factor = 1.5 if count >= 3 and temp_result > 10 else 0.8
    
    # Final computation
    final_value = int(temp_result * adjustment_factor) - (count * 2)
    
    # Dead code block - unreachable due to structure
    if False:
        fallback = sum(data) // 5
        final_value = fallback
    
    return final_value

# Execution point of interest
final_output = process_signal(transformed_data, threshold)

# Print result as required
print(f"Target result: {final_output}")