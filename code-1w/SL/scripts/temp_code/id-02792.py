from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:
                count += 1
    return count

def extract_features(data):
    feature_set = []
    for item in data:
        if item % 3 == 0:
            feature_set.append(item * 2)
        elif item % 5 == 0:
            feature_set.append(item // 2)
    return feature_set

def calculate_final_score(ranks, multiplier):
    base = sum(ranks)
    adjustment = 0
    
    # Real logic path
    sorted_ranks = sorted(ranks, reverse=True)
    top_three_product = 1
    for rank in sorted_ranks[:3]:
        top_three_product *= rank
    
    # Distractor: complex but unused pattern analysis
    pair_count = 0
    for a, b in combinations(sorted_ranks, 2):
        if (a + b) % 4 == 0:
            pair_count += 1
    temp_analysis = [a - b for a, b in zip(sorted_ranks, sorted_ranks[1:])]
    spike_count = sum(1 for x in temp_analysis if x > 2)
    
    # Another distractor branch
    derived_values = []
    for val in sorted_ranks:
        if val > 5:
            derived_values.append(val ** 0.5)
    avg_derived = sum(derived_values) / len(derived_values) if derived_values else 0
    
    # Actual contribution
    if top_three_product > 100:
        adjustment += 15
    else:
        adjustment += 5
    
    # More irrelevant computation
    histogram = {}
    for r in ranks:
        histogram[r] = histogram.get(r, 0) + 1
    mode_value = max(histogram, key=histogram.get)
    
    # Final score depends only on base, multiplier, and adjustment from top_three_product
    final = base * multiplier + adjustment
    
    # Dead code - never used
    outlier_check = [x for x in ranks if x < 2]
    if len(outlier_check) > 1:
        final -= 10
    
    return int(final)

# Main execution
raw_input = [4, 6, 3, 8, 2, 9, 5]

# Irrelevant preprocessing
filtered_data = [x for x in raw_input if x > 2]
distinct_pairs = list(combinations(filtered_data, 2))
pair_sums = [a + b for a, b in distinct_pairs if a != b]
sum_frequency = {s: pair_sums.count(s) for s in set(pair_sums)}

# Feature extraction - semi-relevant but not used in final score
features = extract_features(raw_input)

# Pattern analysis - completely irrelevant
pattern_count = analyze_patterns([1, 2, 3, 4, 5])

# Key data for actual logic
rank_data = [x for x in raw_input if x >= 3]
bonus_multiplier = len(features) // 2

# This calls the function containing both critical and distracting logic
final_score = calculate_final_score(rank_data, bonus_multiplier)

print(f"Result: {final_score}")