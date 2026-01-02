import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [2.1, 3.5, 4.8, 5.2, 6.9, 7.0, 8.1, 9.3, 10.5]
baseline_offset = 2.0
smoothing_factor = 0.85

def apply_filter(data, factor):
    filtered = []
    for i in range(len(data)):
        if i == 0:
            filtered.append(data[i])
        else:
            smoothed = factor * data[i] + (1 - factor) * filtered[i-1]
            filtered.append(smoothed)
    return filtered

def generate_checksum(sequence):
    # Irrelevant utility: computes XOR of integer parts
    checksum = 0
    for val in sequence:
        checksum ^= int(val)
    return checksum

def evaluate_stability(metric):
    # Distractor function: not used in final calculation
    return "stable" if metric > 5.0 else "unstable"

def extract_peaks(series, min_threshold):
    peaks = []
    for i in range(1, len(series)-1):
        if series[i] > series[i-1] and series[i] > series[i+1] and series[i] > min_threshold:
            peaks.append(series[i])
    return peaks

def compute_entropy(values):
    # Dead code path: calculates entropy but unused
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def normalize readings(readings, offset):
    return [r - offset for r in readings]

def transform_sequence(nums):
    # Applies complex transformation with slicing and conditional logic
    rev = nums[::-1]
    mid = len(rev) // 2
    left_half = rev[:mid]
    right_half = rev[mid:]
    
    adjusted = []
    for i in range(max(len(left_half), len(right_half))):
        l_val = left_half[i] if i < len(left_half) else 0.0
        r_val = right_half[i] if i < len(right_half) else 1.0
        # Conditional expression used
        adjusted.append(l_val ** 0.5 if l_val > r_val else r_val ** 0.5)
    
    # Add decoy manipulation
    temp_result = sum(adjusted) / len(adjusted)
    extra_shift = math.sin(temp_result)
    return [x + extra_shift for x in adjusted]

def analyze_pattern(data, limit):
    # Core logic hidden among red herrings
    magnitude = 0
    for val in data:
        if val > limit:
            magnitude += int(val) * 2
        elif val > limit - 2:
            magnitude += int(val)
    
    # Key branching logic with short-circuit evaluation
    adjustment = len(data) > 5 and len(set(data)) < 7
    modifier = adjustment * 3 + 1  # Influences final result
    
    # Final computation
    result = magnitude * modifier
    
    # Decoy intermediate
    dummy_analysis = {"score": result * 0.1, "flagged": False}
    
    return result

# Main execution flow
offset_readings = normalize_readings(raw_readings, baseline_offset)
filtered_signal = apply_filter(offset_readings, smoothing_factor)

# Irrelevant transformations (distractors)
peak_values = extract_peaks(filtered_signal, 3.0)
signal_entropy = compute_entropy(filtered_signal)
checksum_value = generate_checksum(filtered_signal)

# Critical data transformation
transformed_data = transform_sequence(filtered_signal)

# Set operation used: determine uniqueness and apply logic
unique_count = len(set([round(x, 1) for x in transformed_data]))
threshold = 2.5 if unique_count > 6 else 3.0

# Early return simulation via conditional expression
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output required format
print(f"Target result: {final_diagnostic}")