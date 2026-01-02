from itertools import compress, cycle

# Simulate sensor data aggregation and decision scoring in an autonomous system
raw_readings = [0.88, 0.91, 0.76, 0.85, 0.94, 0.67, 0.82]
drift_compensation = [i % 4 == 0 for i in range(len(raw_readings))]
adjusted_readings = [r * (0.95 if drift else 1.05) for r, drift in zip(raw_readings, drift_compensation)]

# Irrelevant transformation: frequency modulation (distractor)
frequency_mod = [(r ** 2) / (i + 1) for i, r in enumerate(adjusted_readings)]
mod_sum = sum(frequency_mod[:3])  # Unused beyond this point

# Critical metric weights derived from historical performance
metric_weights = [0.2, 0.35, 0.15, 0.3]

# System state flags (some used, some not)
is_calibration_valid = len(raw_readings) > 5
is_stable_environment = all(r > 0.7 for r in raw_readings)
has_anomaly = any(r < 0.7 for r in adjusted_readings)

# Raw binary outcomes based on thresholds (used later)
raw_outcomes = [int(r >= 0.8) for r in adjusted_readings]

# Misleading secondary score (dead computation path)
baseline_score = sum(adjusted_readings) / len(adjusted_readings)
penalty_factor = 0.9 if has_anomaly else 1.0
baseline_score *= penalty_factor  # Not used in final logic

# Auxiliary mask generation using itertools (semi-relevant)
data_cycle = cycle([1, 0])
mask_pattern = [next(data_cycle) for _ in range(len(raw_outcomes))]
filtered_outcomes = list(compress(raw_outcomes, mask_pattern))  # Used only for distraction

# Aggregation function with nested logic
def aggregate_decision(outcomes):
    windowed = [outcomes[i:i+3] for i in range(len(outcomes)-2)]
    majority_votes = [1 if sum(win) >= 2 else 0 for win in windowed]
    return sum(majority_votes) % 5  # Hashed count

intermediate_result = aggregate_decision(raw_outcomes)

# Core evaluation logic
status_flags = [
    is_calibration_valid,
    is_stable_environment,
    intermediate_result > 1,
    len(filtered_outcomes) < 4
]

# Weighted boolean scoring
flag_scores = [int(flag) * weight for flag, weight in zip(status_flags, metric_weights)]

# Final performance score computation
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Standalone function defined after usage (simulates real codebase disorder)
def evaluate_performance(weights, outcomes):
    base = sum(outcomes) * weights[1]
    adjustment = (outcomes.count(1) % 3) * weights[2]
    penalty = (len(outcomes) - sum(outcomes)) * weights[0]
    bonus = 5.0 if status_flags[1] and status_flags[0] else 2.5
    return int(base - penalty + adjustment + bonus)

print(f"Result: {final_score}")