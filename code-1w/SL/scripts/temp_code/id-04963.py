from collections import defaultdict, Counter
import math

def analyze_access_patterns(logs):
    # Irrelevant function: analyzes access patterns but not used in final calculation
    freq = defaultdict(int)
    for log in logs:
        freq[log.split()[0]] += 1
    return sum(freq.values()) // len(freq) if freq else 0

def compute_baseline(n):
    # Dead code path: this function is defined but never called
    return sum(i * 0.5 for i in range(n)) % 7

def evaluate_streak(values):
    # Distractor function: computes longest increasing streak, not directly related
    max_streak = cur_streak = 1
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            cur_streak += 1
            max_streak = max(max_streak, cur_streak)
        else:
            cur_streak = 1
    return max_streak * 1.5

def validate_threshold(data, limit=100):
    # Unused validation logic — red herring
    overflow = any(x > limit for x in data)
    return not overflow

def filter_outliers(dataset, factor=1.5):
    # Heavily distracting computation: calculates IQR but result unused
    sorted_data = sorted(dataset)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    filtered = [x for x in dataset if lower_bound <= x <= upper_bound]
    return len(filtered) > len(dataset) * 0.7  # Not actually used

def process_performance(metrics, profile):
    # Core relevant logic starts here
    base = 0
    adjustments = defaultdict(float)

    # Real computation branch
    for k, v in metrics.items():
        if 'response' in k:
            base += v * 0.8
        elif 'error' in k:
            base -= v * 2.1
        elif 'timeout' in k:
            adjustments['latency_penalty'] += v * 1.3

    # Meaningful string manipulation affecting result
    mode = profile.get('mode', '').upper()
    flags = set(profile.get('features', []))

    if 'ADVANCED' in mode and 'retry' in flags:
        base *= 1.25

    # Critical data transformation using set operations
    known_keys = {'retries', 'caching', 'batching', 'retry'}
    active_features = flags & known_keys

    feature_bonus = len(active_features) * 3.2
    adjustments['feature_bonus'] = feature_bonus

    # Conditional override based on simulated environment state (irrelevant key)
    if profile.get('env') == 'prod_simulation':
        adjustments['simulated_env'] = -5.0  # Misleading negative adjustment

    # Actual answer depends only on specific components
    temp_result = base + sum(v for k, v in adjustments.items() if k != 'simulated_env')

    # Additional distraction: sorting unrelated list
    historical = [12, 15, 10, 20, 18]
    historical.sort(reverse=True)
    median_historical = historical[len(historical)//2]

    # Final adjustment with case conversion red herring
    tag = profile.get('tag', '')
    normalized_tag = tag.lower().replace('_', '').strip()
    if 'critical' in normalized_tag:
        temp_result += 10

    # Accumulation step that looks important but only one part matters
    cumulative = 0
    for i in range(3):
        cumulative += math.sin(math.pi / (i + 2))  # Adds ~2.35 to total, irrelevant

    final_score = int(temp_result + 0.5)  # Round to nearest integer

    # PRINT REQUIRED AT END
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input setup
    metrics = {
        'response_time_avg': 45,
        'error_rate': 8,
        'timeout_count': 6,
        'response_success': 92
    }

    user_data = {
        'mode': 'advanced_mode',
        'features': ['retry', 'caching', 'compression'],
        'env': 'prod_simulation',  # triggers decoy logic
        'tag': 'PRIORITY_CRITICAL'
    }

    # Trigger irrelevant functions (distractors)
    dummy_logs = [
        "192.168.1.1 GET /api",
        "192.168.1.2 POST /submit",
        "192.168.1.1 GET /api"
    ]
    _ = analyze_access_patterns(dummy_logs)

    sample_values = [5, 7, 6, 8, 10, 12, 11]
    _ = evaluate_streak(sample_values)

    raw_dataset = [10, 12, 14, 15, 100]  # contains outlier
    _ = filter_outliers(raw_dataset)

    # Execute target statement
    final_score = process_performance(metrics, user_data)