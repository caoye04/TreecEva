from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing pipeline with diagnostic evaluation
raw_signals = [0.45, 0.72, 0.13, 0.89, 0.67, 0.34, 0.91, 0.56]
noise_floor = 0.25
amplification_factor = 3.1
calibration_offset = -0.05

# Irrelevant calibration constants (distractors)
system_gain = 1.08
baseline_drift = 0.003
reference_voltage = 3.3
resolution_bits = 12
max_theoretical_value = 2 ** resolution_bits - 1  # Unused in logic

# Signal preprocessing
filtered_data = [x for x in raw_signals if x > noise_floor]
amplified_data = [x * amplification_factor for x in filtered_data]
compensated_data = [x + calibration_offset for x in amplified_data]
rounded_data = [round(x, 2) for x in compensated_data]

# Data bucketing (meaningful but indirect)
data_bins = defaultdict(int)
for val in rounded_data:
    bin_key = int(val // 0.5)
    data_bins[bin_key] += 1

# Decoy analysis function (never called)
def deprecated_diagnostic(signal_list):
    return sum(x ** 0.5 for x in signal_list if x > 0.5)

# Another decoy: complex but unused transformation
fft_approximation = [sum(rounded_data[i::4]) for i in range(4)]
bit_reversed = [int(bin(int(x * 100))[2:][::-1], 2) for x in rounded_data]

# Threshold configuration map (used later)
threshold_map = {}
for i, val in enumerate([0.5, 0.75, 1.0, 1.5]):
    label = ['low', 'medium', 'high', 'critical'][i]
    threshold_map[label] = val + (0.1 if i % 2 == 0 else -0.05)

# Simulated device states (mostly irrelevant)
device_status_codes = {1: 'active', 2: 'idle', 3: 'sleep', 4: 'fault'}
operational_mode = device_status_codes[1]
temperature_log = [23.5, 24.1, 23.8, 25.0, 24.5]

# Construct processed_data using itertools and filtering
paired_stream = list(itertools.combinations(rounded_data, 2))
strong_pairs = [pair for pair in paired_stream if sum(pair) > 2.0]
aggregated_features = []
for a, b in strong_pairs:
    feature = (a * 0.6) + (b * 0.4)
    if feature > threshold_map['medium']:
        aggregated_features.append(feature)

processed_data = [round(x, 2) for x in aggregated_features]

# Auxiliary statistical distraction
value_counter = Counter()
for val in processed_data:
    category = 'A' if val < 1.0 else 'B' if val < 2.0 else 'C'
    value_counter[category] += 1

# Real-time monitoring decoy (unused)
current_alert_level = 'green'
historical_averages = [sum(processed_data)/len(processed_data)]
for window in range(1, len(processed_data)):
    avg = sum(processed_data[:window+1]) / (window+1)
    historical_averages.append(round(avg, 3))

# Core diagnostic logic
status_flags = []
for val in processed_data:
    if val >= threshold_map['critical']:
        status_flags.append(3)
    elif val >= threshold_map['high']:
        status_flags.append(2)
    elif val >= threshold_map['medium']:
        status_flags.append(1)
    else:
        status_flags.append(0)

flag_distribution = Counter(status_flags)

# Final analysis function
def analyze_signal(data, thresholds):
    base_score = sum(1 for x in data if x > thresholds['low'])
    penalty = 0
    
    # Complex conditional logic chain (4 levels deep at points)
    if len(data) > 3:
        penalty += 1
        if flag_distribution[1] > 0:
            if flag_distribution[2] == 0 and flag_distribution[3] == 0:
                penalty += 2
            elif flag_distribution[2] > flag_distribution[1]:
                bonus_factor = 0.5
                if data[-1] > data[0]:
                    bonus_factor *= 1.5
                base_score += int(bonus_factor)
        else:
            max_val = max(data)
            if max_val > thresholds['high']:
                secondary_check = any(x > thresholds['medium'] for x in data[:len(data)//2])
                if not secondary_check:
                    penalty += 3
    else:
        if flag_distribution[3] > 0:
            emergency_response_code = 911  # Red herring
            penalty += flag_distribution[3] * 2

    # Additional interference: bit manipulation on float indices (seemingly complex but controlled)
    index_xor = 0
    for i, val in enumerate(data):
        shifted = i << 1
        masked = shifted & 7
        index_xor ^= masked

    final_score = base_score * 100 - penalty * 10 + (index_xor * 5)
    
    # One last distraction: unused recursive helper
    def _recursive_weight(acc, depth):
        if depth <= 0:
            return acc
        return _recursive_weight(acc + (acc % depth), depth - 1)
    
    return final_score

# Execute main logic
diagnostic_trace = []  # Logged but unused
final_diagnostic = analyze_signal(processed_data, threshold_map)

diagnostic_trace.append(final_diagnostic)

# Print result as required
print(f"Target result: {final_diagnostic}")