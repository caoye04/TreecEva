from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation and anomaly filtering system
def collect_sensor_readings():
    readings = [15, 22, 8, 47, 33, 21, 9, 40, 33, 18, 24, 33]
    return readings

def apply_noise_filter(data):
    filtered = [x for x in data if x > 10]
    padding = [0] * (16 - len(filtered))
    extended = filtered + padding  # padded to fixed length
    return extended

def compute_baseline(readings):
    return sum(readings) / len(readings)

def flag_anomalies(data, threshold_multiplier=1.8):
    avg = sum(data) / len([x for x in data if x > 0])
    anomalies = []
    for i, val in enumerate(data):
        if val > 0 and val > avg * threshold_multiplier:
            anomalies.append(i)
    return anomalies

def slice_window(data, start=4, size=6):
    return data[start:start+size]

def transform_encoding(raw_seq):
    # Bit manipulation: flip every odd-positioned bit
    transformed = []
    for num in raw_seq:
        flipped = num ^ 0b10101010  # XOR with alternating bit pattern
        transformed.append(flipped & 0xFF)  # Ensure 8-bit
    return transformed

def rolling_checksum(segment):
    checksum = 0
    for i, val in enumerate(segment):
        checksum += val * (i + 1)
    return checksum % 10000

def evaluate_stability(metric):
    if metric < 500:
        return 'LOW'
    elif metric < 2000:
        return 'MEDIUM'
    else:
        return 'HIGH'

def prepare_lookup(anomaly_indices):
    lookup = defaultdict(lambda: 'OK')
    for idx in anomaly_indices:
        lookup[idx] = 'FLAGGED'
    return lookup

def generate_histogram(data):
    histo = Counter(data)
    return histo

def normalize_sequence(seq):
    max_val = max(seq)
    return [round(x / max_val * 100) for x in seq]

def process_chunk(data_chunk, config):
    temp_sum = 0
    factor = config.get('amplification', 1)
    offset = config.get('offset', 0)
    
    for i, val in enumerate(data_chunk):
        if i % 2 == 0:
            temp_sum += val * factor
        else:
            temp_sum -= val + offset
    
    return int(temp_sum)

# Irrelevant auxiliary function - dead path
def deprecated_aggregation(arr):
    total = 0
    for x in arr:
        total += x ** 0.5
    return round(total, 2)

# Misleading intermediate variables
initial_power_draw = 230
projected_load = initial_power_draw * 1.15
baseline_correction_factor = 0.92
hypothetical_ceiling = 95
scaling_vector = [1.05, 0.98, 1.01, 1.03]

# Main execution flow
raw_readings = collect_sensor_readings()
filtered_readings = apply_noise_filter(raw_readings)

# Compute baseline (distractor usage)
baseline_avg = compute_baseline(raw_readings)
anomaly_positions = flag_anomalies(filtered_readings, threshold_multiplier=1.8)

# Create lookup map (unused later)
status_map = prepare_lookup(anomaly_positions)
histogram_counts = generate_histogram(filtered_readings)

# Extract window of interest
windowed_data = slice_window(filtered_readings, start=3, size=8)

# Transform using bit manipulation
encoded_data = transform_encoding(windowed_data)

# Normalize values for UI display (red herring)
normalized_display = normalize_sequence(encoded_data)

# Rolling checksum for integrity (intermediate distraction)
integrity_hash = rolling_checksum(encoded_data)
stability_rating = evaluate_stability(integrity_hash)

# Final processing configuration (only some fields are used)
config_settings = {
    'amplification': 3,
    'offset': 7,
    'mode': 'aggressive',
    'version': '2.1a'
}

# Key statement
final_output = process_chunk(encoded_data, config_settings)

# Print result for evaluation
print(f"Result: {final_output}")