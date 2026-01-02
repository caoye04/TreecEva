def process_readings(readings):
    processed = []
    for i, val in enumerate(readings):
        if i % 3 == 0:
            processed.append(val * 1.05)
        elif i % 3 == 1:
            processed.append(val * 0.98)
        else:
            processed.append(val + 2.1)
    return [round(p, 2) for p in processed]

# Irrelevant sensor calibration data (distractor)
calibration_keys = ['kA', 'kB', 'kC']
base_offsets = {k: idx * 0.03 for idx, k in enumerate(calibration_keys)}

# Simulate turbine sensor array
turbine_ids = ['TURB-01', 'TURB-02', 'TURB-03', 'TURB-04']
raw_sensor_data = {
    tid: [120 + idx*4, 135 - idx*2, 142 + idx, 118 + idx*3, 130 - idx] 
    for idx, tid in enumerate(turbine_ids)
}

# Misleading intermediate transformation (dead path)
def compute_efficiency_curve(data):
    return sum(d * 0.87 for d in data if d > 125)

# Unused recursive helper (red herring)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Real processing begins here
turbine_data = {}
for tid, readings in raw_sensor_data.items():
    filtered = [r for r in readings if r >= 120]
    adjusted = process_readings(filtered)
    # Decoy aggregation
    avg_val = sum(adjusted) / len(adjusted) if adjusted else 0
    turbine_data[tid] = {
        'readings': adjusted,
        'baseline': avg_val,
        'status_flag': sum(int(r // 10) for r in adjusted) % 4
    }

# Threshold logic with bit manipulation distraction
flag_mask = 0b11
shifted_mask = flag_mask << 2  # unused

threshold_map = {}
for i, tid in enumerate(turbine_ids):
    base_th = 128.5 + (i % 2) * 7.3
    # Complex but irrelevant rounding pattern
    decoy_round = round(base_th + factorial(3) * 0.01, 1)
    threshold_map[tid] = base_th  # only this matters

# Another red herring: zip with no effect
sync_labels = list(zip(turbine_ids, calibration_keys[:len(turbine_ids)]))
deep_checksum = sum(len(label[0]) ^ len(label[1]) for label in sync_labels)  # unused

# Core logic hidden among distractions
def aggregate_metrics(data_dict, thresholds):
    diagnostics = []
    for tid, info in data_dict.items():
        thresh = thresholds[tid]
        above_count = sum(1 for r in info['readings'] if r > thresh)
        below_count = len(info['readings']) - above_count
        # Critical bitwise operation influencing result
        flag = info['status_flag']
        if flag & 0b01:  # checks least significant bit
            above_count = above_count ^ 3  # XOR twist
        if flag & 0b10:
            above_count += 1
        # Real computation buried here
        score = above_count * 100 - below_count * 10
        diagnostics.append(score)
    
    # Distracting enumeration and transformation
    indexed_scores = {i: score for i, score in enumerate(diagnostics)}
    weights = [0.9, 1.1, 1.0, 0.95]
    weighted = [indexed_scores[i] * w for i, w in enumerate(weights)]
    
    # Final answer determined here despite noise
    total = int(sum(weighted) // 1)  # integer division
    adjustment = len(threshold_map.keys()) & 3  # bitwise adjustment
    return total - adjustment * 25

# Execution point of interest
final_diagnostic = aggregate_metrics(turbine_data, threshold_map)
print(f"Target result: {final_diagnostic}")