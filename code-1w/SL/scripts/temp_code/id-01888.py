def analyze_text_patterns(text_data, pattern):
    char_freq = {}
    for c in text_data:
        char_freq[c] = char_freq.get(c, 0) + 1
    matches = [i for i in range(len(text_data)) if text_data.startswith(pattern, i)]
    return len(matches), char_freq

# Irrelevant utility function (dead code path)
def encrypt_shift(s, shift=3):
    return ''.join(chr((ord(c) - 97 + shift) % 26 + 97) if c.isalpha() else c for c in s.lower())

# Misleading data transformation
text_corpus = "abccbaabcdefg"
decoy_result = encrypt_shift(text_corpus, 5)

# Simulated system metrics with red herring variables
metrics = {
    'throughput': 420,
    'latency': 120,
    'errors': 3,
    'retries': 7,
    'cache_hits': 91,
    'bandwidth': 88,
    'active_sessions': 15
}

baseline = {
    'throughput': 400,
    'latency': 100,
    'errors': 5,
    'retries': 10
}

# Distractor: unused but plausible calculation
aggregate_risk = sum([v**2 for v in metrics.values() if v > 50]) // 100

# Real logic buried in noise
def normalize_metric(value, base):
    return (value - base) / base if base != 0 else 0

def calculate_deviation(data, base):
    dev = 0
    for k, v in base.items():
        if k in data:
            dev += abs(normalize_metric(data[k], v))
    return dev

def track_anomalies(log_string, threshold=2):
    counts = {}
    for word in log_string.split():
        clean_word = word.strip('.,!').lower()
        counts[clean_word] = counts.get(clean_word, 0) + 1
    anomalies = {k: v for k, v in counts.items() if v >= threshold}
    return len(anomalies)

# More decoys
log_sample = "Error occurred in module A. Retry initiated. Error occurred again."
phantom_alerts = track_anomalies(log_sample, 2)

# Core evaluation logic hidden among distractions
def evaluate_performance(m, b):
    # Critical computation path (3 levels of nesting)
    base_keys = set(b.keys())
    matched_keys = set(k for k in m.keys() if k in b)
    if not matched_keys:
        return -1
    
    score_components = []
    for key in matched_keys:
        ref = b[key]
        val = m[key]
        if ref == 0:
            continue
        delta = abs(val - ref) / ref
        weight = 1
        if key == 'throughput':
            weight = 1.5
        elif key == 'latency':
            weight = 2.0
        elif key == 'errors':
            weight = 3.0
        score_components.append(delta * weight)
    
    raw_score = sum(score_components)
    adjustment = 0
    
    # Hidden conditional branch affecting result
    if len(matched_keys) == 3:
        adjustment = 0.5
        temp_slice = [1, 2, 3, 4, 5][1:4]
        # Use of slicing and list comprehension as required
        adjustment += sum([x**2 for x in temp_slice]) / 100.0
    
    final_raw = raw_score - adjustment
    
    # Final mapping to integer score
    return int((10 - final_raw) * 10)

# Trigger point of interest
final_score = evaluate_performance(metrics, baseline)

# Irrelevant post-processing
summary_tag = f"Report_{'_'.join([k[:2].upper() for k in metrics.keys()][:3])}"
buffer_zone = summary_tag[::-1]  # string slicing distraction

# Output must be printed exactly once
print(f"Result: {final_score}")