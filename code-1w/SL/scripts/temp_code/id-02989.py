from collections import defaultdict
import math

# Simulated sensor data with noise and metadata
data_packet = [
    {'id': 'A7', 'readings': [1.2, 3.4, -2.1, 5.6], 'status': 'active', 'calib': 0.98},
    {'id': 'B3', 'readings': [0.0, -1.1, 4.4, 2.2], 'status': 'inactive', 'calib': 1.02},
    {'id': 'C9', 'readings': [2.2, 3.3, 1.1, -5.5], 'status': 'active', 'calib': 0.95}
]

# Irrelevant helper that looks important but isn't used in main logic
def legacy_transform(x):
    return [val ** 2 + 1 for val in x if val > 0]

def normalize_readings(readings, factor):
    # Normalize using calibration factor
    return [r * factor for r in readings]

# Decoy function that computes something plausible but unused
def compute_entropy(data):
    total = sum(abs(x) for x in data)
    if total == 0:
        return 0.0
    probs = [abs(x)/total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Misleading intermediate: looks like it's aggregating but isn't part of final path
aggregate_snapshot = defaultdict(float)
for entry in data_packet:
    key = entry['id'][0]
    aggregate_snapshot[key] += sum(entry['readings'])

# Signal processing pipeline
filtered_entries = []
for entry in data_packet:
    if entry['status'] != 'active':
        continue
    corrected = normalize_readings(entry['readings'], entry['calib'])
    filtered_entries.append(corrected)

# Flatten all corrected readings into single list
flattened = []
for seq in filtered_entries:
    for val in seq:
        flattened.append(val)

# Apply windowed transformation (only odd-indexed windows contribute)
temp_buffers = []
window_size = 3
for i in range(len(flattened) - window_size + 1):
    window = flattened[i:i+window_size]
    transformed = sum(w * (idx+1) for idx, w in enumerate(window))  # Weighted sum
    temp_buffers.append(transformed)

# Only keep odd-positioned results (1-indexed interpretation)
processed_data = [x for i, x in enumerate(temp_buffers) if (i+1) % 2 == 1]

# Red herring: string-based checksum that looks diagnostic but unused
diagnostic_tag = "SIG-" + str(len(filtered_entries))
diag_sum = sum(ord(c) for c in diagnostic_tag) % 100

# Real analysis begins here — uses lambda for dynamic threshold filtering
adaptive_filter = lambda arr, t: [a for a in arr if abs(a) > t]

refined = adaptive_filter(processed_data, 2.5)

# Compute energy signature using bitwise manipulation (simulate low-level processing)
energy_signature = 0
for val in refined:
    int_part = int(abs(val) * 10) & 0xFF  # Scale and mask to 8 bits
    sign_bit = 0 if val >= 0 else 1
    energy_signature ^= (int_part << 1) | sign_bit  # XOR into hash

# Secondary analysis: phase coherence (uses another layer of filtering)
coherence_windows = []
for i in range(0, len(refined) - 1, 2):
    coherence = abs(refined[i] - refined[i+1]) if i+1 < len(refined) else 0
    coherence_windows.append(coherence)

avg_coherence = sum(coherence_windows) / len(coherence_windows) if coherence_windows else 0.0

# Final diagnostic computation: mix of arithmetic, bit ops, and scaling
baseline_score = len(refined) * 100
adjustment_factor = (energy_signature & 0xFFFF) ^ (int(avg_coherence * 100) << 2)
final_diagnostic = baseline_score - adjustment_factor

# Dead code path — looks like logging but never called
def generate_report(code, level):
    prefix = f"[REPORT:L{level}]:"
    return prefix + str(code)

print(f"Result: {final_diagnostic}")