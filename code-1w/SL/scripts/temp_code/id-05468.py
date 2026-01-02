from collections import defaultdict, Counter
import math

# Simulated sensor readings over time (real data)
sensor_readings = [104.5, 98.6, 102.1, 97.3, 103.0, 99.8, 101.2, 96.7, 100.4, 95.9]

# Irrelevant auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E']
label_count = {label: 0 for label in dummy_labels}
for i in range(len(sensor_readings)):
    label_count[dummy_labels[i % 5]] += 1

# Data preprocessing pipeline
filtered_readings = [x for x in sensor_readings if 97 <= x <= 103]
reading_stats = {
    'min': min(filtered_readings),
    'max': max(filtered_readings),
    'range': max(filtered_readings) - min(filtered_readings)
}

# Weight assignment using exponential decay (relevant)
time_weights = [math.exp(-0.1 * i) for i in range(len(filtered_readings))]

# Misleading normalization path (dead end)
normalized_wrong = [w / sum(time_weights) for w in time_weights]
scale_factor = sum(normalized_wrong)  # unused later

# Conditional adjustment based on trend (red herring block)
trend_direction = 'positive' if filtered_readings[-1] > filtered_readings[0] else 'negative'
adjustment_map = defaultdict(lambda: 0.95)
adjustment_map['positive'] = 1.05
adjustment_map['negative'] = 0.85
trend_adjustment = adjustment_map[trend_direction]

# Actual processing chain with key logic
weighted_values = [v * w for v, w in zip(filtered_readings, time_weights)]
composite_score = sum(weighted_values) / sum(time_weights)

# Secondary transformation with conditional expression (relevant)
penalty = 5.0 if composite_score < 100 else 0.0
adjusted_composite = composite_score - penalty

# Bit manipulation decoy (irrelevant but plausible)
bit_encoded = 0
for val in filtered_readings:
    bit_encoded ^= int(val)
bit_correction = bit_encoded & 0xFF  # looks important, unused

# Frequency analysis (distractor)
freq_counter = Counter([round(x) for x in filtered_readings])
mode_value = freq_counter.most_common(1)[0][0]

# Core algorithm: iterative refinement using enumerate and conditional updates
refined_weights = []
for idx, weight in enumerate(time_weights):
    if idx == 0:
        refined_weights.append(weight * 1.1)
    else:
        prev_refined = refined_weights[-1]
        decay_adj = 0.98 if idx % 2 == 0 else 1.02
        new_weight = prev_refined * weight / time_weights[idx-1] * decay_adj
        refined_weights.append(new_weight)

# Normalization of refined weights (critical step)
sum_refined = sum(refined_weights)
final_weights = [w / sum_refined for w in refined_weights]

# Correction factor computed via logical conditions (key dependency)
base_factor = 2.0 if adjusted_composite > 100 else 1.5
volatility = reading_stats['range'] / reading_stats['min']
volatility_boost = 1.25 if volatility > 0.05 else 1.0
logical_trigger = (adjusted_composite > 100) and (volatility > 0.04)
correction_factor = base_factor * volatility_boost if logical_trigger else base_factor * 0.9

# Key assignment point — target of evaluation
threshold_balance = final_weights[-1] * correction_factor

# Irrelevant printing (misdirection)
print(f"Signal integrity: {bit_correction}")
print(f"Dominant reading: {mode_value}")

# Only this output matters
print(f"Target result: {threshold_balance}")