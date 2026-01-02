from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
def fetch_sensor_data():
    raw_signals = [0.8, 1.2, -0.5, 3.1, 2.9, -1.1, 0.05, -0.3, 4.2, 3.8]
    timestamps = list(range(1000, 1010))
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'OK', 'UNKNOWN', 'OK', 'OK', 'ERROR']
    return list(zip(raw_signals, timestamps, statuses))

# Irrelevant helper: counts status occurrences but not used in final logic
def count_status_types(data):
    counts = defaultdict(int)
    for _, _, status in data:
        counts[status] += 1
    return counts

# Signal filter using hysteresis thresholding (relevant)
def filter_noisy_signal(signal_list, low=0.1, high=0.9):
    filtered = []
    state = False
    for val, _, _ in signal_list:
        if val > high:
            state = True
        elif val < low:
            state = False
        filtered.append(state)
    return filtered

# Advanced transformation: frequency domain approximation (partially relevant)
def compute_spectral_tendency(binary_sequence):
    toggle_count = 0
    prev = binary_sequence[0]
    for b in binary_sequence[1:]:
        if b != prev:
            toggle_count += 1
        prev = b
    return toggle_count / len(binary_sequence) if binary_sequence else 0

# Auxiliary checksum (red herring)
def validate_checksum(data):
    total = 0
    for val, ts, _ in data:
        total ^= int(abs(val) * 100) ^ ts
    return total % 17

# Data purification with distraction: combines useful and useless steps
def purify_transmission(signal_data):
    purified = []
    noise_floor = 0.05
    for val, ts, status in signal_data:
        if status == 'ERROR':
            continue
        adjusted = abs(val) ** 0.5 if val != 0 else 0
        if adjusted > noise_floor:
            purified.append((adjusted, ts))
    # Distractor: unused sorting
    sorted(purified, key=lambda x: x[1])
    return [p[0] for p in purified]

# Core analysis function with conditional logic and counting
def analyze_signal(cleaned_signal):
    stats = Counter(cleaned_signal)
    mode_val = stats.most_common(1)[0][1]
    total_energy = sum(x**2 for x in cleaned_signal)
    
    # Logical triage using thresholds
    if total_energy < 5:
        level = 1
    elif total_energy < 15:
        level = 2
    else:
        level = 3
    
    # Bitwise signature from mode and level
    signature = (mode_val << 2) | level
    
    # Decoy calculation: entropy-like measure (unused)
    entropy = -sum((freq/len(cleaned_signal)) * math.log(freq/len(cleaned_signal)) 
                   for freq in stats.values()) if cleaned_signal else 0
    
    # Final diagnostic derived from energy and level
    diagnostic_code = int(total_energy) + (level * 1000)
    
    # Dead code branch: never executed due to logic above
    if entropy > 100:
        diagnostic_code ^= 0xFFFF
    
    return diagnostic_code

# Unused recursive function (distractor)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Unused matrix rotation (dead path)
def rotate_matrix_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

# Main execution flow
sensor_input = fetch_sensor_data()

# Irrelevant status count
status_distribution = count_status_types(sensor_input)

# Generate validation checksum (not used later)
transmission_checksum = validate_checksum(sensor_input)

# Filter signal based on hysteresis
active_segments = filter_noisy_signal(sensor_input)

# Compute spectral characteristic (used only for debugging output)
toggle_rate = compute_spectral_tendency(active_segments)

# Purify signal by removing errors and transforming values
processed_data = purify_transmission(sensor_input)

# Final analysis step
final_diagnostic = analyze_signal(processed_data)

# Output result
print(f"Result: {final_diagnostic}")