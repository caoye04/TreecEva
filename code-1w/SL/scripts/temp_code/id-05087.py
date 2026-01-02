def analyze_efficiency(data, threshold=0.75):
    """Irrelevant efficiency analysis function (distractor)"""
    if not data:
        return 0
    avg = sum(data) / len(data)
    filtered = [x for x in data if x > threshold]
    return len(filtered) / len(data)


def compute_entropy(sequence):
    """Distractor: computes symbol entropy (not used in final result)"""
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Irrelevant constants (red herrings)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
RETRY_LIMIT = 3

# Simulated system metrics (some relevant, some not)
metrics = {
    'response_time': [0.12, 0.15, 0.11, 0.21, 0.13],
    'throughput': [88, 92, 90, 85, 95],
    'errors': [1, 0, 2, 0, 1],
    'cpu_load': [65, 70, 72, 68, 75],
    'memory_usage': [420, 435, 450, 440, 460]
}

baseline = {
    'rt_avg': 0.14,
    'tp_avg': 90,
    'error_tol': 1.5,
    'cpu_max': 70
}

# Distractor: unused complex data structure
system_log = [
    {'timestamp': '13:00', 'event': 'start', 'load': 60},
    {'timestamp': '13:05', 'event': 'query', 'load': 68},
    {'timestamp': '13:10', 'event': 'error', 'load': 72},
    {'timestamp': '13:15', 'event': 'retry', 'load': 65}
]

# Decoy function that looks important but is never called
def generate_diagnostic_report(logs, config=None):
    report = {"issues": [], "status": "stable"}
    for entry in logs:
        if entry['load'] > 70 and entry['event'] == 'error':
            report['issues'].append("High load during error")
    report['issue_count'] = len(report['issues'])
    return report

# Complex distractor computation with slicing and string ops
raw_trace = "a1b2c3d4e5f6g7h8i9j10"
digits = ''.join([c for c in raw_trace if c.isdigit()])
segments = [digits[i:i+2] for i in range(0, len(digits), 2)]
checksum = sum(int(s) for s in segments if len(s) == 2 and s != '10')

# Unused recursive function (dead code path)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Key function - evaluates performance using subtle logic chain
def evaluate_performance(met, base):
    # Step 1: response time compliance
    rt_data = met['response_time']
    rt_avg = sum(rt_data) / len(rt_data)
    rt_good = sum(1 for t in rt_data if t <= base['rt_avg'])
    
    # Step 2: throughput targets
    tp_data = met['throughput']
    tp_trend = [tp_data[i+1] - tp_data[i] for i in range(len(tp_data)-1)]
    tp_increasing = sum(1 for diff in tp_trend if diff > 0)
    
    # Step 3: error rate analysis
    errors = met['errors']
    error_rate = sum(errors) / len(errors)
    
    # Step 4: cpu volatility
    cpu_data = met['cpu_load']
    high_cpu_periods = sum(1 for load in cpu_data if load > base['cpu_max'])
    
    # Step 5: memory trend analysis (irrelevant to final score)
    mem_data = met['memory_usage']
    mem_growth = mem_data[-1] - mem_data[0]
    
    # Step 6: conditional scoring with nested logic
    score_components = []
    
    # Sub-scoring: response time quality
    if rt_avg <= base['rt_avg']:
        score_components.append(25)
    else:
        penalty = int((rt_avg - base['rt_avg']) * 100 * 5)
        score_components.append(max(10, 25 - penalty))
    
    # Sub-scoring: throughput consistency
    if tp_increasing >= 3:
        score_components.append(20)
    elif tp_increasing >= 1:
        score_components.append(15)
    else:
        score_components.append(10)
    
    # Sub-scoring: error tolerance
    if error_rate <= base['error_tol']:
        bonus = 10 if errors[0] == 0 else 5
        score_components.append(20 + bonus)
    else:
        score_components.append(15)
    
    # Sub-scoring: CPU stability
    if high_cpu_periods == 0:
        score_components.append(25)
    elif high_cpu_periods == 1:
        score_components.append(20)
    else:
        reduction = min(15, high_cpu_periods * 5)
        score_components.append(25 - reduction)
    
    # Final calculation - sum with adjustment
    raw_score = sum(score_components)
    
    # Critical adjustment based on initial response success
    if errors[0] == 0 and rt_data[0] <= 0.12:
        raw_score += 10
    
    # Apply decay if memory growth too high (but this condition is never met)
    if mem_growth > 50:
        raw_score -= 5
    
    return raw_score

# Additional red herring: string processing with dictionary
config_profile = "PERF_HIGH_THROUGHPUT"
flags = {
    'dynamic_scaling': True,
    'prefetch_enabled': config_profile.startswith('PERF'),
    'compression': config_profile.endswith('THROUGHPUT'),
    'mode': config_profile.lower().replace('_', '-')
}

# Distractor: bit manipulation chain
flag_value = 0
for i, key in enumerate(sorted(flags.keys())):
    if flags[key] and isinstance(flags[key], bool):
        flag_value |= (1 << i)

# Another decoy variable
encoded_tag = hex(flag_value ^ 0xAA)[2:].upper()

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Target result: {final_score}")