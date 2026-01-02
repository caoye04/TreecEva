from itertools import combinations

def analyze_text_patterns(text):
    words = text.lower().split()
    word_pairs = list(combinations(words, 2))
    pair_freq = {}
    for pair in word_pairs:
        pair_freq[pair] = pair_freq.get(pair, 0) + 1
    redundant_calc = sum(len(p[0]) * len(p[1]) for p in pair_freq.keys())
    return redundant_calc

def normalize_values(data_list):
    magnitude = sum(x ** 2 for x in data_list) ** 0.5
    if magnitude == 0:
        return [0 for _ in data_list]
    return [round(x / magnitude, 5) for x in data_list]

def calculate_harvest_efficiency(clusters, factor):
    flattened = []
    for cluster in clusters:
        for val in cluster:
            flattened.append(val * 1.1)
    
    # Irrelevant string processing (distractor)
    status_log = "Harvest analysis complete"
    padded_log = status_log.center(50, '-')
    log_checksum = sum(ord(c) for c in padded_log if c.isalpha())

    adjusted_vals = [v * factor for v in flattened]
    efficiency_scores = [max(0, min(100, v * 8.3)) for v in adjusted_vals]
    
    # Dead computation: used nowhere
    peak_window = []
    for i in range(len(efficiency_scores) - 2):
        window_avg = sum(efficiency_scores[i:i+3]) / 3
        peak_window.append(window_avg)
    
    overall_score = sum(efficiency_scores) / len(efficiency_scores)
    return round(overall_score, 2)

# Main execution
raw_input = "Season yield report shows variability across zones"
noise_value = analyze_text_patterns(raw_input)
base_factors = [4, 6, 7, 3, 8]
normalized_weights = normalize_values(base_factors)
adjustment_factor = normalized_weights[2]  # Key value extracted

cluster_data = [
    [12, 15, 10],
    [18, 14],
    [9, 11, 13, 16]
]

intermediate_total = sum(sum(cluster) for cluster in cluster_data)
scaled_intermediate = intermediate_total * adjustment_factor

final_yield = calculate_harvest_efficiency(cluster_data, adjustment_factor)
print(f"Result: {final_yield}")