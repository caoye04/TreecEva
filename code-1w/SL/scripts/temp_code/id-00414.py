import itertools

# Sensor simulation and analysis system for environmental monitoring

# Raw sensor inputs (simulated)
sensor_a = [12, 15, 10, 18, 22, 8, 14]
sensor_b = [9, 16, 13, 11, 19, 7, 17]

# Irrelevant auxiliary data (distractor)
baseline_offsets = [0.5, 0.3, 0.7, 0.2, 0.4]
noise_floor = 3.1
temp_cache = {i: sensor_a[i] * 0.9 for i in range(len(sensor_a))}

# Preprocessing: normalize and combine sensor streams
normalized_a = [x * 0.95 for x in sensor_a]
normalized_b = [x * 1.05 for x in sensor_b]
combined_readings = [a + b for a, b in zip(normalized_a, normalized_b)]

# Misleading intermediate calculation (dead path - never used)
avg_normalized = sum(normalized_a + normalized_b) / len(normalized_a + normalized_b)
spike_count = 0
for val in combined_readings:
    if val > 25:
        spike_count += 1

# Real processing begins here
filtered_readings = [r for r in combined_readings if r > 10]
sorted_readings = sorted(filtered_readings, reverse=True)

def apply_digital_filter(data, factor=0.8):
    """Simple IIR-like filter (relevant function)"""
    result = []
    accumulator = data[0]
    result.append(accumulator)
    for i in range(1, len(data)):
        accumulator = accumulator * factor + data[i] * (1 - factor)
        result.append(accumulator)
    return result

# Apply filter to reduce noise (key transformation)
filtered_signal = apply_digital_filter(sorted_readings)

# Windowed analysis using itertools (required feature)
windowed_pairs = list(itertools.pairwise(filtered_signal))
correlation_trend = 0
for x, y in windowed_pairs:
    correlation_trend += (y - x) * 0.5

# Secondary irrelevant computation (distractor)
string_metadata = "SNSR-A,B;LOC=FIELD_4;VER=2.1"
segment_count = len(string_metadata.split(';'))
valid_chars = sum(1 for c in string_metadata if c.isalnum())

# Threshold logic and state tracking
high_activity_threshold = 14.5
activation_log = []
state_flags = []

for val in filtered_signal:
    is_active = val > high_activity_threshold
    activation_log.append(is_active)
    # Generate multi-condition flag (compound boolean logic)
    flag = (val > 12.0) and (is_active or (val * 0.75) > 10.0)
    state_flags.append(int(flag))

# Compute duty cycle from state flags (relevant)
duty_cycle = sum(state_flags) / len(state_flags) if state_flags else 0

# Additional red herring: frequency domain distraction
fft_approximation = [abs(x - y) for x, y in itertools.pairwise(filtered_signal)]
peak_frequency_estimate = len([diff for diff in fft_approximation if diff < 0.6])

# Core diagnostic algorithm
processed_data = {
    'amplitude': filtered_signal[0] if filtered_signal else 0,
    'stability': abs(correlation_trend),
    'consistency': duty_cycle,
    'length': len(filtered_signal)
}

threshold = 0.65

# Decision engine with composite logic
def evaluate_stability(stability_val, base_threshold):
    if stability_val < base_threshold * 0.5:
        return 3
    elif stability_val < base_threshold:
        return 2
    else:
        return 1

def analyze_readings(data, threshold):
    # Multi-factor diagnostic score
    amp_score = 1 if data['amplitude'] > 20 else 0
    stab_factor = evaluate_stability(data['stability'], threshold)
    consistency_weight = data['consistency'] * 2
    
    # Composite formula with logical weighting
    score = (amp_score * 4) + (stab_factor * 3) + (int(consistency_weight) * 2)
    
    # Red herring: unused branch based on length (dead code path)
    adjustment = 0
    if data['length'] > 10:
        adjustment = 5  # Never reached due to data size
    elif data['length'] > 5:
        adjustment = 2  # This will trigger
    else:
        adjustment = 0
    
    # Final adjustment uses only part of computed data
    final_score = score + 1  # Fixed bias
    return final_score

# Execute critical statement
target_intermediate = analyze_readings(processed_data, 0.5)  # Distractor call
final_diagnostic = analyze_readings(processed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")