import itertools

# Simulated sensor array data with noise and redundant measurements
data_stream = [18, 22, 15, 30, 12, 25, 14, 20, 17, 23, 19, 27]

# Irrelevant environmental constants (distractors)
atmospheric_pressure = 1013.25
humidity_index = 45
ambient_noise_level = 78

# Preprocessing: filter anomalies using a sliding window (red herring function)
def detect_anomalies(sequence, window_size=3):
    anomalies = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        if abs(window[0] - sum(window) / window_size) > 5:
            anomalies.append((i, window[0]))
    return anomalies

# False usage path: collected but not used later (dead code path)
anomaly_list = detect_anomalies(data_stream)

# Core signal processing chain
baseline_offset = 10
adjusted_readings = [x - baseline_offset for x in data_stream if x > 14]  # list comprehension

# Bit manipulation decoy: looks important but unused
bit_encoded = 0
for val in adjusted_readings:
    bit_encoded ^= (val << 2) | (val >> 1)

# Secondary filtering based on parity (distraction)
even_filtered = list(filter(lambda x: x % 2 == 0, adjusted_readings))
odd_contribution = sum([x for x in adjusted_readings if x % 2 == 1])  # partial use

# Control flow with nested conditions (3 levels deep)
aggregate_result = 0
for reading in adjusted_readings:
    if reading > 15:
        if reading in even_filtered:
            aggregate_result += reading * 2
        else:
            temp_val = reading + odd_contribution % 4
            if temp_val > 20:
                aggregate_result += temp_val
    else:
        # Unused branch with misleading logic
        backup_flag = True
        for i in range(2):
            for j in range(3):
                backup_flag = not backup_flag

# Decoy statistical calculation (irrelevant)
mean_value = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_value) ** 2 for x in data_stream) / len(data_stream)

# Key threshold derived from bitwise analysis (misleading comment)
threshold = len(even_filtered) ^ odd_contribution & 7  # uses XOR and AND

# Critical statement: target execution point
filtration_score = aggregate_result // (threshold + 1)

# Red herring: tuple unpacking with irrelevant diagnostics
diagnostic_codes = ['OK', 'CALIBRATE', 'CHECK_SENSOR']
status, _, _ = diagnostic_codes if filtration_score > 50 else ['ERROR', 'REBOOT', 'UPDATE']

# Output the required result
print(f"Result: {filtration_score}")