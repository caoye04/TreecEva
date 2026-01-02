from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def calculate_network_latency(nodes, edges):
    return sum(len(edge) for edge in edges) % 7

def preprocess_data(raw):
    # Distractor: complex but unused transformation
    cleaned = [x for x in raw if x > 0]
    stats = defaultdict(int)
    for val in cleaned:
        stats['count'] += 1
        stats['sum'] += val
    return stats

# Unused advanced bit manipulation (red herring)
def encrypt_key(n):
    n = ((n << 3) & 0xff) | (n >> 5)
    n ^= 0xa5
    return n % 19

# Real logic begins here — subtle and buried among noise
def analyze_trend(sequence):
    trend = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend += 1
        elif sequence[i] < sequence[i-1]:
            trend -= 1
    return trend

def compute_entropy(values):
    freqs = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Core metric evaluation with multiple layers
baseline = {'stability': 0.7, 'efficiency': 120, 'consistency': 3}

def evaluate_performance(metrics, baseline):
    # Step 1: Extract relevant features
    stability_diff = abs(metrics.get('stability') - baseline['stability'])
    efficiency_ratio = metrics.get('efficiency') / baseline['efficiency']
    
    # Step 2: Hidden dependency on trend analysis
    history = [metrics['log'][i]['value'] for i in range(len(metrics['log']))]
    trend_strength = analyze_trend(history)
    
    # Step 3: Entropy-based consistency check
    recent_values = [entry['value'] for entry in metrics['log'][-5:]]
    value_entropy = compute_entropy(recent_values)
    
    # Step 4: Bit manipulation red herring (appears important but isn't used)
    secret_code = 0b110101
    masked = (secret_code ^ 0b1011) & 0b1111
    dummy_metric = encrypt_key(masked + 44)  # Misleading call
    
    # Step 5: Weighted aggregation
    score_a = (1 - stability_diff) * 40
    score_b = min(efficiency_ratio, 1.5) * 30
    
    # Step 6: Conditional adjustment based on trend
    if trend_strength > 0:
        bonus = 15
    elif trend_strength == 0:
        bonus = 5
    else:
        bonus = -10
    
    # Step 7: Penalty from entropy (higher entropy = less predictable = penalty)
    entropy_penalty = max(0, (value_entropy - 2.0)) * 10
    
    # Step 8: Final composition
    base = score_a + score_b + bonus
    adjusted = base - entropy_penalty
    
    # Step 9: Clamp to valid range
    final = max(0, min(100, int(round(adjusted))))
    
    # Step 10: Irrelevant rounding debug
    debug_info = {"raw": adjusted, "clamped": final}
    
    return final

# Simulated input data with distractors
raw_input = [-5, 0, 3, 8, 12]
unused_stats = preprocess_data(raw_input)

# Actual execution context
metrics = {
    'stability': 0.65,
    'efficiency': 180,
    'log': [
        {'ts': 1, 'value': 10},
        {'ts': 2, 'value': 12},
        {'ts': 3, 'value': 15},
        {'ts': 4, 'value': 14},
        {'ts': 5, 'value': 16},
        {'ts': 6, 'value': 18},
        {'ts': 7, 'value': 20}
    ],
    'meta': {
        'version': '2.1',
        'author': 'sysbot_3000'
    }
}

# Dead computation — looks important but doesn't affect result
latency_test = calculate_network_latency(['A','B'], [('A','B'), ('B','C')])

final_score = evaluate_performance(metrics, baseline)
print(f"Target result: {final_score}")