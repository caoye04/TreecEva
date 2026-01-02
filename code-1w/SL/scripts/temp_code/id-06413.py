import math

def analyze_phase(root_list, threshold):
    accumulated = 0
    for val in root_list:
        if val > threshold:
            accumulated += int(math.log(val + 1) * 2)
    return accumulated

# Irrelevant helper (dead function - never called in execution path)
def compute_entropy(data):
    entropy = 0.0
    total = sum(data)
    for x in data:
        prob = x / total if total > 0 else 1e-9
        entropy -= prob * math.log(prob, 2)
    return entropy

def transform_sequence(seq):
    # Applies modular arithmetic and bit shifts with red herring logic
    transformed = []
    mask = 0b1111
    for i, n in enumerate(seq):
        temp_val = (n ^ mask) % 17
        shifted = (temp_val << 1) | (temp_val >> 7)  # Circular shift mimic
        if i % 3 == 0:
            shifted = shifted ^ 5
        transformed.append(shifted & 255)
    return transformed

def filter_critical(entries, tags):
    # Uses set operations (required feature)
    critical_set = {"err", "fail", "crit"}
    filtered = []
    for e, t in zip(entries, tags):
        if t in critical_set:
            filtered.append(e * 2)
    return filtered

def process_metrics(log_data, system_flags):
    # Core computation buried in distractions
    base_score = 0
    temp_cache = []
    
    # Distractor: unused variable collection
    debug_snapshot = {
        'version': '2.1.9',
        'uptime': 87423,
        'mode': 'diagnostic'
    }
    
    # Real logic begins
    raw_values = [x['metric'] for x in log_data if x['active']]
    
    # Summation and accumulation
    total_power = sum(x for x in raw_values if x > 0)
    
    # Conditional branching with decoy blocks
    if total_power > 100:
        base_score += 42
    elif total_power > 50:
        base_score += 15
    else:
        base_score += 3
    
    # Modular arithmetic in non-trivial context
    modulo_anchor = (total_power * 7) % 13
    base_score = (base_score + modulo_anchor) * 2
    
    # Bit manipulation distraction (some effect but minimal)
    flag_state = 0
    for flag in system_flags:
        if flag == 'ACTIVE':
            flag_state |= 0b1010
        elif flag == 'STANDBY':
            flag_state ^= 0b0101
    
    # Only the lower 4 bits matter
    flag_contribution = flag_state & 0xF
    base_score += flag_contribution
    
    # Set-based filtering (required feature)
    tag_pool = [entry['tag'] for entry in log_data]
    unique_tags = set(tag_pool)
    diagnostic_codes = {hash(t) % 1000 for t in unique_tags}  # Decoy usage
    
    # Actual use of set: determine enhancement factor
    control_tags = {'alpha', 'beta', 'gamma'}
    overlap_count = len(unique_tags & control_tags)
    base_score *= (1 + overlap_count * 0.5)
    
    # Hidden accumulator chain
    accumulator = base_score
    for _ in range(3):
        accumulator = int((accumulator + 1) ** 0.5) * 3
    
    # Final assignment - key statement
    final_diagnostic = accumulator + len(diagnostic_codes) // 100  # Minor tweak
    
    # Dead code paths below
    if False:
        backup_log = transform_sequence(raw_values)
        fallback = analyze_phase(backup_log, 10)
        final_diagnostic = fallback
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Input construction with meaningful names
    log_data = [
        {'metric': 23, 'active': True, 'tag': 'alpha'},
        {'metric': 15, 'active': True, 'tag': 'beta'},
        {'metric': 8, 'active': False, 'tag': 'debug'},
        {'metric': 41, 'active': True, 'tag': 'gamma'},
        {'metric': 7, 'active': True, 'tag': 'info'}
    ]
    
    system_flags = ['ACTIVE', 'STANDBY', 'ACTIVE']
    
    # Key execution point
    final_diagnostic = process_metrics(log_data, system_flags)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")