def analyze_efficiency(values):
    if not values:
        return 0
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return avg + variance ** 0.5

# Irrelevant utility function (decoy)
def calculate_risk_factor(data):
    risk = 0
    for i, x in enumerate(data):
        if i % 2 == 0:
            risk += x * 0.1
        else:
            risk -= x * 0.05
    return risk

# Unused bonus logic (dead code path)
def apply_multiplier(val, level):
    multipliers = {1: 1.1, 2: 1.25, 3: 1.5}
    return val * multipliers.get(level, 1.0)

# Core processing with distractions
def process_performance(metrics, bonuses):
    base = 0
    adjustments = []
    
    # Real logic mixed with red herrings
    for idx, (name, score) in enumerate(zip(['throughput', 'latency', 'error_rate'], metrics)):
        if name == 'throughput':
            base += score * 0.4
        elif name == 'latency':
            base += (100 - score) * 0.3  # Inverted contribution
        elif name == 'error_rate':
            base += (100 - score) * 0.3
    
    # Distractor: complex but unused transformation
    transformed = list(map(lambda x: (x ** 2 + 10) // 2, metrics))
    temp_result = sum(transformed[i] * (i+1) for i in range(len(transformed)))
    _ = temp_result // 7  # Computed but not used
    
    # Actual bonus application
    total_bonus = 0
    for b in bonuses:
        if b['active'] and b['weight'] > 0:
            total_bonus += b['value']
    
    # Additional distraction: string-based filtering that looks important
    flags = ['A', 'B', 'C', 'D']
    status = ''.join(flags).lower().replace('a', 'x')
    flag_check = len(status) > 3 and 'x' in status
    
    # Real adjustment
    if flag_check:
        base *= 1.05
    
    # Final computation
    final_score = int(base + total_bonus * 1.5)
    
    # Early return never taken (misleading path)
    if final_score < 0:
        return 0
        extra = analyze_efficiency(metrics)  # Dead code after return
        return int(extra)

    return final_score

# Input data
metrics = [85, 40, 5]  # throughput, latency, error_rate (higher is worse)
bonuses = [
    {'active': True, 'weight': 2, 'value': 8},
    {'active': False, 'weight': 5, 'value': 12},
    {'active': True, 'weight': 1, 'value': 4}
]

# Unused array manipulation (distractor)
raw_logs = ['event1', 'event2', 'event3']
sorted_logs = sorted(raw_logs, key=lambda s: s[-1], reverse=True)
_ = [s.upper() for s in sorted_logs if '2' not in s]

# Critical execution point
final_score = process_performance(metrics, bonuses)
print(f"Result: {final_score}")