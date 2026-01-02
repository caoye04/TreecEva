import itertools

def analyze_text_patterns(text):
    # Irrelevant function: analyzes character frequencies (dead end)
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [item[0] for item in sorted_freq[:5]]

def preprocess_metrics(raw_scores):
    # Distractor transformation: applies multiple irrelevant scaling operations
    transformed = []
    scaling_factor = 1.75
    offset = 3
    for val in raw_scores:
        temp_val = (val * scaling_factor) + offset
        if temp_val > 50:
            temp_val = temp_val / 2.5
        transformed.append(round(temp_val, 3))
    return transformed

def generate_combinations(elements):
    # Decoy function using itertools — generates all 3-combinations (not used in final logic)
    return list(itertools.combinations(elements, 3))

def filter_outliers(data, threshold=10):
    # Seemingly relevant but actually bypassed in main logic
    return [x for x in data if abs(x - sum(data)/len(data)) <= threshold]

def compute_entropy(values):
    # Red herring: computes entropy but result is unused
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    from math import log2
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def core_evaluation(seq):
    # Actual core logic buried among distractions
    base_sum = sum(x ** 2 for x in seq if x % 2 == 1)  # Sum squares of odd numbers
    adjustment = len([x for x in seq if x > 0]) * 2
    return base_sum - adjustment

def evaluate_performance(metrics, data_map):
    # Main evaluation path with embedded distractors
    temp_results = []
    decoy_accum = 0
    
    for k in ['X1', 'Y2', 'Z3']:
        if k in data_map and isinstance(data_map[k], list):
            # This block appears important but only one case matters
            if k == 'X1':
                processed = [x for x in data_map[k] if x in metrics]
                temp_results.append(sum(processed))
            elif k == 'Y2':
                # Dead branch: adds noise
                decoy_accum += sum(x * 0.5 for x in data_map[k] if x < 10)
            else:
                # Unused path
                decoy_accum -= len(data_map[k])
    
    # Critical computation hidden in middle
    primary_metric = core_evaluation(list(metrics))
    secondary_weight = len(metrics.intersection({2, 4, 6, 8}))
    
    # Final formula
    score = primary_metric * 3 + secondary_weight * 4 - temp_results[0]
    
    # Misleading normalization step (not applied to final answer)
    if score > 100:
        normalized = score / 1.5
    else:
        normalized = score * 1.1
    
    return int(score)  # Only this matters

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # Input data setup with multiple decoys
    raw_input_scores = [12, 7, 3, 8, 1, 4, 9]
    filtered_data = preprocess_metrics(raw_input_scores)  # Irrelevant processing
    
    # Real input sets
    metric_set = {1, 3, 7, 9}  # Odd numbers from raw_input_scores
    benchmark_data = {
        'X1': [1, 3, 5],           # Used in temp_results
        'Y2': [2, 4, 6, 8],         # Partially processed, doesn't affect outcome
        'Z3': [10, 20],             # Dead entry
        'config': {'mode': 'strict'}  # Useless metadata
    }
    
    # Unused structures to increase interference
    all_triplets = generate_combinations(list(metric_set))
    text_sample = "Performance evaluation sequence"
    top_chars = analyze_text_patterns(text_sample)
    
    # Decoy calculations
    outlier_filtered = filter_outliers(raw_input_scores)
    entropy_value = compute_entropy(raw_input_scores)
    
    # Key execution point
    final_score = evaluate_performance(metric_set, benchmark_data)
    
    # Output required result
    print(f"Result: {final_score}")