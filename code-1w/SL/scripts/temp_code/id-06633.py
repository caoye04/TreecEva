from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings and complex logic
raw_readings = [14, 19, 24, 17, 22, 31, 13, 8, 36, 42]
baseline_shift = 15
calibration_factor = 0.85

# Irrelevant statistical buffer (distractor)
deviation_pool = []
for val in raw_readings:
    deviation_pool.append((val - sum(raw_readings)/len(raw_readings)) ** 2)

# Misleading transformation chain (dead path)
shadow_copy = [x * calibration_factor for x in raw_readings if x > 20]
shadow_copy = [math.floor(x) for x in shadow_copy]
shadow_stats = sum(shadow_copy) / len(shadow_copy) if shadow_copy else 0

# Real processing begins: filtering anomalies
filtered_stream = [x for x in raw_readings if x >= baseline_shift]

# Bit manipulation decoy (irrelevant but plausible)
bitmask = 0b1101
masked_values = [v ^ bitmask for v in raw_readings]
parity_check = sum(1 for mv in masked_values if bin(mv).count('1') % 2 == 0)

# Control flow distraction: nested conditionals with unused branches
mode_flag = 'enhanced'
if len(filtered_stream) > 5:
    adjustment = 2
    if mode_flag == 'legacy':
        adjustment = -1
    else:
        temp_cache = defaultdict(int)
        for i in range(len(filtered_stream)):
            temp_cache[i] = filtered_stream[i] % 7
        # Unused cache (distractor)
else:
    adjustment = 0

# Core computation disguised among noise
offset_buffer = [abs(x - baseline_shift) for x in filtered_stream]
scale_factor = len(offset_buffer) if offset_buffer else 1
aggregate_score = sum(offset_buffer) * scale_factor // max(offset_buffer) if offset_buffer else 0

# Decoy function (never called in critical path)
def legacy_normalizer(data):
    return [d * 0.95 for d in sorted(data, reverse=True)]

# Real auxiliary function with subtle relevance
def anomaly_detector(seq):
    if not seq:
        return 0
    freq_map = Counter(seq)
    mode_count = freq_map.most_common(1)[0][1]
    if mode_count > 2:
        return int(math.sqrt(mode_count * len(seq)))
    else:
        return sum(1 for x in seq if x % 2 == 1) - 1

# Secondary red herring: unused recursive structure
def predict_next(arr, depth=2):
    if depth == 0 or len(arr) < 2:
        return arr[-1] if arr else 0
    diff_seq = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    return arr[-1] + predict_next(diff_seq, depth-1)

# Critical statement embedded in distracting context
intermediate_fusion = aggregate_score ^ parity_check
buffer_snapshot = offset_buffer.copy()
anomaly_seed = anomaly_detector(offset_buffer)
final_diagnostic = aggregate_score + anomaly_detector(offset_buffer)

print(f"Result: {final_diagnostic}")