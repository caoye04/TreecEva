from collections import defaultdict, Counter
from itertools import zip_longest

def analyze_pattern(sequence):
    freq = Counter(sequence)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    mode = sorted_items[0][0]
    
    # Distractor: pattern analysis with no impact on final result
    runs = []
    current_run = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)
    avg_run = sum(runs) / len(runs) if runs else 0
    
    return mode, avg_run

def calculate_adjusted_efficiency():
    # Simulated sensor readings over time (real data stream)
    timestamps = list(range(10, 200, 10))
    readings = [t * 0.7 + ((t % 30) // 10) * 2.5 for t in timestamps]
    
    # Normalize readings using min-max scaling (relevant)
    min_val, max_val = min(readings), max(readings)
    normalized = [(r - min_val) / (max_val - min_val) for r in readings]
    
    # Bucket into performance tiers (relevant)
    tier_count = defaultdict(int)
    for n in normalized:
        if n < 0.3:
            tier_count['low'] += 1
        elif n < 0.7:
            tier_count['medium'] += 1
        else:
            tier_count['high'] += 1
    
    # Efficiency base score calculation (key step)
    base_efficiency = (tier_count['high'] * 2 + tier_count['medium']) * 10
    
    # Distractor: complex temporal correlation matrix (not used)
    correlations = []
    for i in range(len(normalized) - 1):
        corr = abs(normalized[i+1] - normalized[i])
        correlations.append(corr * 0.95)
    smoothed_corr = sum(correlations) / len(correlations) if correlations else 0
    
    # Simulated calibration offset (distractor)
    calibration_log = {}
    for t in timestamps[::5]:
        residual = (t * 0.01) ** 2
        calibration_log[t] = round(residual, 3)
    
    # Critical adjustment based on outlier detection (semi-relevant)
    outliers = [n for n in normalized if n > 0.9 or n < 0.05]
    penalty = len(outliers) * 15
    
    # Final score computation (answer point)
    final_score = base_efficiency - penalty
    
    # Additional red herring: zipping unrelated sequences
    dummy_labels = [f"S{i}" for i in range(len(timestamps))]
    paired_data = list(zip_longest(timestamps, dummy_labels, fillvalue="X"))
    
    # Dead code path (never executed)
    if False:
        temp_sum = 0
        for p in paired_data:
            if isinstance(p[0], int):
                temp_sum += p[0] * 0.1
        final_score += temp_sum
    
    return final_score

def main():
    # Input data: system event codes (used in analysis but not efficiency)
    events = [201, 203, 201, 205, 203, 203, 207, 201, 205, 205, 205, 207]
    dominant_event, run_stat = analyze_pattern(events)
    
    # State tracking with irrelevant counters
    status_tracker = {"init": 0, "active": 0, "error": 0}
    for e in events:
        if e == 201:
            status_tracker["init"] += 1
        elif e in (203, 205):
            status_tracker["active"] += 1
        else:
            status_tracker["error"] += 1
    
    # Key execution point
    final_score = calculate_adjusted_efficiency()
    
    # Output requirement
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()