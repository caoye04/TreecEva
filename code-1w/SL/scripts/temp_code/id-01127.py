import itertools

# Simulated system performance metrics (some are relevant, others are red herrings)
def collect_metrics():
    raw_data = [78, 95, 88, 45, 73, 90, 82]
    
    # Irrelevant transformations (distractors)
    squared_values = [x**2 for x in raw_data if x > 50]
    filtered_pairs = list(itertools.combinations(squared_values[:4], 2))
    checksum = sum(filtered_pairs[0]) % 17

    # Relevant metrics extraction
    response_times = [120, 85, 95, 110, 90]  # in ms
    success_rate = 0.93
    throughput = 47.2  # transactions per second
    error_count = 5

    # Misleading intermediate calculation (dead path)
    if len(raw_data) > 10:
        ghost_metric = max(squared_values) - min(squared_values)
    else:
        ghost_metric = None  # unused

    # Distractor: complex lambda with no impact
    transform_fn = lambda x, y: (x + y) // 3 if y != 0 else 0
    dummy_agg = transform_fn(sum(response_times), checksum)

    # Actual metrics used in final evaluation
    return {
        'latency': sum(response_times) / len(response_times),
        'success': success_rate,
        'volume': throughput,
        'consistency': len([x for x in raw_data if 80 <= x <= 100]),
        'errors': error_count
    }

# Weighting function with irrelevant branching
def apply_weights(data):
    base_weights = {
        'latency': 0.3,
        'success': 0.25,
        'volume': 0.2,
        'consistency': 0.15,
        'errors': -0.1  # negative weight
    }

    # Spurious adjustment (not applied)
    temp_adjust = {k: v * 1.1 for k, v in base_weights.items()}
    if any(v > 0.3 for v in temp_adjust.values()):
        pass  # dead logic

    # Correct weights returned
    return base_weights

# Evaluation logic with early exit red herring
def evaluate_performance(metrics, weights):
    score_components = {}

    # Real scoring
    score_components['latency'] = (100 - metrics['latency']) * weights['latency']
    score_components['success'] = (metrics['success'] * 100) * weights['success']
    score_components['volume'] = metrics['volume'] * weights['volume']
    score_components['consistency'] = metrics['consistency'] * 10 * weights['consistency']
    score_components['errors'] = (5 - metrics['errors']) * 10 * weights['errors']  # capped penalty

    # Fake component to mislead
    if metrics['errors'] == 0:
        score_components['bonus'] = 10
    else:
        # This branch runs but value not used
        fake_bonus = 5

    # Final aggregation
    total = sum(score_components[k] for k in ['latency', 'success', 'volume', 'consistency', 'errors'])

    # Early return distraction (never reached)
    if total > 100:
        return 100  # capping - unreachable due to math

    return total

# Unused recursive helper (decoy)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)

# Main execution flow
if __name__ == '__main__':
    # Collect system metrics
    metrics = collect_metrics()
    
    # Apply weighting scheme
    weights = apply_weights(metrics)
    
    # Evaluate overall performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")