def analyze_efficiency(data, config):
    temp_result = 0
    for k, v in data.items():
        if len(k) % 2 == 0:
            temp_result += v * 1.5
        else:
            temp_result -= v * 0.5
    return temp_result

# Irrelevant helper function (dead path)
def deprecated_calculate_legacy(x):  
    return (x ** 2 + 3 * x + 1) // 2

# Misleading metric computation
counter_weights = {'A': 3, 'B': 1, 'C': 4, 'D': 1}
shift_factor = 7
offset_lookup = {i: i**2 for i in range(10)}

# Core logic disguised among noise
def transform_inputs(raw_values):
    transformed = []
    for val in raw_values:
        if val < 0:
            transformed.append(abs(val) << 1)
        elif val == 0:
            transformed.append(9)
        else:
            transformed.append(val ^ 5)
    return set(transformed)  # Use of set operation

raw_data_stream = [12, -3, 0, 8, -7]
processed_set = transform_inputs(raw_data_stream)
decoy_sum = sum(x * 2 for x in processed_set if x > 5)

# Fake performance indicator (distractor)
baseline_metrics = {
    'latency': 42,
    'throughput': None,
    'errors': [],
    'version': 'old'
}

config_settings = {'mode': 'strict', 'scale': 2}
data_payload = {'alpha': 10, 'beta': 20, 'gamma': 30}

intermediate = analyze_efficiency(data_payload, config_settings)
synthetic_offset = offset_lookup[len(processed_set)] if len(processed_set) in offset_lookup else 0

# Main evaluation logic buried in complexity
def evaluate_performance(metrics, benchmarks):
    score = 0
    
    # Dictionary-based scoring rules
    rules = {
        'alpha': lambda x: x * 1.1,
        'beta': lambda x: x + 5 if x > 15 else x - 3,
        'gamma': lambda x: x ** 0.5 * 2
    }
    
    for key, value in metrics.items():
        if key in rules:
            score += rules[key](value)
    
    # Conditional expression with misleading alternative branch
    bonus = 10 if len(benchmarks) > 3 and 'gamma' in metrics else 0
    
    # Bitwise manipulation red herring
    magic_mask = 0b1101
    decoy_flag = synthetic_offset & magic_mask
    
    # Real adjustment using set intersection (critical but hidden)
    critical_keys = {'alpha', 'beta', 'gamma'}
    present = critical_keys & benchmarks  # Set intersection
    score += len(present) * 2.5
    
    # Final adjustment based on earlier intermediate result
    score += intermediate / 10
    
    return int(score)  # Ensure integer result

# Unused variables to increase interference
threshold_limit = 1000
dummy_cache = [0] * 100
legacy_mode = False

# Key data structure
benchmarks_available = {'alpha', 'beta', 'delta', 'gamma'}

# Critical execution point
final_score = evaluate_performance(data_payload, benchmarks_available)
print(f"Result: {final_score}")