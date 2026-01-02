from collections import defaultdict, Counter

# Irrelevant helper function (decoy)
def validate_checksum(seq):
    return sum(seq) % 7 == 0

# Misleading transformation chain
def transform_v1(data):
    temp = [x * 2 + 1 for x in data]
    return [t for t in temp if t % 3 != 0]

def transform_v2(data):
    shifted = [(x >> 1) ^ 5 for x in data]
    filtered = [s for s in shifted if s > 10]
    return sorted(filtered, reverse=True)

# Unused dead-end function
def legacy_compatibility(data):
    return list(map(lambda x: x + 100, data))

# Core logic buried among distractions
def evaluate_threshold(seq, limit=25):
    count = 0
    for val in seq:
        if val < limit:
            count += 1
            if count > 3:
                break
    return count >= 4

# Heavily obfuscated but correct processing path
def process_sequence(raw, cfg):
    # Distractor: unused config keys
    mode = cfg.get('mode', 'unknown')
    debug = cfg.get('debug_trace', False)
    timeout = cfg.get('max_wait', 999)
    seed = cfg.get('init_seed', 0)

    # Real logic begins
    stage1 = [x for x in raw if x % 2 == 1]  # keep odds
    
    # Bit manipulation red herring
    masked = [x & 0b1111 for x in stage1]
    extended = masked + [sum(masked) // len(masked)] if masked else [0]
    
    # Conditional expression with distractor
    multiplier = 3 if len(extended) > 5 else 2
    stage2 = [x * multiplier for x in extended]
    
    # Use of collections.Counter for non-obvious purpose
    freq = Counter(stage2)
    common_vals = [v for v, cnt in freq.most_common() if cnt > 1]
    
    # Actual decision point
    adjustment = -5 if evaluate_threshold(stage2, 30) else 10
    
    # String-based decoy (irrelevant to outcome)
    status_flag = "OK" if sum(stage2) > 50 else "ERR"
    log_entry = f"Status: {status_flag}, Size: {len(stage2)}"
    
    # Critical calculation
    base_result = sum(stage2) + adjustment
    
    # More distraction: unused tuple unpacking
    if len(common_vals) >= 2:
        first_common, *rest_common = common_vals
        buffer = (first_common * 2) ^ 17
    else:
        buffer = 0

    # Final computation
    final_shift = (base_result >> 2) + (len(raw) % 7)
    return final_shift

# Main execution flow
if __name__ == "__main__":
    # Input data with meaningful structure
    data = [12, 15, 22, 27, 30, 33, 36, 39]
    
    # Configuration map with many irrelevant fields
    config = {
        'mode': 'production',
        'debug_trace': True,
        'max_wait': 500,
        'init_seed': 42,
        'cache_enabled': False,
        'retry_limit': 3,
        'timeout_policy': 'strict'
    }
    
    # Dead code path (never executed)
    if False:
        backup_data = transform_v1(data)
        alt_out = legacy_compatibility(backup_data)

    # Key statement
    final_output = process_sequence(data, config)
    
    # Print result as required
    print(f"Target result: {final_output}")