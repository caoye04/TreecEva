from collections import defaultdict, Counter
import math

# Simulated system telemetry data (irrelevant accumulation)
def collect_telemetry():
    data = defaultdict(list)
    for i in range(5):
        data['cpu'].append((i + 1) * 17 % 103)
        data['mem'].append((i + 2) * 29 % 89)
    return data

telemetry_log = collect_telemetry()

# Decoy function - looks important but unused in critical path
def analyze_anomaly_pattern(seq):
    count = 0
    for x in seq:
        if x % 11 == 0:
            count += 1
    return count

# Auxiliary statistical function with red herring variables
def moving_average(values, window=3):
    if len(values) < window:
        return [0]
    avg = []n    for i in range(len(values) - window + 1):
        avg.append(sum(values[i:i+window]) / window)
    temp_result = [x * 0.9 for x in avg]  # Distractor computation
    return avg

# Irrelevant combinatorics precomputation
def generate_pairs(elements):
    pairs = []
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            pairs.append((elements[i], elements[j]))
    return pairs

precomputed_pairs = generate_pairs([4, 8, 15, 16, 23, 42])

# Core logic disguised among distractions
baseline = {'latency': 120, 'throughput': 80, 'error_rate': 0.05}

metrics = {
    'latency': 145,
    'throughput': 87,
    'error_rate': 0.035,
    'jitter': 23.1,  # Unused field - distractor
    'retry_count': 4  # Unused field - distractor
}

# Secondary metrics with misleading intermediate scoring
def calculate_efficiency_ratio(x, y):
    if y == 0:
        return float('inf')
    return round((x ** 0.5) / y, 4)

efficiency = calculate_efficiency_ratio(metrics['throughput'], metrics['error_rate'])
backup_flag = efficiency > 1500  # False, but looks consequential

# Bit manipulation decoy - simulates low-level optimization
status_word = 0
for val in [metrics['latency'], metrics['throughput']]:
    status_word ^= int(val) & 0xFF
    status_word = (status_word << 1) | (status_word >> 7)

# Real evaluation logic buried in conditionals
def evaluate_performance(obs, base):
    score = 0
    
    # Latency: worse than baseline → penalty
    if obs['latency'] > base['latency']:
        score -= int((obs['latency'] - base['latency']) * 0.7)
    else:
        score += 10
        
    # Throughput: better than baseline → reward
    if obs['throughput'] > base['throughput']:
        bonus = int((obs['throughput'] - base['throughput']) * 1.3)
        score += bonus
    
    # Error rate improvement
    if obs['error_rate'] < base['error_rate']:
        improvement = (base['error_rate'] - obs['error_rate']) * 1000
        score += int(improvement * 2.5)
    
    # Hidden adjustment based on bit pattern of score so far
    temp = score & 0xF
    if temp % 3 == 0:
        score += 5  # Subtle deterministic boost
    
    # Final nonlinear scaling
    final = int(math.floor(score * (1.0 + 0.1 * (score > 0)) - 0.05 * abs(score)))
    
    # Dead code branch - looks like it might execute
    if score < 0 and status_word % 7 == 0:  # Never reached
        final *= -1
        
    return final

# Key execution point
temp_debug = moving_average([10, 15, 20, 25, 30])  # Distractor call
final_score = evaluate_performance(metrics, baseline)
Result: {final_score}