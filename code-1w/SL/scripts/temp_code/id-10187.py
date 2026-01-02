import math

# Simulated sensor array diagnostics with interference

def collect_sensor_readings():
    raw_signals = [2.1, 3.5, 4.8, 5.0, 6.3, 7.2, 8.1, 9.5]
    noise_floor = 1.3
    adjusted = [sig - noise_floor for sig in raw_signals]
    return adjusted

def compute_entropy(values):
    # Irrelevant entropy calculation (unused later)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def generate_fibonacci(n):
    # Distractor: Unused Fibonacci sequence generator
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def validate_checksum(data):
    # Dead path: checksum not used in main logic
    return sum(data) % 7 == 0

def filter_outliers(stream, limit=7.0):
    # Partially relevant but ultimately bypassed filtering
    return [x for x in stream if x < limit]

def derive_metrics(readings):
    # Complex transformation with red herring variables
    squared = [x**2 for x in readings]
    shifted = [s - 2.5 for s in squared]
    normalized = [abs(s) % 4.0 for s in shifted]
    
    # Decoy aggregation
    avg_sq = sum(squared) / len(squared)
    peak = max(normalized)
    
    # Actual relevant metric embedded
    product_factor = 1
    for n in normalized[:5]:
        if n > 1.5:
            product_factor *= int(n)
    
    # Red herring return components
    return {
        'peak': peak,
        'average_squared': avg_sq,
        'factor': product_factor,
        'size': len(normalized),
        'dummy_flag': False
    }

def merge_sets(config_a, config_b):
    # Set operations (required Python feature)
    set_a = {x % 5 for x in config_a}
    set_b = {x % 3 for x in config_b}
    union_result = set_a | set_b
    intersection_size = len(set_a & set_b)
    return sorted(union_result), intersection_size

def analyze_pattern(dataset, criteria):
    # Core logic buried in distractions
    base_score = 0
    
    # String manipulation decoy
    status_log = "diagnostic_pass_ok ready_stable"
    tokens = status_log.split('_')
    if tokens[0] == "diagnostic" and tokens[2] == "ok":
        base_score += 5
    
    # Counting/grouping red herring
    category_count = {}
    for item in tokens:
        category_count[item] = category_count.get(item, 0) + 1
    
    # Real logic hidden in conditional chain
    threshold_met = 0
    for key, value in criteria.items():
        if key.startswith('t') and value > 3.0:
            threshold_met += 1
    
    if threshold_met >= 2:
        base_score += 17
    
    # Bit manipulation distractor
    flag = 0b1010
    flag ^= 0b1100
    flag <<= 2
    
    # Critical dependency on derived metrics
    metrics = derive_metrics(dataset)
    base_score += metrics['factor']
    
    # Final determination
    adjustment = len(merge_sets([1,2,3], [3,4,5])[0])
    return base_score * adjustment

# Main execution with misleading setup
if __name__ == "__main__":
    # Collect data
    collected_data = collect_sensor_readings()
    
    # Generate unused sequences
    fib_sequence = generate_fibonacci(10)
    entropy_value = compute_entropy(collected_data)
    
    # Create thresholds with decoy entries
    thresholds = {
        't1': 4.2,
        't2': 3.8,
        't3': 2.1,  # Below cutoff
        'debug_mode': False,
        'version': 1.0
    }
    
    # Apply filters that are not used
    cleaned_data = filter_outliers(collected_data, 6.0)
    valid = validate_checksum(collected_data)
    
    # Key computation
    final_diagnostic = analyze_pattern(collected_data, thresholds)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")