import math

# Simulated sensor data with noise and redundant channels
data_stream = [127, 83, 150, 92, 204, 67, 181, 95, 133, 110, 167, 72, 144, 88, 176, 64]

# Irrelevant transformation: frequency domain mock (dead-end computation)
freq_weights = [math.sin(i * 0.5) * 10 for i in range(len(data_stream))]
transformed = [data_stream[i] * freq_weights[i] for i in range(len(data_stream))]
aggregate_power = sum(abs(w) for w in transformed) / len(transformed)

# Decoy function: looks important but unused
def analyze_pattern(seq):
    return sum(seq[i] ^ seq[-i-1] for i in range(len(seq)//2))

# Noise filter threshold (unused red herring)
threshold = 75
filtered_data = [x for x in data_stream if x > threshold]  # Only distractor usage

# Real processing begins: extract every 4th reading (control signal)
signal_samples = data_stream[::4]  # Picks indices 0, 4, 8, 12 -> [127, 204, 133, 144]

# Misleading checksum calculation (not used in final result)
checksum = 0
for val in signal_samples:
    checksum ^= (val << 2) | (val >> 6)

# Apply non-linear correction using logarithmic scaling
corrected = [math.log(x) * 2.1 for x in signal_samples]  # [log(127)*2.1, ...]

# Compute rolling window averages (3-element) - one result is irrelevant
averages = []
for i in range(len(corrected) - 2):
    avg = sum(corrected[i:i+3]) / 3
    averages.append(round(avg, 3))

# Secondary decoy: set-based anomaly detection (never called)
anomaly_pool = set(signal_samples)
reference_set = {100, 120, 133, 144, 150, 200}
detected_anomalies = anomaly_pool.symmetric_difference(reference_set)

# Extract middle two corrected values and apply bitwise weighting
subset = corrected[1:3]  # [log(204)*2.1, log(133)*2.1]
weighted_bits = 0
for val in subset:
    int_part = int(val)
    weighted_bits += (int_part & 0xFF) ^ (int_part >> 4)  # Bit manipulation red herring

# Actual logic: use first and last of corrected with min/max normalization
norm_base = max(corrected) - min(corrected)
if norm_base != 0:
    normalized = [(x - min(corrected)) / norm_base for x in corrected]
else:
    normalized = corrected

# Trim to first and last elements only
trimmed_norm = [normalized[0], normalized[-1]]

# Calculate composite metric: geometric mean + offset
if trimmed_norm[0] > 0 and trimmed_norm[1] > 0:
    geo_mean = math.sqrt(trimmed_norm[0] * trimmed_norm[1])
else:
    geo_mean = 0

offset = len([x for x in data_stream if x % 2 == 0]) * 0.01  # 8 even numbers => 0.08
composite_metric = geo_mean + offset

# Final scoring function (appears complex but deterministic)
def calculate_final_score(metric):
    # Dummy shadow variables
    scale_factor = 17.3
    bias_correction = -2.1
    temp_buffer = [metric * 2, metric * 3, metric + 1.5]
    
    # Multi-step transformation
    stage1 = metric ** 2
    stage2 = stage1 * 1.4
    stage3 = stage2 + bias_correction
    stage4 = abs(stage3) ** 0.5
    
    # Conditional adjustment based on parity of initial data length
    if len(data_stream) % 2 == 0:
        stage4 *= 1.1
    
    # Apply final mapping via artificial lookup
    lookup_seed = int(stage4 * 10) % 4
    adjustments = [0.95, 1.02, 0.98, 1.05]
    result = stage4 * adjustments[lookup_seed]
    
    # Distractor: update buffer with irrelevant logic
    for i in range(len(temp_buffer)):
        temp_buffer[i] += math.sin(result) * i
    
    return round(result, 6)

# Intermediate variable before final assignment
processed_data = composite_metric

# Key execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")