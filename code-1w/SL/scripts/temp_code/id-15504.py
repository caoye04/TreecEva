import math

# Simulated sensor array data (irrelevant initialization)
sensor_grid_a = [[0 for _ in range(5)] for _ in range(5)]
sensor_grid_b = [[1 for _ in range(4)] for _ in range(4)]

# Irrelevant calibration constants
calibration_x = sum(sum(row) for row in sensor_grid_a)
calibration_y = len(sensor_grid_b) ** 2
dummy_offset = calibration_x * 0.01 + calibration_y * 0.02

# Real signal data stream
raw_signal = [3, 7, 2, 8, 1, 9, 4, 6, 5]

# Signal processing pipeline
noise_floor = 3
filtered_data = [x for x in raw_signal if x > noise_floor]  # Remove low-amplitude noise

# Decoy transformation: unused but plausible
transformed_data = [int(math.sqrt(x * 2)) for x in raw_signal if x % 2 == 0]

def apply_envelope(signal):
    # Irrelevant envelope calculation
    envelope = []
    for i in range(len(signal)):
        envelope.append(signal[i] * (0.5 + 0.5 * math.sin(i)))
    return [round(e, 2) for e in envelope]

# Unused function - red herring
def legacy_filter(data, limit=5):
    result = []
    for val in data:
        if val < limit:
            result.append(val * 2)
        else:
            result.append(val // 2)
    return result

# Bit manipulation decoy
effective_bits = 0
for val in filtered_data:
    effective_bits |= (val & 7)  # Track lower 3 bits OR

# Threshold logic with conditional expression
dynamic_factor = 1.5 if len(filtered_data) > 4 else 0.8
threshold = (sum(filtered_data) / len(filtered_data)) * dynamic_factor

# Set operations - relevant and irrelevant
unique_values = set(filtered_data)
expected_set = {4, 5, 6, 7, 8, 9}
missing_components = expected_set - unique_values  # This is not used later
redundant_check = unique_values | {0, 1, 2}  # Dead operation

# Main analysis function with early returns and nesting
def analyze_signal(data, thresh):
    if not data:
        return -1
    
    cumulative_score = 0
    adjustment = 0
    
    for i, val in enumerate(data):
        if val > thresh:
            adjustment += 0.5
            if i % 2 == 0:
                cumulative_score += val * 2
            else:
                cumulative_score += val
        else:
            adjustment -= 0.2
            # Nested condition with bit check
            if (val & 1) and (cumulative_score > 0):
                cumulative_score -= 1

        # Early termination decoy (never triggered due to data)
        if cumulative_score < -10:
            return -999  # Unreachable with current data
            
    # Final adjustment using conditional expression
    final_weight = 2 if adjustment > 0 else 1
    
    # Core computation
    base_result = cumulative_score * final_weight
    
    # Destructuring assignment - irrelevant but meaningful
    first, *middle, last = data
    span = last - first if len(data) > 1 else 0
    
    # Composite diagnostic formula
    return int(base_result - span + len(middle) * adjustment)

# Execute main logic
interim_check = legacy_filter(transformed_data)  # Dead call
envelope_test = apply_envelope(filtered_data)   # Another dead call

final_diagnostic = analyze_signal(filtered_data, threshold)

# Print final answer as required
print(f"Result: {final_diagnostic}")