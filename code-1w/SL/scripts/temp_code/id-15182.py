from itertools import combinations

# Simulate sensor data calibration and weighted scoring
raw_readings = [12.5, 8.3, 15.7, 23.1, 9.4]
offsets = [0.2, -0.4, 0.1, 0.0, -0.3]
weights = [0.1, 0.2, 0.3, 0.25, 0.15]

# Apply offsets to calibrate readings
calibrated_readings = [r + o for r, o in zip(raw_readings, offsets)]

# Misleading transformation: normalize using max but not used later
normalized_readings = [cr / max(calibrated_readings) for cr in calibrated_readings]

# Generate all possible pairs of readings (distractor computation)
pairs = list(combinations(calibrated_readings, 2))
mean_product_pairs = sum([a * b for a, b in pairs]) / len(pairs)  # unused beyond this

# Filter out any low-confidence sensors (below threshold)
effective_readings = [cr for cr in calibrated_readings if cr >= 9.0]

# Adjust weights proportionally for effective sensors only
active_weights = [weights[i] for i in range(len(weights)) if calibrated_readings[i] >= 9.0]
total_active_weight = sum(active_weights)
normalized_weights = [w / total_active_weight for w in active_weights]

# Re-align filtered data
aligned_readings = [effective_readings[i] for i in range(len(effective_readings))]

# Compute weighted score
weighted_sum = sum(aligned_readings[i] * normalized_weights[i] for i in range(len(aligned_readings)))

# Secondary adjustment based on volatility check
volatility = max(aligned_readings) - min(aligned_readings)
adjustment_factor = 0.95 if volatility > 10 else 1.0
interim_score = weighted_sum * adjustment_factor

# Case-based final correction using string logic from status
status_flags = ['CALIBRATED', 'STABLE', 'ACTIVE']
status_concat = ''.join(status_flags).lower()

# Use string method to determine bonus
bonus_key = status_concat.count('a') * status_concat.count('e')
bonus_points = 0.5 if bonus_key >= 6 else 0.2

# Final aggregation
def calculate_final_score(data, weights):
    base = sum(d * w for d, w in zip(data, weights))
    penalty = 0.1 if len(data) == 4 else 0  # arbitrary rule
    return round(base + bonus_points - penalty, 4)

final_score = calculate_final_score(aligned_readings, normalized_weights)
print(f"Result: {final_score}")