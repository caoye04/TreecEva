import math

def analyze_readings(readings):
    # Irrelevant function: processes sensor-like data (avoided theme, but repurposed generically)
    normalized = [r / max(readings) for r in readings]
    filtered = [n for n in normalized if n > 0.5]
    return sum(filtered) * 0.7


def transform_sequence(seq):
    # Distractor: complex-looking transformation with no impact on final result
    shifted = [(x << 1) ^ 3 for x in seq]
    wrapped = [y % 100 + (y // 100) for y in shifted]
    return [math.sin(z * 0.1) for z in wrapped]


def compute_weighting(factors):
    # Dead code path — never called
    total = 0
    for f in factors:
        if f % 2 == 0:
            total += f ** 2
        else:
            total -= f // 3
    return total

# Irrelevant data structures
temp_log = [23, 24, 22, 25, 26, 21, 20]
config_flags = {'debug': False, 'trace': 1, 'mode': 'production'}
offset_table = {i: (i * i) % 7 for i in range(15)}

# Core relevant data
metric_data = [85, 90, 78, 92, 88]

# Misleading intermediate computation
calibration_factor = sum([x & 7 for x in temp_log])  # Uses bitwise AND but irrelevant
baseline_shift = len(offset_table) - config_flags['trace']
dummy_metric = calibration_factor * baseline_shift

# Hidden dependency chain
scaling_cache = {}
for val in metric_data:
    if val not in scaling_cache:
        scaling_cache[val] = round(math.log(val) * (val % 11), 4)

# Another distractor list comprehension with side effects (none)
_ = [transform_sequence([i, i+10]) for i in range(1, 6)]

# Key logic embedded in distraction
aggregated = 0
for idx, score in enumerate(metric_data):
    weight = (idx + 1) * 0.5
    adjusted = score * weight
    if idx % 2 == 0:
        adjusted += math.sqrt(weight * 10)
    aggregated += adjusted

# Conditional manipulation using boolean logic and comparisons
criterion_met = all(s > 75 for s in metric_data)
penalty_applied = False
if criterion_met and not penalty_applied:
    threshold_check = sum(1 for x in metric_data if x >= 85)
    if threshold_check >= 3:
        aggregated *= 1.1
    elif threshold_check == 2:
        aggregated *= 0.95
    else:
        aggregated *= 0.85

# Decoy assignment
interim_result = analyze_readings([50, 60, 70, 80, 90])
interim_result += dummy_metric  # Adds noise

# Actual target computation
final_score = 0
def evaluate_performance(data):
    base = sum(data)
    bonus = 0
    for i, v in enumerate(data):
        if v > 80:
            bonus += int(v / 10) * (i + 1)
    # Apply exponential decay factor on bonus (advanced arithmetic)
    decayed_bonus = bonus * (0.9 ** len(data))
    return base + round(decayed_bonus)

final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")