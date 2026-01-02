import math

# Simulated sensor data processing pipeline for environmental monitoring
raw_readings = [2.1, 3.5, 4.8, 5.2, 6.7, 7.3, 8.9, 9.1, 10.5]

# Irrelevant calibration constants (distractor)
calibration_offset = 0.789
dead_band_filter = [0.1 * i for i in range(10)]
scaling_factor = 1.05

# Preprocessing: apply logarithmic correction to stabilize variance
corrected_readings = [math.log(x + 1) for x in raw_readings]

# Misleading intermediate transformation (dead path)
temp_filtered = []
for val in corrected_readings:
    if val > 1.5:
        temp_filtered.append(val * 0.95)

# Actual relevant transformation: sliding window averaging with overlap
transformed_data = []
window_size = 3
for i in range(len(corrected_readings) - window_size + 1):
    window_avg = sum(corrected_readings[i:i+window_size]) / window_size
    transformed_data.append(round(window_avg, 3))

# Decoy function that is defined but not used (red herring)
def legacy_process(data):
    accumulator = 0
    for item in data:
        accumulator += item ** 2
    return accumulator % 7

# Auxiliary functions
def entropy(signal):
    total = 0
    for x in signal:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

def bit_reversal(n):
    # Unused bitwise operation (distractor)
    result = 0
    while n:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Key threshold derived from modular arithmetic on list length
key_threshold = (len(transformed_data) ** 2) % 13

# Another irrelevant computation chain (misdirection)
synthetic_index = 0
for i in range(5):
    synthetic_index += (i * key_threshold) % 4
synthetic_index = math.sqrt(synthetic_index) if synthetic_index > 0 else 0

# Core analysis logic
def analyze_pattern(signal, threshold):
    count_above = 0
    running_sum = 0
    squared_total = 0

    # Nested loop with conditional logic and multiple operations
    for idx, value in enumerate(signal):
        adjusted_val = value + (idx % 3) * 0.1

        # Conditional filtering based on threshold
        if adjusted_val > threshold / 4.0:
            count_above += 1
            
            # Bit manipulation embedded in arithmetic (complex distractor)
            binary_weight = (idx ^ 5) & 3
            if binary_weight > 1:
                adjusted_val *= 1.1

            running_sum += adjusted_val

        # Independent accumulation regardless of condition
        squared_total += value ** 2

    # Composite diagnostic metric combining multiple sources
    stability_metric = math.sqrt(squared_total) / len(signal)
    activity_score = running_sum * count_above

    # Final diagnostic uses only one component, others are distractions
    final_diagnostic = int(activity_score + 0.5)  # Rounded to nearest integer

    # Dead code branch (never executed due to structure)
    if False:
        fallback = entropy(signal)
        final_diagnostic = int(fallback * 100)

    return final_diagnostic

# Execute main analysis
diagnostic_flag = sum(dead_band_filter) > 5.0
if diagnostic_flag:
    pass  # Placeholder for alternate logic (unused)

final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")