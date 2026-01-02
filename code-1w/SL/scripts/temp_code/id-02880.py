from collections import defaultdict
from itertools import combinations

# Simulate sensor data processing with noise filtering and thresholding
def main():
    raw_readings = [105, 210, 150, 99, 450, 300, 120, 85, 250]
    baseline = 100
    adjustment_factor = 0.1
    
    # Irrelevant statistical placeholders (distractors)
    mean_deviation = 0
    peak_count = 0
    total_variance = 0.0

    # Step 1: Normalize readings relative to baseline
    normalized = [x / baseline for x in raw_readings]

    # Step 2: Apply nonlinear correction (log-like dampening on high values)
    corrected = [val if val <= 1.5 else 1.5 + (val - 1.5) ** 0.5 for val in normalized]

    # Step 3: Identify potential anomalies (unused path - red herring)
    anomalies = []
    for i, val in enumerate(corrected):
        if val > 2.0:
            anomalies.append(i)
    anomaly_flag = len(anomalies) > 0  # Not used later

    # Step 4: Scale back to approximate original magnitude with adjustment
    scaled_values = [int(baseline * val * (1 + adjustment_factor)) for val in corrected]

    # Step 5: Define dynamic thresholds using combinatorial analysis (overkill - distractor)
    threshold_combinations = list(combinations([110, 120, 130], 2))
    temp_thresholds = [sum(pair) / 2 for pair in threshold_combinations]
    thresholds = defaultdict(lambda: 115)
    for idx, thr in enumerate(temp_thresholds):
        thresholds[f'level_{idx}'] = int(thr)

    # Step 6: Compute aggregate score based on threshold crossings
    def compute_aggregate(values, limits):
        count = 0
        cross_map = defaultdict(int)
        for v in values:
            if v > limits['level_0']:
                count += 1
                cross_map['high'] += 1
            elif v > limits['level_1']:
                cross_map['medium'] += 1
        # Final logic: 50 base + 10 per high reading above primary threshold
        return 50 + 10 * cross_map['high']

    # Step 7: Execute key computation
    intermediate_checksum = sum(scaled_values) % 97  # Distractor
    debug_snapshot = {"size": len(scaled_values), "max_val": max(scaled_values)}  # Unused

    final_score = compute_aggregate(scaled_values, thresholds)

    # Output result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()