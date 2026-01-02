def analyze_component(metrics, threshold=0.75):
    high_perf = [m for m in metrics if m > threshold]
    low_perf = [m for m in metrics if m <= threshold]
    ratio = len(high_perf) / len(metrics) if metrics else 0
    return ratio, high_perf, low_perf


def normalize_values(entries):
    total = sum(entries)
    return [round(e / total, 4) for e in entries] if total else [0] * len(entries)

# Simulate sensor data aggregation from distributed nodes
raw_data = [0.82, 0.63, 0.91, 0.45, 0.77, 0.69, 0.88, 0.53]
dispatch_codes = ['A7', 'C2', 'B9', 'D4', 'E1', 'F3', 'G8', 'H6']

# Irrelevant transformation: convert codes to ASCII sums
ascii_sum = sum(sum(ord(c) for c in code) for code in dispatch_codes)
scaling_factor = (ascii_sum % 50) / 100  # Random scaling factor, not used later

# Normalize raw sensor readings
normalized_readings = normalize_values(raw_data)

# Filter and analyze performance segments
effective_ratio, strong_nodes, weak_nodes = analyze_component(normalized_readings, threshold=0.12)

# Misleading intermediate calculation (dead-end path)
temp_diagnostic = max(normalized_readings) - min(normalized_readings)
flagged_count = len([x for x in normalized_readings if 0.05 < x < 0.1])

# Core logic: compute weighted score using string-based node classification
weight_map = {}
for code in dispatch_codes:
    prefix = code[0]
    if prefix in 'ABC':
        weight_map[code] = 1.2
    elif prefix in 'DEF':
        weight_map[code] = 0.9
    else:
        weight_map[code] = 1.0

# Attach weights to normalized values
weighted_scores = []
for i, val in enumerate(normalized_readings):
    key = dispatch_codes[i]
    weight = weight_map.get(key, 1.0)
    weighted_scores.append(round(val * weight, 4))

# Secondary adjustment based on position (even/odd index)
adjusted_scores = []
for idx, score in enumerate(weighted_scores):
    if idx % 2 == 0:
        adjusted_scores.append(score * 1.05)
    else:
        adjusted_scores.append(score * 0.98)

# Aggregate final statistics
sum_adjusted = sum(adjusted_scores)
count_above_avg = len([s for s in adjusted_scores if s > sum_adjusted / len(adjusted_scores)])

# Simulate data provenance trace (distractor)
trace_log = ""
for i, code in enumerate(dispatch_codes):
    status = "CRITICAL" if i in [2, 6] else "NORMAL"
    trace_log += f"Node:{code}|Val:{normalized_readings[i]:.3f}|St:{status}\n"

# Count how many nodes have 'high impact' after full processing
high_impact = [s for s in adjusted_scores if s > 0.15]
impact_fluctuation = (max(adjusted_scores) - min(adjusted_scores)) * len(high_impact)

# Final performance score computation
def calculate_performance(data):
    base = sum(data)
    penalty = 0.0
    if count_above_avg < 3:
        penalty = 0.05 * base
    bonus = 0.01 * len(high_perf) * base  # high_perf from earlier tuple unpacking
    result = base - penalty + bonus
    return round(result, 4)

final_score = calculate_performance(adjusted_scores)
print(f"Result: {final_score}")