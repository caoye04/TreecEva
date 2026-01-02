from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (1001, 4.5), (1002, 5.2), (1003, 3.8), (1004, 6.1), (1005, 4.4),
    (1006, 5.0), (1007, 4.9), (1008, 7.2), (1009, 4.6), (1010, 5.3)
]

# Mapping of error codes to diagnostic messages
error_log = defaultdict(str)
error_log[1] = "Sensor drift detected"
error_log[2] = "Calibration required"
error_log[3] = "Signal interference"

# Parameters for analysis
base_threshold = 4.7
adjustment_factor = 0.3
threshold = base_threshold + adjustment_factor

# Filter readings above dynamic threshold
filtered_data = []
spike_count = 0
for ts, val in timestamped_readings:
    if val > threshold:
        filtered_data.append((ts, val))
        spike_count += 1

# Misleading computation: analyzing temporal gaps (not used in final result)
temporal_gaps = []
for i in range(1, len(timestamped_readings)):
    gap = timestamped_readings[i][0] - timestamped_readings[i-1][0]
    temporal_gaps.append(gap)

average_gap = sum(temporal_gaps) / len(temporal_gaps) if temporal_gaps else 0

# Helper function to simulate diagnostic processing
def compute_entropy(values):
    from math import log2
    if not values:
        return 0.0
    total = sum(values)
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log2(prob)
    return round(entropy, 4)

# Another red herring: character pattern in dummy ID
device_id = "SEN-TRX-7F21"
hex_digits = ''.join([c for c in device_id if c in '0123456789abcdefABCDEF'])
checksum = 0
for c in hex_digits:
    if c.lower() == 'f':
        checksum += 15
    elif c.isdigit():
        checksum += int(c)

# Core logic: process only the filtered data
reading_values = [val for ts, val in filtered_data]

# Compute weighted score using bitwise manipulation for obfuscation
weight = len(reading_values) << 1  # Multiply by 2 using left shift
summed = sum(reading_values)
adjusted_sum = summed + (spike_count ^ 3)  # XOR with constant (distraction)

# Final diagnostic is based on conditional logic and arithmetic
if len(reading_values) >= 3:
    base_score = adjusted_sum * weight
    penalty = 10 if spike_count > 4 else 5
    final_diagnostic = int(base_score / 10) - penalty
else:
    final_diagnostic = compute_entropy(reading_values) * 100

# Print result as required
print(f"Result: {final_diagnostic}")