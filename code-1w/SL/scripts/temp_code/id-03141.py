import itertools

def analyze_component(data, threshold=5.0):
    # Irrelevant analysis function (dead code path)
    return sum(x ** 0.5 for x in data if x > threshold)

def preprocess_signal(signal_stream):
    # Distractor: signal processing that isn't used later
    filtered = [x for x in signal_stream if abs(x) < 10]
    normalized = [(x + 1) / 2 for x in filtered]
    return [round(x, 3) for x in normalized]

def calculate_entropy(values):
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

def recursive_weight_adjust(w, level=3):
    # Misleading recursion – looks important but unused
    if level <= 0 or w > 100:
        return w
    return recursive_weight_adjust(w * 1.1 + 2, level - 1)

def generate_combinations(items):
    # Dead utility using itertools – not part of main logic
    return list(itertools.combinations(items, 2))

def evaluate_dimensional_metric(vals, mode='primary'):
    # Complex-looking transformation with red herring modes
    if mode == 'primary':
        base = sum(v ** 2 for v in vals) ** 0.5
        adjustment = len([v for v in vals if v < 0]) * 0.5
        return base - adjustment
    elif mode == 'auxiliary':
        return max(vals) - min(vals)
    else:
        return sum(vals) / len(vals)

def evaluate_performance(metrics, weights):
    # Core logic buried among distractions
    composite = 0.0
    
    # Real computation begins here — deeply nested and obscured
    temp_results = {}
    for key in metrics:
        if key == 'latency':
            # High nesting depth: 4 levels
            raw_val = metrics[key]
            weight_factor = weights.get(key, 1.0)
            if raw_val > 0:
                transformed = 100 / raw_val
                if transformed > 10:
                    capped = 10
                else:
                    capped = transformed
                temp_results[key] = capped * weight_factor
        elif key == 'throughput':
            t_val = metrics[key]
            w_t = weights.get(key, 1.0)
            bonus = 0
            if t_val > 80:
                bonus = 5
            temp_results[key] = (t_val / 10) * w_t + bonus
        elif key == 'stability':
            s_val = metrics[key]
            # Bit manipulation red herring
            binary_flags = bin(int(s_val))[2:]
            set_bits = binary_flags.count('1')
            temp_results[key] = s_val + (set_bits * 0.2)
    
    # Actual answer derived here
    raw_composite = sum(temp_results.values())
    
    # Final nonlinear adjustment
    if raw_composite >= 25:
        final_composite = raw_composite * 1.2
    else:
        final_composite = raw_composite * 0.9
    
    return int(round(final_composite))

# Main execution block
if __name__ == '__main__':
    # Irrelevant data structures
    sensor_log = [2.3, 7.8, 1.1, 9.2, 5.0, 6.7, 3.3]
    frequencies = [50, 60, 100, 120]
    device_states = ['active', 'idle', 'active', 'fault']
    
    # Unused combinatorics
    pairs = generate_combinations(frequencies)
    
    # Distractor: entropy calculation on unrelated data
    state_entropy = calculate_entropy(device_states)
    
    # Signal preprocessing (unused)
    noisy_signal = [-0.5, 1.2, 10.5, 0.8, -2.1, 15.0]
    cleaned_signal = preprocess_signal(noisy_signal)
    
    # Dictionary operations (some relevant, some misleading)
    system_metrics = {
        'latency': 20,      # ms
        'throughput': 95,   # ops/sec
        'stability': 8      # uptime score
    }
    
    weighting_schema = {
        'latency': 1.5,
        'throughput': 1.2,
        'stability': 1.0,
        'reliability': 0.8  # unused key
    }
    
    # Key statement
    final_score = evaluate_performance(system_metrics, weighting_schema)
    
    # Print result as required
    print(f"Result: {final_score}")