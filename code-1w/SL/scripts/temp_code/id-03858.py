import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_sensor(stream, bias):
    adjusted = []
    for val in stream:
        if val < 0:
            val = abs(val) + bias
        normalized = round((val / 1024.0) * 5.0, 4)
        adjusted.append(normalized)
    return adjusted

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(x):
    return (x * 0.987) + 2.1 if x > 1.5 else x

# Signal transformation using frequency-weighted envelope
def envelope_detect(signal, weights):
    result = []
    for i, sample in enumerate(signal):
        contribution = 0
        for j, w in enumerate(weights):
            if i + j < len(signal):
                contribution += signal[i + j] * w
        result.append(round(contribution, 5))
    return result[:len(signal)]

# Frequency band classification (red herring: not actually used in final logic)
def classify_band(energy):
    bands = {'low': 0.5, 'mid': 1.2, 'high': 2.0}
    if energy < bands['low']:
        return 'L'
    elif energy < bands['mid']:
        return 'M'
    else:
        return 'H'

# Core analysis function with conditional recursion
def analyze_signal(data, thresholds, depth=0):
    if depth >= 3:  # Limit recursion depth (real control flow)
        return sum(data) * thresholds['base']

    temp_result = 0
    flag_state = False

    for idx, reading in enumerate(data):
        key = f"t{idx % len(thresholds)}"
        thresh = thresholds[key] if key in thresholds else thresholds['default']

        # Conditional bit manipulation based on parity and threshold
        if reading > thresh:
            shifted = int((reading * 100)) >> 2
            flipped = shifted ^ 0xFF  # Bitwise XOR red herring
            temp_result += math.sin(flipped * 0.01)  # Unused complex calc
            flag_state = True
        elif reading == thresh:
            temp_result += len([x for x in data if x >= thresh]) * 0.1
        else:
            temp_result -= math.log(thresh + 1) * 0.05

    # Recursive refinement branch (actually contributes)
    if flag_state and depth < 2:
        inverted_data = [max(0, 2.5 - x) for x in data]
        recursive_contribution = analyze_signal(inverted_data, thresholds, depth + 1)
        temp_result += recursive_contribution * 0.3

    return round(temp_result, 5)

# Misleading auxiliary computation (distractor)
def compute_entropy(seq):
    from collections import Counter
    freq = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in freq.values():\n        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Real execution begins here
raw_stream = [128, 256, -512, 768, 1024, 300, 450]
bias_correction = 0.3
processed_data = preprocess_sensor(raw_stream, bias_correction)

# Apply envelope detection with dummy weights (partially relevant)
weights = [0.25, 0.5, 0.75, 1.0]
envelope_signal = envelope_detect(processed_data, weights)

# Build threshold map using dictionary and string operations (key setup)
threshold_keys = ['t0', 't1', 't2', 'default', 'base']
dynamic_names = [k.upper() + '_VAL' for k in threshold_keys]
threshold_map = {}
for i, key in enumerate(threshold_keys):
    base_val = 1.25 + (i * 0.15)
    if 't' in key:
        threshold_map[key] = round(base_val + math.cos(i), 4)
    else:
        threshold_map[key] = round(base_val, 4)

# Dead code involving zip and enumerate (distractor)
indexed_pairs = list(enumerate(zip(processed_data, envelope_signal)))
summary_stats = {}
for index, (orig, env) in indexed_pairs:
    status_flag = 'OK' if orig >= env else 'LOW'
    summary_stats[index] = f'{status_flag}:{orig:.3f}'

# Unused set operation (distractor)
unique_orig = set(round(x, 3) for x in processed_data)
unique_env = set(round(x, 3) for x in envelope_signal)
common_values = unique_orig & unique_env

# String-based validation check (irrelevant but plausible)
data_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
label_suffix = ''.join([s[-1] for s in data_ids])
validation_code = f'DIAG_{label_suffix}_END'
if validation_code.find('X') != -1:
    raise RuntimeError('Invalid labels')

# Actual critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print final result as required
print(f"Result: {final_diagnostic}")