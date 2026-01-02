import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_signals = [18, 23, 15, 47, 30, 12, 40]
    offset = 7
    adjusted = [x + offset for x in raw_signals]
    filtered = [x for x in adjusted if x > 25]
    return filtered

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(x):
    return (x * 3) % 19

# Unused transformation chain (red herring)
def transform_sequence(data):
    result = []
    for i, val in enumerate(data):
        temp = val ^ (i + 1)
        temp = (temp * 2) >> 1
        result.append(temp)
    return result

# Signal processing core
def normalize_signal(signal_list):
    total = sum(signal_list)
    norm_factor = 100.0 / total
    return [round(x * norm_factor, 2) for x in signal_list]

# Bit manipulation for checksum (relevant only in part)
def compute_checksum(packets):
    chk = 0
    for p in packets:
        chk ^= p
        chk = (chk << 1) & 0xFF
    return chk | 10  # artificial bias

# Decoy statistical function (never called)
def get_distribution_moment(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(variance ** 0.5, 3)

# Real processing pipeline
sensor_data = collect_sensor_readings()
dummy_pad = [0] * len(sensor_data)
merged_frame = [(a, b) for a, b in zip(sensor_data, dummy_pad)]
flattened = list(itertools.chain.from_iterable(merged_frame))  # includes zeros
nonzero = [x for x in flattened if x != 0]

normalized = normalize_signal(nonzero)

# Construct threshold map using irrelevant logic mix
base_thresholds = {'t1': 15, 't2': 22, 't3': 35}
expanded = {k: v + 5 for k, v in base_thresholds.items()}
expanded['t4'] = expanded['t1'] + expanded['t2']
threshold_map = {key: val * 1.1 for key, val in expanded.items()}

# String-based flag system (irrelevant but plausible)
diagnostic_flags = 'pass,calibrate,verify'
flag_list = diagnostic_flags.split(',')
flag_state = {f: idx for idx, f in enumerate(flag_list)}

# Core analysis function
def analyze_signal(signal, thresholds):
    t_vals = sorted(thresholds.values())
    count_above = sum(1 for s in signal if s > t_vals[1])
    magnitude_score = sum(signal) * 0.1
    
    # Real logic begins here
    stage_one = magnitude_score + count_above
    stage_two = stage_one ** 2
    
    # Use bit trick to encode stability
    stable = True
    for i in range(1, len(signal)):
        if abs(signal[i] - signal[i-1]) > 12.0:
            stable = False
    
    stability_bonus = 5 if stable else 0
    intermediate = int(stage_two) + stability_bonus
    
    # Checksum of indices above threshold (real contribution)
    high_indices = [i for i, s in enumerate(signal) if s > t_vals[2]]
    chk = 0
    for idx in high_indices:
        chk ^= idx
        chk = (chk * 3) % 23
    
    final_score = intermediate - chk
    return int(final_score)

# Execute main logic
processed_data = normalized
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Output target result
print(f"Result: {final_diagnostic}")