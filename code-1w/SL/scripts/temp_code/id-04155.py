from itertools import combinations

def analyze_efficiency(logs):
    # Irrelevant helper function – not used in final computation
    return sum(len(log) for log in logs if len(log) > 5)

def preprocess_data(records):
    # Semi-relevant preprocessing: modifies structure but only one output is used
    cleaned = [r.strip().lower() for r in records]
    char_count = sum(len(r) for r in cleaned)
    tokenized = [r.split('.') for r in cleaned]
    flat_tokens = [item for sublist in tokenized for item in sublist]
    return flat_tokens, char_count  # Only char_count is later used

def evaluate_performance(metrics, weights):
    weighted_sum = 0
    temp_results = []
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        adjustment = 1.0
        if i % 2 == 0:
            adjustment = 0.9 + i * 0.05
        adjusted_metric = metric * adjustment
        temp_results.append(adjusted_metric)
        
        # Distractor: complex but unused calculation
        pair_sums = [a + b for a, b in combinations(temp_results, 2)] if len(temp_results) > 1 else [0]
        noise_correction = sum(pair_sums) / (len(pair_sums) + 1)
    
        weighted_sum += adjusted_metric * weight
    
    # Final logic step: apply bonus if performance consistency is high
    variance_proxy = max(temp_results) - min(temp_results)
    consistency_bonus = 10 if variance_proxy < 15 else 0
    
    return int(weighted_sum + consistency_bonus)

# Main execution block
raw_records = ['USER.Query...', 'SYS.Init...', 'NET.Request.Data.Stream...', 'CACHE.Hit.', 'ERROR.Retry...']
data_tokens, total_chars = preprocess_data(raw_records)

# Key variables for evaluation
base_metrics = [85, 76, 90, 80]  # Performance indicators across dimensions
weights_list = [0.2, 0.3, 0.25, 0.25]

# Dummy operations to increase cognitive load
char_stats = {chr(i): total_chars % (i + 1) for i in range(65, 70)}
dummy_pairs = list(combinations(base_metrics, 2))
avg_pair_value = sum(a * b for a, b in dummy_pairs) / len(dummy_pairs) if dummy_pairs else 0

# Misleading intermediate score
interim_score = sum(m * w for m, w in zip(base_metrics, weights_list)) * (total_chars % 40)

# Critical statement
final_score = evaluate_performance(base_metrics, weights_list)

# Output result as required
print(f"Target result: {final_score}")