from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_packet = [
    {'id': 'A7', 'readings': [1.2, 0.9, 1.5, 2.1, 1.8], 'status': 'active', 'calib': 0.98},
    {'id': 'B3', 'readings': [0.1, 0.05, 0.0], 'status': 'idle', 'calib': 1.02},
    {'id': 'C9', 'readings': [3.0, 3.1, 2.9, 3.0], 'status': 'active', 'calib': 0.99}
]

# Irrelevant helper that looks important but unused in critical path
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Decoy function that computes something plausible but unused
def compute_entropy(readings):
    counts = Counter([round(x, 1) for x in readings])
    total = len(readings)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

# Auxiliary transformation not directly contributing to final result
def normalize_readings(readings, base=1.0):
    factor = base / sum(readings) if sum(readings) != 0 else 1.0
    return [r * factor for r in readings]

# Misleading aggregation that seems central but is a red herring
total_diagnostics = defaultdict(float)
for entry in data_packet:
    raw_sum = sum(entry['readings'])
    calibrated_sum = raw_sum * entry['calib']
    total_diagnostics[entry['id']] = round(calibrated_sum, 3)

# Another distraction: string-based status encoding that goes nowhere
status_flags = ''
for entry in data_packet:
    flag_char = entry['status'][0].upper()
    status_flags += flag_char
status_flags = status_flags[::-1]  # reverse it for no reason

# Real preprocessing begins here — only now we extract active sensors
active_readings = []
for entry in data_packet:
    if entry['status'] == 'active':
        # Apply actual needed calibration
        calibrated = [r * entry['calib'] for r in entry['readings']]
        active_readings.extend(calibrated)

# Now process: filter out any reading below threshold
filtered_readings = [x for x in active_readings if x > 0.5]

# Compute moving average over 2-point window (relevant processing)
moving_averages = []
for i in range(len(filtered_readings) - 1):
    avg_val = (filtered_readings[i] + filtered_readings[i+1]) / 2
    moving_averages.append(avg_val)

# Extract peaks: values above 1.5 after averaging
peaks = [p for p in moving_averages if p > 1.5]

# Perform bit manipulation on length of peaks (unexpected but key)
peak_count = len(peaks)
shifted = (peak_count << 3)  # multiply by 8
masked = shifted & 0xFF  # ensure within byte range

# Secondary metric: aggregate variance from mean of filtered readings
def compute_variance(data):
    if len(data) == 0:
        return 0.0
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean)**2 for x in data]
    return sum(squared_diffs) / len(data)

variance_metric = compute_variance(filtered_readings)
scaled_variance = int(variance_metric * 100)

# Combine two metrics: masked peak info and scaled variance
combined_key = masked ^ scaled_variance  # XOR as fusion

# String operation distractor: encode combined_key in hex and shuffle
key_hex = hex(combined_key)[2:].zfill(4)
shuffled_hex = ''.join([key_hex[i] for i in [2,3,0,1]])

# Now real analysis function — used at the end
def analyze_signal(signal_data):
    # Actual logic: count how many original active readings are near integer
    near_integer = 0
    for val in signal_data:
        if abs(val - round(val)) < 0.05:  # very close to whole number
            near_integer += 1
    # Transform via bitwise and arithmetic
    temp = (near_integer * 17) & 0xFFFF
    # Add checksum of first three filtered values (if exist)
    checksum = 0
    for i in range(min(3, len(filtered_readings))):
        checksum += int(filtered_readings[i] * 10)  # scale before int
    temp += checksum
    return temp

# Critical assignment point
processed_data = filtered_readings
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")