from collections import defaultdict

# Simulate system performance evaluation with noise and filtering
def main():
    raw_metrics = [120, 135, 142, 128, 139, 150, 133, 145]
    threshold = 130
    filtered_data = [x for x in raw_metrics if x > threshold]

    # Count frequency of performance bands
    freq_map = defaultdict(int)
    for val in filtered_data:
        band = val // 10 * 10
        freq_map[band] += 1

    # Irrelevant: Track secondary stats (not used in final score)
    secondary_stats = {}
    for k, v in freq_map.items():
        secondary_stats[k + 5] = v * 0.7  # Distractor computation

    # Determine efficiency based on spread of high performers
    min_band = min(freq_map.keys())
    max_band = max(freq_map.keys())
    efficiency = (max_band - min_band) / 10 if max_band != min_band else 1

    # Bonus logic with conditional expression
    peak_count = sum(1 for x in raw_metrics if x >= 140)
    bonus_flags = []
    for i in range(len(raw_metrics)):
        if i % 3 == 0 and raw_metrics[i] > 135:
            bonus_flags.append(f"B{i}")
    
    # Red herring: unused transformation
    transformed = [round(x ** 0.5, 2) for x in raw_metrics if x % 2 == 0]
    avg_transform = sum(transformed) / len(transformed) if transformed else 0

    # Core scoring function
    base_score = len(filtered_data) * 10
    adjustment = 5 if len(bonus_flags) >= 2 else -2
    
    def calculate_performance(flags, eff):
        multiplier = 1.5 if 'B0' in flags else 1.0
        return int(base_score + adjustment + (eff * 10) * multiplier)

    # Key execution point
    final_score = calculate_performance(bonus_flags, efficiency)
    
    # Dead code path (never executed)
    if False:
        final_score *= 0.5
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()