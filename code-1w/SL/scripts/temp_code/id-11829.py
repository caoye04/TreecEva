import math

def generate_baseline(count):
    return [math.sin(i * 0.1) + 0.5 for i in range(count)]

def corrupt_data(data, factor=2.0):
    # Irrelevant transformation
    return [x * factor + 1.5 for x in data]

def compute_checksum(arr):
    # Distractor function: looks important but unused
    return sum(int(x * 100) for x in arr) % 1007

def filter_outliers(readings, threshold=0.75):
    upper_bound = threshold
    lower_bound = -threshold
    result = []
    for val in readings:
        if lower_bound <= val <= upper_bound:
            result.append(val)
    return result

def rolling_average(values, window=3):
    # Dead code path — never called
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        segment = values[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    return smoothed

def extract_features(data):
    # Decoy feature extraction with irrelevant slicing
    part_a = data[::2]  # Every other element
    part_b = data[1::2]
    total_energy = sum(x**2 for x in part_a)
    peak_magnitude = max(part_b, default=0)
    return total_energy, peak_magnitude

def validate_coherence(signal):
    # Misleading validation that doesn't affect outcome
    if len(signal) < 10:
        return False
    score = sum(1 for x in signal if x > 0.1)
    return score > len(signal) * 0.6

def recursive_transform(seq, depth):
    if depth == 0 or not seq:
        return seq
    shifted = [seq[-1]] + seq[:-1]  # Right rotation
    return recursive_transform(shifted, depth - 1)

def analyze_signal(cleaned):
    # Core logic begins here
    normalized = [x * 2.0 for x in cleaned]  # Amplify signal
    truncated = normalized[:len(normalized)//2]  # Slicing operation (required)
    
    # Set usage to track unique magnitude bands
    magnitude_levels = set()
    for x in truncated:
        level = int(abs(x) * 10)
        magnitude_levels.add(level)
    
    # Key computation
    base_score = sum(truncated)
    adjustment = len(magnitude_levels) * 0.25
    final_score = base_score + adjustment
    
    # Red herring: complex-looking but unused tuple unpacking
    temp_results = (base_score, adjustment, final_score)
    primary, _, derived = temp_results
    
    # Final result depends only on final_score
    return final_score

# Main execution flow
baseline_readings = generate_baseline(50)
corrupted = corrupt_data(baseline_readings, 3.0)
diagnostic_sum = compute_checksum(corrupted)  # Stored but unused
filtered_readings = filter_outliers(baseline_readings, threshold=0.8)

# Unused recursive transformation (distractor)
transformed_signal = recursive_transform(filtered_readings, depth=4)

# This is the key statement
final_diagnostic = analyze_signal(filtered_readings)

# Extract features just before print (irrelevant to answer)
features = extract_features(transformed_signal)

# Validate coherence (misleading side check)
valid = validate_coherence(filtered_readings)

print(f"Result: {final_diagnostic}")