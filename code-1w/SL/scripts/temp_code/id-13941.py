from collections import defaultdict, Counter
import math

def preprocess_signal(raw):
    # Irrelevant preprocessing function (dead code path)
    return [x * 0.95 for x in raw if x > 0]

def detect_spikes(data):
    # Misleading function: detects spikes but not used in final chain
    spikes = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > 80:
            spikes.append(i)
    return spikes

def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]

def filter_anomalies(readings):
    # Only values within 2 std dev are kept
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    filtered = [x for x in readings if abs(x - mean) <= 2 * std_dev]
    
    # Distractor: unused normalization
    normalized_filtered = normalize(filtered)
    
    # Decoy operation: counting digits
    digit_count = defaultdict(int)
    for val in filtered:
        for digit in str(int(val)):
            digit_count[digit] += 1
    
    return filtered

def compute_entropy(arr):
    # Unused advanced metric (red herring)
    counts = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def process_readings(valid_readings):
    # Transform: apply logarithmic scaling
    logged = [math.log(x) if x > 0 else 0 for x in valid_readings]
    
    # Bit manipulation distraction
    bit_modified = []
    for val in valid_readings:
        int_val = int(val)
        transformed = (int_val ^ 255) & 0xFF  # Invert lower byte
        bit_modified.append(transformed)
    
    # Main logic: weighted average based on position
    weighted_sum = 0.0
    weight_sum = 0.0
    for idx, val in enumerate(logged):
        weight = 1 / (idx + 1)  # Higher weight for earlier elements
        weighted_sum += val * weight
        weight_sum += weight
    
    # Additional transformation using string operations
    key_str = "".join([chr(int(b) % 26 + 97) for b in bit_modified[:5]])  # a-z mapping
    adjustment_factor = 0
    for c in key_str:
        if c in 'aeiou':
            adjustment_factor += 1
    
    # Final diagnostic calculation
    base_diagnostic = weighted_sum / weight_sum
    final_diagnostic = int(base_diagnostic * 1000) + adjustment_factor * 5
    
    # Irrelevant assignment
    summary_stats = {
        'count': len(valid_readings),
        'range': max(valid_readings) - min(valid_readings),
        'mode_approx': Counter([round(x) for x in valid_readings]).most_common(1)[0][0]
    }
    
    return final_diagnostic

# Simulated sensor data (physiological readings)
sensor_data = [78, 85, 90, 150, 88, 82, 86, 83, 79, 81, 92, 87, 84, 80, 89]

# Unused spike detection (misdirection)
spike_positions = detect_spikes(sensor_data)

# Key execution point
final_diagnostic = process_readings(filter_anomalies(sensor_data))

# Output result
print(f"Result: {final_diagnostic}")