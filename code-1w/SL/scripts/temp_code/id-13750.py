from itertools import compress, count

def analyze_performance(metrics):
    base_scores = [m * 1.1 for m in metrics if m > 0]
    adjusted_scores = []
    offset = 3
    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            adjusted_scores.append(score + 0.5)
        else:
            adjusted_scores.append(score - 0.2)
    return adjusted_scores

def calculate_rating(entries, factor):
    weights = [0.8, 1.2, 0.9, 1.1, 1.0]
    weighted_sum = sum(e * w for e, w in zip(entries, weights[:len(entries)]))
    rating = weighted_sum * factor

    # Distractor: irrelevant transformation
    temp_results = [x ** 0.5 for x in entries if x > 5]
    unused_aggregation = sum(temp_results) / len(temp_results) if temp_results else 0

    # Another red herring: dead code path
    debug_mode = False
    if debug_mode:
        print("Debug info:", unused_aggregation)

    return int(rating)

# Main execution
raw_data = [4, 7, 6, 8]
efficiency = 1.3

# Irrelevant preprocessing (moderately distracting)
duplicates_removed = list(set(raw_data))
sorted_indices = [i for i, _ in sorted(enumerate(raw_data), key=lambda x: x[1])]
indexed_stream = list(zip(count(start=1), raw_data))

# Real computation chain
processed = analyze_performance(raw_data)
contributions = [round(p * 0.95) for p in processed]

# Key statement
final_score = calculate_rating(contributions, efficiency)

# Print result as required
print(f"Result: {final_score}")