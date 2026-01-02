import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused mathematical constant
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

# Distractor: complex-looking but unused transformation chain
decoy_transform = lambda s: s.upper().replace('A', 'X').swapcase()

# Simulated sensor data with noise masking
raw_signals = [14, 8, 22, 19, 31, 12, 44, 7, 17, 23]
noise_mask = [i % 3 for i in range(len(raw_signals))]
filtered_data = [raw_signals[i] - noise_mask[i] for i in range(len(raw_signals)) if raw_signals[i] > 10]

# Irrelevant string processing using string methods (distractor block)
log_headers = ['ERR', 'INFO', 'DEBUG', 'WARN']
formatted_logs = set(header.ljust(8, '_') for header in log_headers)
status_flag = ''.join(sorted({h[0] for h in log_headers})).lower()  # yields 'deiw'

# Unused bitwise manipulation decoy
twist_value = 0
for item in filtered_data:
    twist_value ^= (item << 2) | (item >> 1)
twist_value = twist_value & 0xFFFF  # Keep within 16 bits

# Real computation begins: analyze only odd-positioned elements after filtering
effective_samples = [filtered_data[i] for i in range(len(filtered_data)) if i % 2 == 0]

# Compute checksum using modular arithmetic and accumulation
current_phase = 0.0
for idx, val in enumerate(effective_samples):
    current_phase += math.sin(val * math.pi / 4) * (idx + 1)

# Distractor: unused set operation with no impact
duplicate_check_set = set(effective_samples)
duplicate_found = len(duplicate_check_set) != len(effective_samples)

# Core pipeline function with embedded logic
pipeline_stages = [
    lambda x: x * 3 + 1,
    lambda x: x ^ 0xFF,  # Bit flip lower byte
    lambda x: sum(int(b) for b in bin(x)[2:]) * ((-1) ** (x % 2)),  # Population count with sign flip on odd
]

# Actual data stream used in final calculation
data_stream = [13, 11, 18]

# Misleading accumulation (not part of result)
phantom_sum = 0
for v in data_stream:
    phantom_sum += pow(v, 2, 100)  # Modulo exponentiation distraction

# Critical processing pipeline
def process_pipeline(stream):
    accumulator = 0
    for num in stream:
        temp = num
        for stage in pipeline_stages:
            temp = stage(temp)
        accumulator += abs(temp)  # Use absolute to ensure positive contribution
    
    # Final transformation involving trigonometric weighting and decimal precision
    angle = math.radians(current_phase * 10)  # Depends on earlier sin-sum
    scaled = accumulator * math.cos(angle)
    return round(scaled, 6)

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output required format
print(f"Result: {final_output}")