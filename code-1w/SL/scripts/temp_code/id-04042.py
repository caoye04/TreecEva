import math

# Simulated sensor array data (irrelevant initial setup)
sensor_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
base_frequency = 50.0
harmonics = [base_frequency * i for i in range(1, 6)]

# Irrelevant signal generation (distractor)
sine_waves = []
for h in harmonics:
    wave = []
    for t in range(0, 10):
        wave.append(round(math.sin(2 * math.pi * h * t / 100), 3))
    sine_waves.append(wave)

# Real data input (hidden among distractions)
raw_readings = [380, 250, 120, 410, 95, 500, 305, 199, 476, 104]

# Decoy transformation (dead path)
def transform_log_scale(data):
    return [round(math.log(x), 2) for x in data if x > 0]

unused_result = transform_log_scale(raw_readings)  # Not used later

# Signal filtering logic (core path)
def filter_anomalies(values, limit=450):
    return [v for v in values if v <= limit]

filtered_data = filter_anomalies(raw_readings)  # Removes 500

# Bit manipulation layer (misleading complexity)
def scramble_index(idx, size):
    shifted = (idx << 1) % size
    return (shifted ^ 3) % size

reorder_map = [scramble_index(i, len(filtered_data)) for i in range(len(filtered_data))]
# Note: reorder_map is computed but not actually used

# Threshold logic with red herring conditional
baseline = sum(filtered_data) / len(filtered_data)
threshold = baseline * 0.75

# Another decoy function (never called)
def detect_spike(sequence, amp_threshold):
    return any(abs(seq - baseline) > amp_threshold for seq in sequence)

# Core processing with list comprehension and set operation (actual logic)
def process_signals(data, thresh):
    above_thresh = [x for x in data if x > thresh]
    duplicates = len(data) - len(set(data))  # Check for repeated readings
    
    # Secondary filter: only odd-indexed elements in original filtered_data
    indexed_values = [(i, val) for i, val in enumerate(data)]
    odd_indexed = [val for i, val in indexed_values if i % 2 == 1]
    
    # Final computation: product of count adjustments
    adjustment_factor = abs(len(above_thresh) - duplicates)
    secondary_score = len(odd_indexed) + int(thresh // 100)
    
    # Critical calculation
    result = (adjustment_factor * secondary_score) + 17
    return result

# Unused control flow block (distraction)
if len(raw_readings) > 8:
    temp_state = [x * 1.05 for x in raw_readings]
    normalized = [min(x, 500) for x in temp_state]
    final_output = sum(normalized) // 10  # Looks important but unused

# Actual execution point
final_output = process_signals(filtered_data, threshold)

# Output
print(f"Result: {final_output}")