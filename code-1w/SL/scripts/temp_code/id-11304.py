from collections import defaultdict, Counter

# Simulated sensor data stream (irrelevant in part)
sensor_readings = [14, 28, 14, 56, 7, 84, 14, 21, 98, 14]
reading_frequencies = Counter(sensor_readings)
spurious_reading_count = sum(count for val, count in reading_frequencies.items() if val % 7 == 0 and val > 30)

# System mode configuration
current_mode = 'diagnostic'
threshold_map = defaultdict(lambda: 10, {'normal': 25, 'diagnostic': 5})
activation_threshold = threshold_map[current_mode]

# Primary signal processing chain
raw_signals = [x * 2 + 1 for x in range(9)]  # generates odd numbers 1 to 17
filtered_signals = [sig for sig in raw_signals if sig % 3 != 0]  # remove multiples of 3
transformed_signals = []
for s in filtered_signals:
    if s < 10:
        transformed_signals.append(s ** 2)
    else:
        transformed_signals.append(s + 5)

# Secondary decoy processing path (dead code - never used)
decoy_accumulator = 0
temp_buffer = []
for x in range(6):
    temp_buffer.append(x * x + 3)
    if x % 2 == 0:
        decoy_accumulator += x ** 3
decoy_result = sum(temp_buffer) / (len(temp_buffer) or 1)

# Conditional logic with nested dependencies
signal_magnitude = sum(transformed_signals)
noise_floor = 120
system_engaged = (signal_magnitude > noise_floor) and (len(filtered_signals) >= 5)

# Red herring calculation (looks important but unused)
baseline_correction = 0.0
if spurious_reading_count > 3:
    baseline_correction = 0.75
elif activation_threshold < 15:
    baseline_correction = 0.9
else:
    baseline_correction = 1.1

# Core computation with distractors
aggregate_score = 0
for idx, val in enumerate(transformed_signals):
    if idx % 2 == 0:
        aggregate_score += val // 2
    else:
        aggregate_score -= -(-val // 3)  # ceiling division via double negation

# Misleading intermediate (appears critical but isn't final)
interim_diagnostic = aggregate_score * 1.05 if system_engaged else -1

# Key statement: this is where the answer comes from
correction_factor = 1.25
final_diagnostic = aggregate_score * correction_factor if system_engaged else 0

print(f"Result: {final_diagnostic}")