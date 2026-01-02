import math

# Sensor simulation and diagnostic analysis system
def generate_noise(length, seed=42):
    # Irrelevant function: simulates noise but not used in final calculation
    result = []
    val = seed
    for i in range(length):
        val = (val * 937) % 101
        result.append((val % 100) / 100.0)
    return result

def deprecated_filter(data):
    # Dead code path: never called
    return [x for x in data if x > 0.5]

def collect_readings():
    # Simulated sensor readings from multiple sources
    raw_readings = [
        [12, 15, 14, 18, 20],
        [8, 10, 11, 13, 12],
        [25, 24, 26, 23, 27],
        [5, 6, 5, 7, 6]
    ]
    weights = [0.1, 0.3, 0.4, 0.2]  # Weight per sensor group
    weighted_avg = []
    for i in range(len(raw_readings[0])):
        avg = sum(raw_readings[j][i] * weights[j] for j in range(4))
        weighted_avg.append(round(avg, 2))
    return raw_readings, weighted_avg

def transform_signal(signal, factor=1.05):
    # Applies gain factor and converts to dB-like scale
    adjusted = [round(x * factor, 3) for x in signal]
    db_values = [10 * math.log10(abs(x) + 1) for x in adjusted]  # Avoid log(0)
    normalized = [min(max(x, 0), 10) for x in db_values]  # Clamp to 0-10
    return normalized

def compute_entropy(data):
    # Misleading intermediate metric: looks important but unused in final result
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def validate_integrity(checksum_list):
    # Unused validation routine (red herring)
    base = checksum_list[0]
    diffs = [abs(checksum_list[i] - base) for i in range(1, len(checksum_list))]
    return all(d < 3 for d in diffs)

def analyze_readings(processed):
    # Core logic: counts how many readings exceed dynamic threshold
    base_threshold = 6.5
    adjustment = len(processed) * 0.1  # Minor tweak based on count
    threshold = base_threshold - adjustment
    
    # Count readings above adjusted threshold
    count_above = sum(1 for x in processed if x > threshold)
    
    # Apply quadratic weighting based on position (more weight to later readings)
    weighted_sum = sum(x * (i * 0.1 + 1) for i, x in enumerate(processed))
    
    # Final diagnostic score combines count and trend
    trend_bias = sum((processed[i+1] - processed[i]) for i in range(len(processed)-1))
    final_score = count_above * 100 + int(weighted_sum) + int(trend_bias * 10)
    
    return final_score

# Main execution flow
raw_data, averages = collect_readings()

# Transform each sensor's time-series data (only first sensor used in final path)
transformed_signal = transform_signal(averages)  # This is the actual input

# Irrelevant transformations on unused data
noise_pattern = generate_noise(5)
dummy_diagnostics = [transform_signal(row, 0.95) for row in raw_data]

# Fake integrity check with decoy variables
checksum_candidates = [sum(row) for row in raw_data]
valid = validate_integrity(checksum_candidates)

# Compute meaningless entropy
entropy_value = compute_entropy(transformed_signal)  # Looks important, unused

# Key transformation: only this matters
transformed_data = [round(x + 0.5, 2) for x in transformed_signal]  # Final preprocessing

# Introduce dead assignment (misleading)
final_diagnostic = -1
final_diagnostic = analyze_readings(transformed_data)

print(f"Result: {final_diagnostic}")