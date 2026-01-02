from collections import defaultdict, Counter
import math

# Irrelevant utility function (dead code)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

def calculate_entropy(labels):
    counts = Counter(labels)
    total = len(labels)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Distractor data
log_data = ['error', 'info', 'warning', 'error', 'info', 'info']
label_entropy = calculate_entropy(log_data)  # Misleading intermediate result

# Real problem: Performance metric aggregation with red herrings
def evaluate_component(stability, throughput, latency_ms):
    score = 0
    if stability > 0.9:
        score += 30
        if throughput > 1000:
            score += 40
            if latency_ms < 50:
                score += 30
            elif latency_ms < 100:
                score += 15
        else:
            score += 10
    else:
        score += 10
        if latency_ms < 30:
            score += 25  # Rare path, misleading
    return score

def analyze_pattern(seq):
    # Unused complex analysis (red herring)
    transitions = defaultdict(int)
    for i in range(len(seq) - 1):
        transitions[(seq[i], seq[i+1])] += 1
    return dict(transitions)

def extract_features(raw):
    features = []
    for item in raw:
        if isinstance(item, str):
            features.append(len(item.strip()))
        elif isinstance(item, (int, float)):
            features.append(abs(item) % 100)
    return features

def validate_inputs(data, weights):
    # Superficial validation with side effects
    issues = []
    if len(data) != len(weights):
        issues.append('length_mismatch')
    for i, (d, w) in enumerate(zip(data, weights)):
        if d < 0 and w < 0:
            issues.append(f'negative_pair_{i}')
    # Returns useless info
    return len(issues) == 0, issues

def process_metrics(data, weights):
    # Core logic buried in distractions
    temp_results = []
    component_scores = []
    
    # Real processing mixed with noise
    for i, (d, w) in enumerate(zip(data, weights)):
        if i % 3 == 0:
            # Apply non-linear transformation on every 3rd element
            transformed = math.log(d + 1) * (w ** 0.5)
            temp_results.append(round(transformed, 4))
        elif i % 3 == 1:
            shifted = (d * w) / (i + 1)
            temp_results.append(shifted)
        else:
            temp_results.append(d + w)
    
    # Actual aggregation
    base_sum = sum(temp_results)
    adjustment_factor = 1.0
    
    # Red herring conditional chain
    if base_sum > 100:
        adjustment_factor *= 0.9
    elif base_sum > 50:
        adjustment_factor *= 1.1
        # Nested distraction
        dummy_list = [x for x in range(5) if x % 2 == 0]
        _ = [math.sin(math.pi * y / 4) for y in dummy_list]  # No effect
    else:
        adjustment_factor *= 1.2
    
    # Critical evaluation call
    performance_flag = evaluate_component(0.92, 1200, 45)
    if performance_flag >= 70:
        adjustment_factor *= 1.25
    
    # Main computation
    final_score = int(base_sum * adjustment_factor) + performance_flag
    
    # Dead code block (never reached due to logic)
    if final_score < 0:
        recovery = extract_features(["retry", "fallback"])
        final_score = sum(recovery)
    
    # Irrelevant string manipulation
    status_msg = "System nominal"
    padded = status_msg.ljust(20, '.').upper()
    
    return final_score

# Global decoy variables
decoy_matrix = [[i*j for j in range(3)] for i in range(3)]
phantom_total = sum(sum(row) for row in decoy_matrix)

# Input data (partially obscured meaning)
data = [85, 105, 70, 95, 110, 65]
weights = [1.2, 0.8, 1.5, 0.9, 1.1, 1.3]

# Trigger main logic
def run_pipeline():
    valid, _ = validate_inputs(data, weights)
    if not valid:
        return -1
    # Real execution point
    final_score = process_metrics(data, weights)
    print(f"Result: {final_score}")
    return final_score

result = run_pipeline()