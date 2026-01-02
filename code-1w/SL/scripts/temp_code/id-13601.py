import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x > 0) - len(data)

# Misleading intermediate calculation with decoy variables
temp_offset = 17
scaling_factor = 0.89
legacy_mode = True
decoys = [i * 2 + temp_offset for i in range(5)]  # Unused list

# Core parameters (some are red herrings)
baseline = {
    'latency': 120,
    'throughput': 850,
    'error_rate': 0.012,
    'energy': 45.7
}

metrics = {
    'latency': 98,
    'throughput': 942,
    'error_rate': 0.008,
    'energy': 41.3,
    'retries': 3,
    'timeout_count': 0
}

# Distractor: complex but unused computation
correlation_matrix = [
    [math.sin(i * j * 0.1) for j in range(4)] 
    for i in range(4)
]

# Conditional expression used idiomatically
def adjust_for_environment(value, env_flag):
    return value * 0.95 if env_flag else value * 1.05

# Another decoy function that looks important but is never called
def calculate_legacy_metric(attrs):
    total = 0
    for k, v in attrs.items():
        if 'err' in k:
            total += 1 / (v + 1e-6)
        else:
            total += math.sqrt(v)
    return round(total, 3)

# Bit manipulation distraction (no impact on final result)
flag_register = 0b10101010
mask = 0b11110000
masked_flags = flag_register & mask
shifted_flags = masked_flags >> 4

# Real logic begins here — subtle integration among relevant parts
status_map = {'low': 1, 'medium': 2, 'high': 3}

def assess_latency_score(lat, base):
    ratio = lat / base
    if ratio <= 0.7:
        return 3
    elif ratio <= 0.9:
        return 2
    else:
        return 1

def assess_throughput_score(tp, base):
    ratio = tp / base
    return 3 if ratio >= 1.1 else (2 if ratio >= 0.95 else 1)

def get_error_impact(er, base_er):
    diff = er - base_er
    return 0 if diff <= 0 else 1 if diff < 0.005 else 2

# Energy efficiency evaluation using conditional expression
def energy_bonus(curr, base):
    return 10 if curr < base and (base - curr) / base > 0.08 else 0

# Main scoring logic — only this function contributes to answer
def evaluate_performance(m, b):
    score = 0

    # Latency assessment
    latency_good = assess_latency_score(m['latency'], b['latency'])
    score += latency_good * 15

    # Throughput assessment
    throughput_level = assess_throughput_score(m['throughput'], b['throughput'])
    score += throughput_level * 12

    # Error rate penalty
    error_penalty = get_error_impact(m['error_rate'], b['error_rate'])
    score -= error_penalty * 8

    # Energy bonus via conditional expression
    e_bonus = energy_bonus(m['energy'], b['energy'])
    score += e_bonus

    # Hidden adjustment: timeout check using ternary
    timeout_adj = -5 if m.get('timeout_count', 0) > 0 else (2 if m.get('retries') < 2 else 0)
    score += timeout_adj

    # Final nonlinear transformation (important!)
    adjusted = math.floor(score * scaling_factor) if legacy_mode else math.ceil(score)

    # Irrelevant mutation below (does not affect returned value)
    adjusted += sum(correlation_matrix[0])  # Red herring addition

    return adjusted  # Only this matters

# Decoy call that does nothing meaningful
_ = unused_diagnostic(decoys)

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Result: {final_score}")