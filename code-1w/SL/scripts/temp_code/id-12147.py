from collections import defaultdict, Counter

def analyze_pattern(sequence):
    freq_map = defaultdict(int)
    for item in sequence:
        freq_map[item] += 1
    return dict(freq_map)

def compute_aggregate(data, weights):
    weighted_sum = 0
    total_weight = sum(weights)
    temp_result = [a * b for a, b in zip(data, weights)]
    
    # Irrelevant intermediate computation (distractor)
    squared_chain = [x**2 for x in data if x % 2 == 0]
    placeholder_sum = sum(squared_chain) * 0.1
    
    for val, weight in zip(data, weights):
        weighted_sum += val * weight
    
    return int(weighted_sum / total_weight) if total_weight else 0

def main():
    # Input data representing sensor readings over time
    timestamps = [101, 102, 103, 104, 105, 106, 107]
    readings = [18, 22, 19, 25, 21, 17, 23]
    weights = [1, 2, 1, 3, 2, 1, 2]

    # Auxiliary analysis (not directly used in final result)
    reading_stats = analyze_pattern(readings)
    unique_count = len(reading_stats)
    mode_info = Counter(readings).most_common(1)

    # Nested loop simulating time-window correlation (partially irrelevant)
    correlations = []
    for i, t1 in enumerate(timestamps[:-1]):
        row = []
        for j, t2 in enumerate(timestamps[i+1:], start=i+1):
            if abs(t2 - t1) <= 3:
                row.append((t1 + t2) % 5)
        if row:
            correlations.append(sum(row))

    # Key processing chain
    adjusted_readings = [r + (i * 0.5) for i, r in enumerate(readings)]  # Slight drift adjustment
    floored_readings = [int(x) for x in adjusted_readings]

    # Critical assignment point
    final_score = compute_aggregate(floored_readings, weights)

    # More red herring variables
    outlier_flags = [1 if abs(r - 20) > 5 else 0 for r in floored_readings]
    correction_factor = sum(outlier_flags) * 0.5

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()