from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [15, 23, 18, 25, 30, 12, 22, 29, 17, 26, 31, 14, 24, 20, 27]

def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append('up')
        elif data[i] < data[i-1]:
            trends.append('down')
        else:
            trends.append('flat')
    return trends

def calculate_entropy(sequence):
    count = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for freq in count.values():
        p = freq / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_fallback_map(keys):
    # Irrelevant helper - dead code path
    fallback = {}
    for k in keys:
        fallback[k] = (k * 7 + 3) % 19
    return fallback

def validate_sequence(seq, threshold=20):
    # Misleading validation with unused logic
    above_threshold = [x for x in seq if x > threshold]
    below_threshold = [x for x in seq if x <= threshold]
    ratio = len(above_threshold) / len(below_threshold) if below_threshold else 0
    return ratio > 0.8

def filter_outliers(data, factor=1.5):
    # Decoy function - not actually used in main logic
    q1, q3 = sorted(data)[len(data)//4], sorted(data)[-len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def compute_weighted_average(values, weights=None):
    if not weights:
        weights = [1 for _ in values]
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight if total_weight else 0

def extract_key_metrics(stream):
    # Extract moving averages and volatility
    ma_3 = [sum(stream[i:i+3])/3 for i in range(len(stream)-2)]
    volatility = [abs(ma_3[i+1] - ma_3[i]) for i in range(len(ma_3)-1)]
    avg_volatility = sum(volatility) / len(volatility)
    peak = max(stream)
    base = stream[0]
    growth_rate = (peak - base) / base if base else 0
    return {
        'volatility': avg_volatility,
        'growth': growth_rate,
        'peak': peak,
        'length': len(stream)
    }

def process_performance(metrics, reference):
    # Core logic hidden among distractions
    score = 0
    score += int(metrics['volatility'] * 100)  # scaled impact
    score += int(metrics['growth'] * 50)
    
    # Bit manipulation red herring
    temp_flag = metrics['peak'] ^ 15
    if temp_flag & 1:
        score += 5
    else:
        score += 10
    
    # String-based decoy using slicing
    key_string = 'performance_anchor'
    anchor_value = sum(ord(c) for c in key_string[::3])  # every third char
    score += (anchor_value % 17)
    
    # Real but non-obvious contribution: length parity affects outcome
    if metrics['length'] % 2 == 0:
        score *= 2
    else:
        score += 20
    
    # Hidden conditional: depends on entropy of trend direction
    trends = analyze_trends(reference)
    entropy = calculate_entropy(trends)
    if entropy > 1.2:
        score = int(score * 1.1)
    
    # Unused branching - misleading control flow
    if metrics['peak'] > 25:
        adjustment = 0
        for i in range(5):
            adjustment += (i ** 2) % 7
        # This adjustment is never applied
    
    return score

# Irrelevant global mappings
event_codes = defaultdict(lambda: 'UNKNOWN')
event_codes.update({1: 'START', 2: 'PROGRESS', 3: 'COMPLETE'})

# Dummy data structure - distractor
system_state = {
    'status': 'active',
    'mode': 'production',
    'version': '3.7.1'
}

# Primary execution path
metrics = extract_key_metrics(telemetry_stream)
benchmark_data = telemetry_stream.copy()
final_score = process_performance(metrics, benchmark_data)

# Critical output - must print final_score
print(f"Target result: {final_score}")