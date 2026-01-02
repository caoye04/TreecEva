import math

def analyze_component(x, threshold=0.5):
    if x < threshold:
        return int((x + 0.1) * 100)
    else:
        return int((1 - x) * 50)

# Irrelevant helper (decoy)
def compute_factorial(n):
    if n <= 1:
        return 1
    return n * compute_factorial(n - 1)

# Unused but plausible function
def normalize_vector(vec):
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Distractor data
temp_readings = [0.4, 0.7, 0.3, 0.9]
baseline_shift = 0.05
offset_correction = [x + baseline_shift for x in temp_readings]

# Core logic disguised among noise
def process_metrics(raw):
    result = {}
    for k, v in raw.items():
        if isinstance(v, list):
            cleaned = [x for x in v if x > 0.1]
            if len(cleaned) > 0:
                avg = sum(cleaned) / len(cleaned)
                result[k] = round(avg, 3)
        elif isinstance(v, dict):
            nested_val = sum(v.values()) / len(v)
            result[k] = math.sqrt(abs(nested_val - 0.5))
        else:
            result[k] = abs(v - 0.5) * 2
    return result

# Bit manipulation red herring
def encode_flag(value):
    flag = 0
    flag |= (value & 1) << 3
    flag |= (value & 2)
    flag ^= 5
    return flag  # Never actually used

def evaluate_performance(metrics, config):
    score = 0
    
    # Real logic starts here — buried in noise
    adjustment_map = {
        'latency': 0.8,
        'throughput': 1.2,
        'stability': 0.9,
        'memory': 1.1
    }
    
    # Irrelevant conditional branch
dummy_cache = {}
for i in range(3):
    dummy_cache[i] = compute_factorial(i+3)

    # Actual computation path
    intermediate = process_metrics(metrics)
    
    # More distractions
    outlier_filter = lambda x: x > 0.05
    filtered_keys = [k for k in intermediate.keys() if outlier_filter(intermediate[k])]
    
    # Real scoring logic
    for key in filtered_keys:
        base = intermediate[key]
        adj = adjustment_map.get(key, 1.0)
        contribution = base * adj
        if key == 'throughput':
            contribution *= 1.5  # Bonus weight
        elif key == 'latency':
            contribution *= 0.7  # Penalty factor
        score += contribution
    
    # Hidden correction using dictionary lookup
    penalty_table = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1}
    size_penalty = penalty_table.get(len(filtered_keys), 0)
    
    # Final transformation
    raw_final = (score * 100) - (size_penalty * 10)
    final_value = int(round(raw_final))
    
    # Dead code branch
    if final_value < 0:
        final_value = 0
    elif final_value > 1000:
        overflow_log = {'excess': final_value - 1000, 'flag': encode_flag(7)}
        final_value = 1000
    
    return final_value

# Input data — some values trigger logic, others don't
metrics = {
    'latency': [0.4, 0.6, 0.3],
    'throughput': [0.8, 0.9, 0.75],
    'stability': 0.85,
    'memory': {'usage': 0.6, 'peak': 0.9},
    'debug_mode': False
}

benchmark_data = {
    'version': '2.1',
    'calibration': [0.1, 0.2],
    'active': True
}

# Execution point of interest
final_score = evaluate_performance(metrics, benchmark_data)
print(f"Result: {final_score}")