import itertools

# Simulated system log analyzer with distractors
def analyze_failures(records):
    critical = [r for r in records if r['level'] == 'CRITICAL']
    timeouts = [r for r in records if 'timeout' in r['msg']]
    return len(critical) + len(timeouts) * 2

# Irrelevant helper - dead code path
def deprecated_aggregator(data):
    return sum(x ** 0.5 for x in data if x > 0) // len(data)

# Real processing function
def normalize(values):
    total = sum(values)
    if total == 0:
        return [0] * len(values)
    return [v / total for v in values]

def detect_anomalies(stream):
    anomalies = 0
    window = []
    for val in stream:
        window.append(val)
        if len(window) > 3:
            window.pop(0)
        if len(window) == 3 and window[0] < window[1] > window[2]:
            anomalies += 1
    return anomalies

def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / len(data)
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Decoy metrics (not used in final result)
decoys = {
    'cache_miss': 127,
    'retry_count': 43,
    'latency_outlier': 9,
    'deprecated_flag': True
}

# Input data
log_data = [
    {'timestamp': 1001, 'level': 'INFO', 'msg': 'user login'},
    {'timestamp': 1005, 'level': 'WARNING', 'msg': 'high memory'},
    {'timestamp': 1010, 'level': 'CRITICAL', 'msg': 'timeout error'},
    {'timestamp': 1015, 'level': 'INFO', 'msg': 'data sync'},
    {'timestamp': 1020, 'level': 'CRITICAL', 'msg': 'disk full'},
    {'timestamp': 1025, 'level': 'ERROR', 'msg': 'timeout error'},
    {'timestamp': 1030, 'level': 'INFO', 'msg': 'service restart'}
]

# Performance counters (some irrelevant)
counters = {
    'requests': [120, 135, 130, 145, 160, 155, 170],
    'errors': [3, 5, 4, 8, 12, 10, 14],
    'queue_depth': [10, 25, 18, 40, 35, 50, 45]
}

# Weights for scoring (used in final calculation)
weights = {
    'failure_weight': 3.5,
    'anomaly_weight': 1.2,
    'entropy_weight': 0.8
}

# Distractor: unused complex structure
struct = list(itertools.combinations([1, 2, 3, 4], 3))
struct_filtered = [s for s in struct if s[0] % 2 == 0]

# Auxiliary transformation (partially relevant)
request_anomalies = detect_anomalies(counters['requests'])
failure_count = analyze_failures(log_data)
entropy_metric = compute_entropy(counters['errors'])

# Normalize counters (distractor usage)
norm_requests = normalize(counters['requests'])
norm_errors = normalize(counters['errors'])

# Intermediate decoy score
interim_score = (sum(norm_requests[:4]) * 100) - (len(struct_filtered) * 7)

# Key processing function
def process_metrics(logs, w):
    base_failures = analyze_failures(logs)
    stream = [len(record['msg']) for record in logs]
    anomaly_count = detect_anomalies(stream)
    error_pattern_entropy = compute_entropy([len(r['msg']) % 5 for r in logs])
    
    # Actual score computation
    score = 0
    score += base_failures * w['failure_weight']
    score += anomaly_count * w['anomaly_weight']
    score += error_pattern_entropy * w['entropy_weight']
    
    # Red herring: this line looks important but doesn't affect output
    score += decoys['cache_miss'] * 0.01  
    
    return int(round(score))

# Final execution point
final_score = process_metrics(log_data, weights)

# Target result
print(f"Target result: {final_score}")