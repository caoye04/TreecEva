import itertools

def analyze_pattern(seq):
    # Irrelevant helper function – never called
    return [x ** 2 for x in seq if x % 2 == 0]

def unused_transformation(values):
    # Dead code path – looks useful but unused
    temp = 0
    for v in values:
        temp += v * (v & (v - 1))  # Bitwise red herring
    return temp

def evaluate_threshold(signal, limit=50):
    # Misleading intermediate computation
    count = 0
    for s in signal:
        if s > limit and s % 3 == 0:
            count += 1
    return count * 2  # Distractor logic

def filter_outliers(stream, low=10, high=90):
    # Looks important but not used in final calculation
    return [x for x in stream if low <= x <= high]

def compute_moving_average(series, window=3):
    # Unused but plausible preprocessing step
    averages = []
    for i in range(len(series) - window + 1):
        averages.append(sum(series[i:i+window]) / window)
    return averages

def extract_features(dataset):
    # Partially relevant: only one output is used later
    total_entries = len(dataset)
    sum_squares = sum(x**2 for x in dataset)
    max_value = max(dataset)
    min_value = min(dataset)
    range_val = max_value - min_value
    
    # Decoy statistics
    even_count = sum(1 for x in dataset if x % 2 == 0)
    peak_moments = [i for i, x in enumerate(dataset) if x == max_value]
    
    # Only this returned value matters
    return {'sum_sq': sum_squares, 'total': total_entries}

def process_metrics(raw_data, importance_weights):
    # Core logic buried in distractions
    
    # Real data processing begins
    stats = extract_features(raw_data)
    
    # Irrelevant transformation chain
    shifted = [x - 5 for x in raw_data if x > 5]
    paired = list(zip(shifted[:-1], shifted[1:]))
    diff_pairs = [a - b for a, b in paired]
    
    # Fake accumulation using itertools
    accumulated = list(itertools.accumulate(diff_pairs, func=lambda x, y: x + y * 0.5))
    if len(accumulated) > 10:
        accumulated = accumulated[:10]
    
    # Real logic starts here — obscurely dependent on earlier result
    base_metric = stats['sum_sq'] / (stats['total'] + 1e-8)
    
    # Weighted adjustment with decoy dictionary lookups
    modifier_map = {i: w * 1.5 for i, w in enumerate(importance_weights)}
    extra_offset = 0
    for idx, weight in enumerate(importance_weights):
        if idx % 2 == 0:
            extra_offset += modifier_map[idx] * 0.1
    
    # Actual core computation
    adjusted_base = base_metric * importance_weights[0]
    penalty = len([x for x in raw_data if x < 15]) * 2.5
    bonus = sum(1 for x in raw_data if x > 75) * 1.75
    
    # Final score built from multiple sources, but only some are real
    intermediate = adjusted_base + bonus - penalty + extra_offset
    
    # Key obfuscation: final correction using enumerate to seem complex
    for i, val in enumerate(raw_data):
        if i % 4 == 0 and val > 20:
            intermediate += 0.25
    
    # This is the actual answer variable
    final_score = round(intermediate, 4)
    
    # Never executed — dead branch
    if False:
        fallback = sum(accumulated) / len(accumulated)
        final_score = fallback
    
    return final_score

# Main execution context
if __name__ == '__main__':
    # Input data with meaningful structure
    sensor_readings = [23, 45, 12, 67, 89, 9, 34, 56, 78, 11, 29, 83, 91, 4, 68]
    
    # Weights – only first element matters
    feature_importance = [0.85, 0.12, 0.34, 0.56, 0.78]  # Last four are red herrings
    
    # Dummy preprocessing that does nothing
    filtered_data = filter_outliers(sensor_readings, 5, 95)
    evaluated_peaks = evaluate_threshold(sensor_readings, 40)
    smoothed_signal = compute_moving_average(filtered_data, 2)
    
    # Actual key computation
    final_score = process_metrics(sensor_readings, feature_importance)
    
    # Output required format
    print(f"Result: {final_score}")