import itertools

def analyze_efficiency(values):
    # Irrelevant function - dead code path
    cumulative = 0
    for v in values:
        if v > 50:
            cumulative += v // 3
    return cumulative

def validate_input(data):
    # Distractor: validates but doesn't affect final result
    if not isinstance(data, dict) or 'items' not in data:
        return False
    return all(isinstance(x, int) for x in data['items'])

def compute_baseline(seq, mode='fast'):
    # Computes baseline but only part is relevant
    total = sum(x ** 0.5 for x in seq if x > 0)
    count = len([x for x in seq if x % 2 == 0])
    adjustment = total / (count + 1)
    # Red herring: unused complex logic
    extras = [x for x in seq if x in (64, 128)]
    scale = 1.0
    if len(extras) > 1:
        scale = len(extras) * 0.7
    return adjustment  # Only this matters

def extract_flags(config):
    # Misleading intermediate computation
    flags = []
    for k, v in config.items():
        if k.startswith('flag_') and v:
            flags.append(k[5:])
    return len(flags) > 0

def process_performance(met, adj):
    # Core logic with embedded distractors
    temp_data = []
    for k, v in met.items():
        if 'latency' in k:
            temp_data.append(v * 1.2)
        elif 'throughput' in k:
            temp_data.append(v * 0.85)
    
    # Real computation begins here
    base = compute_baseline(temp_data)
    
    # Distractor: complex-looking but unused block
    shadow_map = {i: val for i, val in enumerate(itertools.accumulate(temp_data)) if val % 2 == 0}
    outlier_check = [x for x in temp_data if x > 100]
    if len(outlier_check) > 2:
        base *= 0.9
    
    # Key transformation
    modifier = 1.0
    if 'scaling' in adj and adj['scaling'] == 'aggressive':
        modifier = 1.5
    elif 'scaling' in adj and adj['scaling'] == 'conservative':
        modifier = 0.7

    # Additional red herring: string processing unrelated to output
    status_msg = "System operational"
    tokens = status_msg.upper().replace(" ", "_")
    token_len = len(tokens)
    padding = ''.join(itertools.islice(itertools.cycle(['X']), token_len))

    # Actual answer derivation
    raw_score = base * modifier
    
    # Final conditional adjustment
    if raw_score > 60:
        final_score = int(raw_score - 12.5)
    else:
        final_score = int(raw_score + 8.3)
    
    # Critical statement
    final_score = process_performance(metrics, adjustments)
    return final_score

# Setup data
metrics = {
    'latency_avg': 45,
    'latency_peak': 130,
    'throughput_rps': 75,
    'latency_stddev': 20,
    'throughput_max': 110
}

adjustments = {
    'scaling': 'aggressive',
    'flag_optimized': True,
    'flag_debug': False,
    'buffer_size': 2048
}

# Unused variables - distraction
system_state = {'health': 'nominal', 'load': 0.67}
data_buffer = [0] * 128
diagnostic_trace = analyze_efficiency([64, 72, 88, 92, 105])

# Input validation call - irrelevant to outcome
is_valid = validate_input({'items': [1, 2, 3, 4]})

# Flag extraction - misleading side computation
flags_active = extract_flags(adjustments)

# Main execution
final_score = 0
final_score = process_performance(metrics, adjustments)
print(f"Result: {final_score}")