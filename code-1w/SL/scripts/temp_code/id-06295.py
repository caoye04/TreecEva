import itertools

def analyze_sequence(data):
    # Irrelevant helper: computes sum of squares (not used in final logic)
    return sum(x ** 2 for x in data if x > 0)

def validate_input(entry):
    # Misleading validation that looks important but is bypassed
    if not isinstance(entry, list) or len(entry) == 0:
        return False
    return all(isinstance(x, int) for x in entry)

def transform_readings(readings):
    # Distractor transformation with unused result
    scaled = [r * 1.5 for r in readings]
    filtered = [s for s in scaled if s.is_integer()]
    return [int(f) for f in filtered]

def calculate_entropy(values):
    # Dead function - looks scientific but irrelevant
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def integrate_signals(a, b):
    # Unused signal merger with bitwise red herring
    result = 0
    for x, y in zip(a, b):
        result ^= (x & 7) + (y << 1)
    return result

def assess_stability(seq):
    # Another decoy metric using string methods on numbers (never called)
    seq_str = ''.join(map(str, seq))
    ups = seq_str.count('1') + seq_str.count('2')
    downs = seq_str.count('3') + seq_str.count('4')
    return abs(ups - downs)

def evaluate_performance(metrics, base):
    # Core logic hidden among distractions
    adjusted = {}
    for k, v in metrics.items():
        if k.startswith('err'):
            adjusted[k] = base['tolerance'] - abs(v - base['target'])
        elif k.endswith('_rate'):
            adjusted[k] = v * base['scaling']
    
    # Critical path: complex conditional aggregation
    temp_vals = []
    for val in adjusted.values():
        if val > 0:
            temp_vals.append(val ** 0.5)
        else:
            temp_vals.append(abs(val) / 2.5)
    
    # Key computation
    raw_total = sum(temp_vals)
    
    # Use of dictionary and itertools together as required
    pairs = list(itertools.combinations(temp_vals, 2))
    bonus = 0
    for p in pairs:
        if p[0] > 1 and p[1] > 1:
            bonus += 0.25
    
    # Final score calculation
    final_score = raw_total + bonus
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    # Real input data
    sensor_data = [3, 1, 4, 1, 5, 9, 2, 6]
    readings = [10, 20, 30, 40]
    
    # Irrelevant preprocessing
    processed = transform_readings(readings)
    entropy = calculate_entropy(sensor_data)
    
    # Decoy data structures
    system_state = {
        'status': 'active',
        'mode': 'debug',
        'flags': [0, 1, 1, 0],
        'checksum': 0xDEADBEEF
    }
    
    # String-based distractor
    mode_flag = system_state['mode'].upper().replace('E', '3')
    
    # Actual relevant data
    metrics = {
        'error_primary': 12,
        'error_secondary': 8,
        'throughput_rate': 4.5,
        'latency_rate': 6.2,
        'redundant_metric_x': 100,  # ignored due to naming
        'auxiliary_err': 15
    }
    
    baseline = {
        'target': 10,
        'tolerance': 5.0,
        'scaling': 1.2
    }
    
    # Unused recursive function (red herring)
    def track_decay(val, depth):
        if depth <= 0 or val < 1:
            return val
        return 0.9 * track_decay(val - 1, depth - 1)
    
    # Critical assignment
    final_score = evaluate_performance(metrics, baseline)