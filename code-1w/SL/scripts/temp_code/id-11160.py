def analyze_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_freq[:3]]

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from math import log2
    total = sum(data)
    entropy = 0
    for count in data:
        if count > 0:
            p = count / total
            entropy -= p * log2(p)
    return round(entropy, 4)

# Unused transformation (dead code path)
def transform_sequence(seq):
    result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            result.append(val ** 2)
        else:
            result.append(val // 2)
    return result

# Misleading metric calculation with red herring variables
system_flags = {"debug": True, "tracing": False, "optimize": True}
base_weights = [0.1, 0.3, 0.4, 0.2]
dummy_cache = {i: i * i for i in range(100)}  # Distractor: looks important but unused

# Simulated system metrics log with multiple irrelevant fields
metrics_log = [
    {'timestamp': 1678886400, 'module': 'net', 'latency': 45, 'retries': 0, 'active': True},
    {'timestamp': 1678886401, 'module': 'io', 'latency': 120, 'retries': 1, 'active': True},
    {'timestamp': 1678886402, 'module': 'comp', 'latency': 23, 'retries': 0, 'active': True},
    {'timestamp': 1678886403, 'module': 'io', 'latency': 310, 'retries': 2, 'active': True},
    {'timestamp': 1678886404, 'module': 'net', 'latency': 67, 'retries': 1, 'active': True},
]

# Auxiliary lookup map (partially used)
module_severity = {
    'net': 1,
    'io': 2,
    'comp': 3,
    'gpu': 4
}

# Bit manipulation decoy (looks related but not directly used in final logic)
current_state = 0b1101
for entry in metrics_log:
    current_state ^= hash(entry['module']) & 0b1111  # Side effect only, not affecting output

# Core evaluation logic buried among distractions
def evaluate_performance(log):
    total_latency = 0
    total_retries = 0
    module_count = {}
    
    for record in log:
        if record['active']:
            total_latency += record['latency']
            total_retries += record['retries']
            mod = record['module']
            module_count[mod] = module_count.get(mod, 0) + 1
    
    # Real computation hidden among noise
    avg_latency = total_latency / len(log) if log else 0
    penalty = 0
    
    # Apply severity-weighted penalty based on retries per module
    for record in log:
        if record['retries'] > 0:
            penalty += record['retries'] * module_severity.get(record['module'], 0)
    
    # Secondary adjustment based on frequency of module usage
    max_usage = max(module_count.values()) if module_count else 1
    usage_bonus = len([m for m in module_count.values() if m == max_usage]) * 5
    
    # Final score computed from multiple reasoning steps
    raw_score = avg_latency + penalty * 10 - usage_bonus
    normalized = abs(raw_score * 1.5)  # Final transformation
    
    # Dead branch (never taken, misleading)
    if system_flags.get('tracing') and len(dummy_cache) > 200:
        normalized += 100  # Never executed
    
    return int(normalized)

# Key execution point
final_score = evaluate_performance(metrics_log)
print(f"Result: {final_score}")