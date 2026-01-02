import math

# Simulated employee performance metrics across multiple dimensions
def generate_metrics():
    raw_scores = {
        'productivity': 84,
        'teamwork': 73,
        'innovation': 91,
        'punctuality': 96,
        'leadership': 67,
        'adaptability': 88
    }
    return raw_scores

# Misleading function - not actually used in final calculation
def calculate_average_old_system(scores):
    total = 0
    count = 0
    for k, v in scores.items():
        if k in ['productivity', 'punctuality']:
            total += v * 1.2
        else:
            total += v * 0.8
        count += 1
    return total / count if count else 0

# Unused utility - red herring
def normalize_score(value, max_val=100):
    return value / max_val

# Another decoy function with complex logic but no impact
def compute_entropy(data_dict):
    total = sum(data_dict.values())
    entropy = 0
    for val in data_dict.values():
        prob = val / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 3)

# Weight adjustment based on department (only some weights matter)
def get_department_weights(dept_code):
    all_weights = {
        'engineering': {
            'productivity': 0.25,
            'teamwork': 0.15,
            'innovation': 0.20,
            'punctuality': 0.10,
            'leadership': 0.15,
            'adaptability': 0.15
        },
        'sales': {
            'productivity': 0.30,
            'teamwork': 0.10,
            'innovation': 0.05,
            'punctuality': 0.20,
            'leadership': 0.25,
            'adaptability': 0.10
        },
        'design': {
            'productivity': 0.15,
            'teamwork': 0.20,
            'innovation': 0.30,
            'punctuality': 0.05,
            'leadership': 0.10,
            'adaptability': 0.20
        }
    }
    # Only engineering weights are actually used
    return all_weights.get('engineering', all_weights['engineering'])

# Complex transformation with filtering and scaling
def preprocess_metrics(metrics):
    processed = {}
    filters = {'min_thresh': 70, 'bonus_factor': 1.1}
    bonus_applied = 0

    for key, value in metrics.items():
        # Filtering logic: only scores >= 70 are kept
        if value >= filters['min_thresh']:
            processed[key] = value
            if value > 90:
                processed[key] = int(value * filters['bonus_factor'])
                bonus_applied += 1

    # Irrelevant counters
    stats = {
        'valid_count': len(processed),
        'bonus_awarded': bonus_applied,
        'theoretical_max': 100 * len(processed)
    }

    # Add dummy entry to mislead
    processed['ghost_metric'] = 0  # This will be filtered later

    return processed, stats

# Main evaluation logic - this is where the real computation happens
def evaluate_performance(metrics, weights):
    # Step 1: Filter and preprocess
    clean_metrics, _ = preprocess_metrics(metrics)
    
    # Step 2: Remove any zero or invalid metrics
    clean_metrics = {k: v for k, v in clean_metrics.items() if v > 0}
    
    # Step 3: Apply weights only to matching keys
    weighted_sum = 0.0
    weight_sum = 0.0
    
    for metric, value in clean_metrics.items():
        if metric in weights:
            contribution = value * weights[metric]
            weighted_sum += contribution
            weight_sum += weights[metric]
    
    # Step 4: Normalize by total active weights
    final = weighted_sum / weight_sum if weight_sum else 0
    
    # Step 5: Apply experience multiplier (fixed in this case)
    experience_years = 5
    exp_multiplier = 1 + (experience_years * 0.02)
    final *= exp_multiplier
    
    # Step 6: Cap at maximum possible score
    final = min(final, 100.0)
    
    # Step 7: Round to 3 decimal places
    return round(final, 3)

# Irrelevant aggregation function - dead code path
def aggregate_by_category(raw_data):
    categories = {
        'execution': ['productivity', 'punctuality'],
        'soft_skills': ['teamwork', 'adaptability'],
        'strategy': ['innovation', 'leadership']
    }
    grouped = {cat: [] for cat in categories}
    for metric, score in raw_data.items():
        for cat, members in categories.items():
            if metric in members:
                grouped[cat].append(score)
    return {k: sum(v)/len(v) for k, v in grouped.items()}

# Global constants - some are decoys
BASELINE_THRESHOLD = 75
PERFORMANCE_BONUS_RATE = 0.08
UNUSED_LIMIT = 999
ANALYSIS_MODE = "comprehensive"

# Execution flow
if __name__ == "__main__":
    # Step 1: Get raw data
    metric_data = generate_metrics()
    
    # Step 2: Retrieve correct weights
    weights = get_department_weights('engineering')
    
    # Step 3: Preprocessing (has side effects via filtering)
    processed_data, summary_stats = preprocess_metrics(metric_data)
    
    # Step 4: Evaluate final performance score
    final_score = evaluate_performance(metric_data, weights)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    # Additional outputs - distractions
    # entropy_value = compute_entropy(metric_data)
    # category_scores = aggregate_by_category(metric_data)
    # legacy_avg = calculate_average_old_system(metric_data)