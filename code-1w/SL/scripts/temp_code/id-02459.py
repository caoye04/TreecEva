from collections import Counter

def analyze_frequency(data):
    freq = Counter(data)
    return {k: v for k, v in freq.items() if v > 1}

def apply_modifiers(values, modifier):
    adjusted = []
    temp_sum = 0
    for val in values:
        temp_sum += val * modifier
        if val % 2 == 0:
            adjusted.append(val + modifier)
        else:
            adjusted.append(val - modifier)
    noise = sum([i**2 for i in range(3)])  # Irrelevant computation
    return adjusted

def compute_balance(arr):
    left, right = 0, sum(arr)
    for i in range(len(arr)):
        right -= arr[i]
        if left == right:
            return i
        left += arr[i]
    return -1

def evaluate_performance(seq, limit):
    filtered = [x for x in seq if x >= limit]
    sorted_vals = sorted(filtered, reverse=True)
    if len(sorted_vals) < 3:
        return 0
    top_three_sum = sum(sorted_vals[:3])
    penalty = 0
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] == sorted_vals[i-1]:
            penalty += 1
    result_set = set(sorted_vals)
    unique_count_bonus = len(result_set) * 2
    intermediate_total = top_three_sum + unique_count_bonus - penalty
    
    # Distractor block: complex but unused calculation
    distractor_dict = {}
    for x in seq:
        bin_key = x // 10
        distractor_dict[bin_key] = distractor_dict.get(bin_key, 0) + 1
    distractor_sorted = sorted(distractor_dict.values())
    median_idx = len(distractor_sorted) // 2
    pseudo_median = distractor_sorted[median_idx] if distractor_sorted else 0
    dummy_aggregate = sum(distractor_sorted) * pseudo_median
    
    # Actual logic continues
    base_distribution = [x % 7 for x in seq if x > 0]
    mode_counter = Counter(base_distribution)
    most_frequent_remainder = mode_counter.most_common(1)[0][1]
    final_score = intermediate_total + most_frequent_remainder
    
    return final_score

# Main execution
raw_data = [42, 35, 28, 42, 35, 50, 55, 35, 40, 45, 30, 35]
distribution = apply_modifiers(raw_data, 3)
threshold = 100

# Unused helper call (dead code path)
analysis_result = analyze_frequency(raw_data)
index_balance = compute_balance([10, 20, 30])

final_score = evaluate_performance(distribution, threshold)
print(f"Target result: {final_score}")