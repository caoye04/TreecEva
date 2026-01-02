from collections import defaultdict
import math

# Simulated sensor fusion system for environmental monitoring
raw_readings = [127, 255, 64, 191, 32, 223, 159, 96]
noise_floor = 37
calibration_offset = 13

# Irrelevant signal smoothing (dead path)
def smooth_signal(data, factor=0.1):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(smoothed[-1] * factor + data[i] * (1 - factor))
    return smoothed

# Decoy transformation - never used
decimated_readings = [x >> 2 for x in raw_readings if x > 50]

# Bitmask analysis with red herring logic
effective_bits = []
for val in raw_readings:
    active = 0
    temp = val ^ noise_floor
    for _ in range(8):
        if temp & 1:
            active += 1
        temp >>= 1
    effective_bits.append(active)

# False aggregation path
total_entropy = sum(math.log(x + 1) for x in raw_readings if x > 100)
entropy_threshold = 15.0
exceeds_noise = total_entropy > entropy_threshold  # Misleading boolean

# Real processing begins here — well hidden
processed = list(map(lambda x: (x ^ calibration_offset) & 0x7F, raw_readings))

# Conditional data routing (distraction)
data_route = 'A' if sum(processed) > 500 else 'B'
if data_route == 'X':  # Dead branch
    processed = [x * 2 for x in processed]

# Weighted metric calculation (core logic buried)
weights = defaultdict(float)
weights['clarity'] = 0.35
weights['stability'] = 0.45
weights['consistency'] = 0.20  # Note: unused weight as distractor

metric_data = {}
metric_data['clarity'] = sum(p for p in processed if p < 100) / len(processed)
metric_data['stability'] = sum(effective_bits) / len(effective_bits)

# Spurious data transformation
temp_metrics = {k: v * 1.1 for k, v in metric_data.items()}
baseline_adjustment = math.sin(math.pi / 6)  # Looks important, unused

# Core evaluation function with conditional expression
def evaluate_performance(metrics, w):
    base = 0.0
    base += metrics['clarity'] * w['clarity']
    base += metrics['stability'] * w['stability']
    # Apply bonus only if clarity threshold met (conditional expression)
    bonus = 25.0 if metrics['clarity'] > 60.0 else 10.0 if metrics['clarity'] > 50.0 else 0.0
    return base + bonus

# Secondary decoy function that's defined but not called
def analyze_trend(seq):
    trend_score = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trend_score += 1
        elif seq[i] < seq[i-1]:
            trend_score -= 1
    return abs(trend_score)

# Final computation
final_score = evaluate_performance(metric_data, weights)

# Output requirement
print(f"Result: {final_score}")