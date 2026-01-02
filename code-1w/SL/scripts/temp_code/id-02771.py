import itertools

def analyze_trend(values, threshold):
    """Irrelevant helper function for trend analysis."""
    if len(values) < 3:
        return False
    return sum(1 for a, b in zip(values, values[1:]) if b - a > threshold) > len(values) // 3

def preprocess_signal(signal, factor=0.9):
    """Distraction: signal smoothing that isn't used in final computation."""
    smoothed = [signal[0]]
    for x in signal[1:]:
        smoothed.append(smoothed[-1] * factor + x * (1 - factor))
    return smoothed

def generate_sequence(n):
    """Produces Fibonacci-like sequence as decoy data."""
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def validate_entry(record):
    """Red herring validation not affecting main logic."""
    if not record.get('active'):
        return False
    if record.get('flags', 0) > 5:
        return False
    return True

def calculate_entropy(data):
    """Unused complexity: computes entropy but never called in critical path."""
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    return -sum((count / total) * log2(count / total) for count in freq.values())

def core_transform(x, shift):
    """Relevant transformation used in filtering."""
    return (x * 3 + shift) % 17

def evaluate_performance(metrics, base):
    """Main logic buried among distractions."""
    # Irrelevant initialization
    temp_buffer = [0] * 10
    debug_mode = False
    max_outlier = None
    
    # Distractor: complex-looking but unused structure
    lookup_table = {i: (i ** 2) % 13 for i in range(20)}
    
    # Real logic begins
    adjusted = []
    for val in metrics:
        transformed = core_transform(val, base)
        if transformed > 10:
            adjusted.append(transformed * 2)
        elif transformed > 5:
            adjusted.append(transformed + 3)
        else:
            adjusted.append(transformed)
    
    # Filtering using itertools
    filtered = list(itertools.dropwhile(lambda x: x < 15, sorted(adjusted)))
    
    # More distractions
    outlier_count = 0
    temp_sum = 0
    for x in adjusted:
        if x > 25:
            outlier_count += 1
        temp_sum += x
    
    # Dead code branch (never executed due to logic)
    if len(filtered) > 100:
        fallback = sum(temp_buffer)
        return fallback // 2
    
    # Critical decision point
    if not filtered:
        fallback_value = sum(generate_sequence(8)) // 10
        return fallback_value
    
    # Actual result computation
    base_modifier = len([x for x in filtered if x % 2 == 0])
    primary_score = sum(filtered) // len(filtered)
    final_score = primary_score + base_modifier
    
    # This print is required per instructions
    print(f"Result: {final_score}")
    return final_score

# Main execution with decoy data
if __name__ == "__main__":
    # Irrelevant dataset
    sensor_log = [12, 45, 23, 67, 89, 11, 34]
    config_flags = {"debug": False, "version": 2, "strict": True}
    
    # Unused recursion example
    def recursive_checksum(data, depth=0):
        if depth >= 5 or len(data) == 1:
            return data[0] if data else 0
        mid = len(data) // 2
        left = recursive_checksum(data[:mid], depth+1)
        right = recursive_checksum(data[mid:], depth+1)
        return (left ^ right) + depth
    
    # Real input data
    metric_data = [4, 7, 2, 9, 5]
    baseline = 6
    
    # Trigger the key statement
    final_score = evaluate_performance(metric_data, baseline)