from collections import defaultdict
import math

def analyze_metrics(values):
    stats = defaultdict(float)
    temp_buffer = []
    total_positive = 0
    total_negative = 0

    for idx, val in enumerate(values):
        if val > 0:
            total_positive += val
            temp_buffer.append(val * 0.1)
        elif val < 0:
            total_negative += abs(val)
            temp_buffer.append(-val * 0.05)

    stats['pos_total'] = total_positive
    stats['neg_total'] = total_negative
    stats['buffer_sum'] = sum(temp_buffer)

    # Irrelevant transformation
    transformed = [math.log(1 + x) for x in temp_buffer if x > 0.1]
    stats['transformed_count'] = len(transformed)

    return stats

def compute_weighted_average(nums, factors):
    weighted_sum = 0.0
    factor_sum = 0.0
    for n, f in zip(nums, factors):
        weighted_sum += n * f
        factor_sum += f
    return weighted_sum / factor_sum if factor_sum != 0 else 0

# Simulate sensor readings with noise filtering
data = [12, -5, 8, 15, -3, 9]
weights = [0.3, 0.1, 0.2, 0.15, 0.05, 0.2]

# Preliminary analysis (partially irrelevant)
diagnostic_stats = analyze_metrics(data)

# Secondary derived variables that don't impact final result
correction_factor = diagnostic_stats['buffer_sum'] * 0.25
offset_adjustment = len(data) // 2

# Core computation chain
base_average = compute_weighted_average(data, weights)
scaled_base = base_average * 1.5

# Apply conditional adjustment based on sign distribution
if diagnostic_stats['pos_total'] > diagnostic_stats['neg_total'] * 2:
    scaled_base += 5
else:
    scaled_base -= 2

# Bitwise flag simulation (distractor)
status_flag = 0b1010
status_flag ^= 0b1100  # meaningless toggle
status_flag |= 0b0001

# Dummy loop with no effect
rolling_temp = 0
for i in range(3):
    rolling_temp = (rolling_temp + i) % 2

# Final score computation - depends only on scaled_base and data length adjustment
length_modifier = len(data) - offset_adjustment  # offset_adjustment is fixed
final_score = int(scaled_base + length_modifier)

print(f"Result: {final_score}")