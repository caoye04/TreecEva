def normalize(value, min_val, max_val):
    """Irrelevant normalization function (distractor)"""
    if value <= min_val:
        return 0.0
    if value >= max_val:
        return 1.0
    return (value - min_val) / (max_val - min_val)


def calculate_entropy(data):
    """Complex distractor: computes entropy but not used in final path"""
    import math
    total = sum(data)
    entropy = 0.0
    for x in data:
        if x > 0:
            p = x / total
            entropy -= p * math.log2(p)
    return entropy

# Irrelevant data structures (red herrings)
user_preferences = {
    'theme': 'dark',
    'notifications': True,
    'auto_save': False,
    'language': 'en'
}

system_config = {
    'max_retries': 3,
    'timeout': 30,
    'debug_mode': True
}

# Real computational data
metrics = {
    'accuracy': 85,
    'latency': 45,
    'throughput': 120,
    'memory_usage': 65,
    'stability': 92
}

weights = {
    'accuracy': 0.3,
    'latency': -0.1,  # Negative weight: lower latency improves score
    'throughput': 0.2,
    'memory_usage': -0.15,
    'stability': 0.45
}

# Misleading intermediate calculations
raw_sum = sum(metrics.values())
score_baseline = raw_sum / len(metrics)  # Distractor: looks important

# Dead code path (never executed)
if False:
    dummy = {}
    for k, v in metrics.items():
        dummy[k] = v ** 2
    score_baseline = sum(dummy.values())

# Unused recursive function (decoy)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Another red herring: string processing with no impact
log_entry = "PERF:ACC=85;LAT=45;THR=120;MEM=65;STB=92"
tokens = log_entry.split(':')[-1].split(';')
parsed_values = {}
for t in tokens:
    k, v = t.split('=')
    parsed_values[k.lower()] = int(v)  # Looks like it's parsing same data

# Actual logic buried among noise
def adjust_for_latency(latency):
    # Higher penalty as latency increases
    if latency < 30:
        return 10
    elif latency < 60:
        return 5
    else:
        return -10

def adjust_memory_penalty(memory):
    if memory < 50:
        return 5
    elif memory < 80:
        return 0
    else:
        return -8

# Core evaluation logic
def evaluate_performance(met, wgt):
    base_score = 0.0
    for key in wgt:
        if key == 'latency':
            base_score += met[key] * wgt[key]
            base_score += adjust_for_latency(met[key])  # Bonus/penalty
        elif key == 'memory_usage':
            base_score += met[key] * wgt[key]
            base_score += adjust_memory_penalty(met[key])
        else:
            base_score += met[key] * wgt[key]
    
    # Additional adjustment based on stability threshold
    if met['stability'] > 90:
        base_score += 7
    
    # Hidden conditional: accuracy above 80 gives bonus only if throughput > 100
    if met['accuracy'] > 80 and met['throughput'] > 100:
        base_score += 6
    
    return round(base_score, 4)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Target result: {final_score}")