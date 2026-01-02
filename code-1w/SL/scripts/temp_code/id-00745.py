def calculate_final_score(data, thresholds):
    # Preprocessing: Normalize data using min-max scaling
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in data]

    # Misleading transformation: frequency analysis (not used in final score)
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    avg_frequency = sum(freq_map.values()) / len(freq_map) if freq_map else 0

    # Threshold filtering with list comprehension
    above_threshold = [n for n in normalized if any(n >= t for t in thresholds)]

    # Weighted scoring using lambda and enumeration
    weights = list(map(lambda i: 0.9 ** i, range(len(above_threshold))))
    weighted_sum = sum(normalized[i] * weights[j] 
                        for j, i in enumerate([data.index(x) for x in sorted(data) if (x - min_val) / range_val in above_threshold][:len(weights)]))

    # Secondary distraction: simulate decay over hypothetical time steps
    decay_accumulator = 0.0
    temp = 1.0
    for _ in range(5):
        temp *= 0.85
        decay_accumulator += temp

    # Real computation path: boost based on density of high performers
    density_factor = len(above_threshold) / len(normalized) if normalized else 0
    stability_bonus = 1.0 if all(abs(normalized[i] - normalized[i+1]) < 0.2 for i in range(len(normalized)-1)) else 0.5

    # Final aggregation
    base_score = sum(above_threshold) * 100
    final_score = base_score * density_factor * stability_bonus

    return int(final_score)

# Input data and parameters
raw_data = [15, 22, 8, 41, 16, 29, 33, 20]
thresholds = [0.4, 0.6]

# Execute calculation
final_score = calculate_final_score(raw_data, thresholds)
print(f"Result: {final_score}")