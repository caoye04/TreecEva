from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion
def fetch_telemetry():
    raw_signals = [24, 18, 24, 12, 18, 6, 12, 24, 18, 6, 12, 18]
    return {i: val for i, val in enumerate(raw_signals)}

def compute_checksum(sequence):
    # Irrelevant checksum calculation (dead-end)
    chk = 0
    for x in sequence:
        chk = (chk + x) * 7 % 97
    return chk

def generate_frequency_map(data_dict):
    # Extract values and count frequencies
    values = list(data_dict.values())
    freq_map = defaultdict(int)
    for v in values:
        freq_map[v] += 1
    return freq_map

def calculate_entropy(counts):
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def apply_noise_filter(signal_list, threshold=15):
    # Misleading filtering operation (not used in final path)
    filtered = []
    running_avg = 0
    for i, x in enumerate(signal_list):
        running_avg = (running_avg * i + x) / (i + 1) if i > 0 else x
        if abs(x - running_avg) > threshold:
            filtered.append(x * 0.5)
    return filtered

def derive_modular_key(inputs):
    # Decoy function: computes modular key but not used
    acc = 0
    for i, v in inputs.items():
        acc += (i * v) % 13
    return acc % 11

def extract_unique_peaks(data):
    # Another distractor: finds local maxima (unused)
    peaks = []
    vals = list(data.values())
    for i in range(1, len(vals)-1):
        if vals[i] > vals[i-1] and vals[i] > vals[i+1]:
            peaks.append(vals[i])
    return peaks

def analyze_pattern(buffer):
    # Core logic hidden among distractions
    temp_state = 0
    for val in buffer:
        temp_state += (val ** 2) % 19
    temp_state *= 3
    # Final transformation
    temp_state = (temp_state ^ 255) % 10000  # Bitwise XOR with modulus
    return temp_state

# Main execution flow
telemetry_data = fetch_telemetry()

# Irrelevant intermediate steps
checksum = compute_checksum(list(telemetry_data.values()))
noise_test = apply_noise_filter(list(telemetry_data.values()))
decoys = extract_unique_peaks(telemetry_data)
mod_key = derive_modular_key(telemetry_data)

# Frequency analysis - relevant
freq_counts = generate_frequency_map(telemetry_data)
symbol_entropy = calculate_entropy(freq_counts)

# Build entropy buffer based on frequency-derived pattern
entropy_buffer = []
for val, cnt in freq_counts.items():
    if cnt >= 2:
        entropy_buffer.append(val % 7)

# Introduce red herring computation
shadow_buffer = [x * 11 for x in entropy_buffer if x % 2 == 0]
shadow_buffer.extend([1] * (5 - len(shadow_buffer)))  # Padding

# Critical statement
final_diagnostic = analyze_pattern(entropy_buffer)

# Print result as required
print(f"Result: {final_diagnostic}")