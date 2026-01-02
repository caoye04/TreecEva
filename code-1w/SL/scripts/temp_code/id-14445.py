import math

# Simulated sensor data with noise and metadata
timestamps = [1623456780 + i * 10 for i in range(20)]
raw_values = [3.1, 5.7, -2.4, 8.9, 0.0, -1.2, 4.4, 7.7, 9.1, -3.3, 2.2, 6.6, 1.1, -5.5, 8.8, 0.5, -0.8, 3.9, 7.2, 6.3]
quality_flags = [True, False, True, True, False, True, False, True, True, True, False, True, True, False, True, False, True, True, False, True]

# Irrelevant auxiliary mappings (distractor)
region_codes = {'A': 101, 'B': 207, 'C': 313, 'D': 409}
mode_settings = {'debug': False, 'verbose': True, 'safe_mode': True}

# Decoy transformation functions (dead code path)
def decrypt_buffer(buf):
    return [x ^ 255 for x in buf]  # never used

def validate_checksum(data):
    return sum(data) % 256  # unused in logic

# Real processing begins here
filtered_data = [
    val for idx, val in enumerate(raw_values)
    if quality_flags[idx] and abs(val) > 0.5
]

# Apply exponential smoothing (relevant)
smoothed = []
alpha = 0.3
if filtered_data:
    smoothed.append(filtered_data[0])
    for i in range(1, len(filtered_data)):
        smoothed.append(alpha * filtered_data[i] + (1 - alpha) * smoothed[i-1])

# Misleading intermediate calculation (red herring)
mean_raw = sum(raw_values) / len(raw_values)
variance_raw = sum((x - mean_raw) ** 2 for x in raw_values) / len(raw_values)
entropy_approx = math.log(variance_raw) if variance_raw > 0 else 0  # distractor

# Bit manipulation layer: encode sign and magnitude as bit fields (relevant)
encoded = []
for val in smoothed:
    sign_bit = 1 if val < 0 else 0
    magnitude = int(abs(val) * 10) & 0xFF  # scale and clamp to 8 bits
    encoded_val = (sign_bit << 8) | magnitude
    encoded.append(encoded_val)

# Secondary filtering based on bit criteria (relevant)
processed = [e for e in encoded if (e & 0xFF) % 3 == 0]

# Map using enumerated index and apply XOR mask (relevant)
xor_key = 0xAA
masked = [
    (idx ^ val) ^ xor_key 
    for idx, val in enumerate(processed)
]

# Aggregate using modular arithmetic and combinatorics (key step)
total_pairs = len(masked) * (len(masked) - 1) // 2 if len(masked) > 1 else 0
mod_base = 9973
aggregate = sum(masked) % mod_base

# Conditional override decoy (never triggered - red herring)
critical_threshold = 1e-5
if entropy_approx < critical_threshold:
    aggregate = int(math.sqrt(mod_base))

# Final pipeline function combining multiple concepts
def process_pipeline(stream):
    # Simulate stream processing with zip and lambda
    indexed_stream = list(enumerate(stream))
    paired = list(zip([x[1] for x in indexed_stream[::2]], [x[1] for x in indexed_stream[1::2]]))
    
    # Compute pairwise XOR products using lambda
    transformer = lambda a, b: ((a ^ b) * 3) & 0xFFFF
    transformed = [transformer(p[0], p[1]) for p in paired]
    
    # Add dummy offset that depends on timestamp hash (irrelevant)
    ts_hash = sum(timestamps) % 17
    
    # Real aggregation
    result = sum(transformed) - ts_hash  # ts_hash has minimal effect
    
    # Extra obfuscation: min/max clamping with fixed bounds
    return max(-1000000, min(1000000, result))

# Execute main logic
data_stream = masked
final_output = process_pipeline(data_stream)

print(f"Target result: {final_output}")