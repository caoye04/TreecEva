import math

# Simulated sensor data with noise and metadata
timestamps = [1623456780 + i * 30 for i in range(200)]
raw_readings = [math.sin(i * 0.1) * 100 + 50 + (i % 7) * 3 for i in range(200)]
metadata_flags = [({'type': 'A'}, {'active': True}) if i % 3 == 0 else ({'type': 'B'}, {'active': False}) for i in range(200)]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.012
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 1024

# Decoy function - never called but looks important
def decrypt_payload(payload, key):
    return sum([ord(c) ^ key for c in payload]) % 1000

# Unused transformation matrices (dead code path)
transform_matrix = [[1 if i == j else 0.1 for j in range(5)] for i in range(5)]
inverse_transform = [[1 if i == j else -0.1 for j in range(5)] for i in range(5)]

# Security-related variables (misleading intermediate results)
security_key = 1337
encryption_layers = [lambda x: x ^ 255, lambda x: ((x << 3) & 255) | (x >> 5), lambda x: x ^ 86]
encrypted_signature = 0
for b in str(security_key):
    encrypted_signature = encryption_layers[0](encrypted_signature + ord(b))

# Data buffer with red herring operations
buffer_pool = [0] * 64
for i in range(len(buffer_pool)):
    buffer_pool[i] = (i * 17 + 13) % 251
    if buffer_pool[i] % 11 == 0:  # Dead branch (never reached due to mod values)
        buffer_pool[i] = CALIBRATION_FACTOR_A * buffer_pool[i]

# Real data stream construction (relevant path)
data_stream = []
for i in range(0, len(raw_readings), 4):
    block = raw_readings[i:i+4]
    avg = sum(block) / len(block)
    normalized = avg + math.cos(i * 0.05)
    data_stream.append(round(normalized, 2))

# Auxiliary diagnostic info (mostly irrelevant)
diag_stats = {
    'peak': max(data_stream),
    'trough': min(data_stream),
    'span': len(data_stream),
    'noise_floor': 0.7 * sum(data_stream) / len(data_stream),
    'checksum': sum(int(x * 10) for x in data_stream[:10]) % 1000
}

# Core logic hidden among distractions
def analyze_entropy(sequence):
    freq = {}
    for val in sequence:
        rounded = int(val)
        freq[rounded] = freq.get(rounded, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Misdirection: fake anomaly detection (unused)
class AnomalyDetector:
    def __init__(self, sensitivity):
        self.sensitivity = sensitivity
        self.history = []

    def check(self, value):
        return abs(value - sum(self.history[-5:]) / (5 if self.history else 1)) > self.sensitivity

# Actual threshold computation (critical path)
def compute_threshold(signal, key):
    base = sum(x for x in signal if x > 0) / len(signal)
    variation = math.sqrt(sum((x - base) ** 2 for x in signal) / len(signal))
    
    # Hidden dependency on key via bit manipulation
    key_factor = (key ^ (key >> 4) ^ (key << 3)) & 255
    dynamic_adjustment = (key_factor / 100.0) if key_factor % 2 == 1 else (128 / 100.0)
    
    # Conditional expression with slicing distraction
    segment = signal[::3] if len(signal) % 2 == 0 else signal[1::2]
    secondary_influence = sum(segment[:5]) / 5 if len(segment) >= 5 else base
    
    # Lambda-based transformation (idiomatic python)
    apply_gain = lambda x, g: x * (1 + g / 100)
    amplified = apply_gain(variation, 15)
    
    # Final threshold calculation
    threshold = base + amplified - abs(secondary_influence - base) * 0.3
    
    # Red herring: modify diag_stats inside function (side effect but not used)
    if 'intermediate' not in diag_stats:
        diag_stats['intermediate'] = []
    diag_stats['intermediate'].append(threshold)
    
    return round(threshold, 4)

# Spurious post-processing (distraction)
filtered_diagnostics = {k: v for k, v in diag_stats.items() if isinstance(v, (int, float)) and v > 10}
summary_hash = sum(ord(c) for c in str(filtered_diagnostics)) % 500

# Key execution point
filtration_threshold = compute_threshold(data_stream, security_key)

# Additional misleading operation (no effect on answer)
sorted_diagnostics = sorted(diag_stats.items(), key=lambda x: str(x[1]))

# Print result as required
print(f"Result: {filtration_threshold}")