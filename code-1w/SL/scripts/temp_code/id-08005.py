from itertools import combinations

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 43]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017]

# Irrelevant transformation - distractor
decoy_transform = [x ** 0.5 for x in pressure_readings if x > 1010]

# Misleading intermediate calculation with no real impact
temp_variance_proxy = sum([(t - 24.0) ** 2 for t in temperature_readings]) / len(temperature_readings)

# Dummy recursive function to confuse path tracing
def useless_binary_sum(n):
    if n <= 1:
        return n
    return n + useless_binary_sum(n // 2)

# Unused but plausible-looking analysis
correlation_clue = [(t, h) for t, h in zip(temperature_readings, humidity_readings) if t > 24.0]

# Real processing begins here: find anomalous patterns
anomaly_flags = []
for i, (t, h, p) in enumerate(zip(temperature_readings, humidity_readings, pressure_readings)):
    if (t > 25.0 or t < 23.0) and abs(p - 1014) > 2:
        anomaly_flags.append(i)

# Compute rolling average of humidity (distraction)
rolling_humidity_avg = []
window_size = 3
for i in range(len(humidity_readings) - window_size + 1):
    rolling_humidity_avg.append(sum(humidity_readings[i:i+window_size]) / window_size)

# Fake classification model (dead code path)
def classify_anomaly(seq):
    bit_pattern = 0
    for val in seq:
        bit_pattern ^= int(val) & 7
    return bit_pattern % 3

# Actual signal extraction via bitwise fingerprinting
valid_indices = [i for i in range(len(temperature_readings)) if i not in anomaly_flags]
combined_fingerprint = 0
for idx in valid_indices:
    temp_bit = int(temperature_readings[idx] * 10) & 15
    hum_bit = humidity_readings[idx] & 15
    combined_fingerprint ^= (temp_bit ^ hum_bit) << (idx % 4)

# Secondary filter: only use every other valid index
filtered_values = [temperature_readings[i] for i in valid_indices[::2]]

# Core computation disguised among distractions
def compute_aggregate(data, fp, weights=None):
    if weights is None:
        weights = [0.5 + (i % 3) * 0.25 for i in range(len(data))]
    
    # Weighted sum with fingerprint modulation
    base_sum = sum(d * w for d, w in zip(data, weights))
    modulator = (fp >> 2) & 63  # Extract bits 2-7
    adjustment = (modulator - 32) * 0.75  # Center around zero
    
    # Red herring: unused branch with complex logic
    if modulator > 50:
        for _ in range(3):
            adjustment = adjustment ** 0.9  # Diminishing returns
    
    return round(base_sum + adjustment, 6)

# Decoy call with incorrect parameters (never executed)
# result_pretend = compute_aggregate(humidity_readings, 123, [0.1]*7)

# Key statement
final_score = compute_aggregate(filtered_values, combined_fingerprint)

print(f"Result: {final_score}")