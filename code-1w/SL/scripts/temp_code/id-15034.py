def evaluate_performance(metrics, limit):
    # Initialize tracking variables
    count_valid = 0
    temp_sum = 0.0
    penalty_factor = 0.9
    debug_log = []

    # Irrelevant pre-scan: counts entries above arbitrary value (not used in final logic)
    outlier_count = 0
    for val in metrics.values():
        if val > 50:
            outlier_count += 1  # Dead-end counter, not used later

    # Core logic: score based on values exceeding threshold
    weighted_tally = 0
    scaling_base = 1.1
    for key, value in metrics.items():
        if value < 0:
            continue  # Ignore invalid negative metrics
        if value >= limit:
            weight = (value / 100.0) ** 0.5
            weighted_tally += weight
            temp_sum += value
            count_valid += 1
            debug_log.append(f"{key}:{weight:.2f}")  # Logged but not used

    # Secondary distraction: simulate calibration drift
    calibration_adjustment = 0
    for i in range(3):
        calibration_adjustment += (limit % (i + 1)) if i % 2 == 0 else 0  # Fake computation

    # Final score computation
    base_score = temp_sum / count_valid if count_valid > 0 else 0
    adjusted_score = base_score * weighted_tally * penalty_factor
    
    # Red herring transformation
    post_processed = round(adjusted_score * scaling_base + calibration_adjustment, 4)
    final_score = int(post_processed)  # Final deterministic integer result

    return final_score

# Simulated system metric data
data_payload = {
    'throughput': 85,
    'latency': 45,
    'error_rate': 5,
    'bandwidth': 92,
    'jitter': 38,
    'availability': 99
}

threshold = 60

# Extraneous helper: never called, adds noise
def calculate_efficiency_ratio(x, y):
    return (x * 0.75 + y * 1.2) / (x + y + 1)

# Unused state tracker
system_state = {"initialized": True, "mode": "diagnostic", "version": 2.1}

# Execution point of interest
final_score = evaluate_performance(data_payload, threshold)

# Output result as required
print(f"Result: {final_score}")