def analyze_access_patterns(log_data):
    # Irrelevant function: analyzes access frequency (not used in final result)
    access_count = {}
    for entry in log_data:
        ip = entry['ip']
        access_count[ip] = access_count.get(ip, 0) + 1
    return {k: v for k, v in access_count.items() if v > 1}


def validate_checksum(sequence):
    # Decoy function: computes XOR checksum (used to mislead)
    checksum = 0
    for val in sequence:
        checksum ^= val
    return checksum == 0


def extract_signals(sensor_stream):
    # Unused transformation: processes sensor data (red herring)
    filtered = [x for x in sensor_stream if x % 3 == 0]
    normalized = [x / max(filtered) if filtered else 0 for x in filtered]
    return [round(x, 2) for x in normalized]


def compute_entropy(values):
    # Dead code path: calculates Shannon entropy (not used)
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * log2(p) for p in probs)


def aggregate_performance(log_entries, metrics):
    # Core logic starts here — heavily obscured by noise above
    
    # Step 1: Extract timestamps and actions
    actions = [entry['action'] for entry in log_entries]
    
    # Step 2: Map action types to numeric scores using dict
    action_weights = {'login': 2, 'view': 1, 'edit': 3, 'delete': -5}
    base_scores = [action_weights.get(act, 0) for act in actions]
    
    # Step 3: Use enumerate and zip to align with user_metrics
    weighted_sum = 0
    for i, score in enumerate(base_scores):
        if i % 2 == 0:
            # Only even-indexed actions are counted
            multiplier = metrics[i % len(metrics)]
            weighted_sum += score * multiplier
    
    # Step 4: Apply conditional boost based on pattern
    success_streak = 0
    max_streak = 0
    for act in actions:
        if act in ['login', 'view']:
            success_streak += 1
        else:
            max_streak = max(max_streak, success_streak)
            success_streak = 0
    max_streak = max(max_streak, success_streak)
    
    # Step 5: Streak bonus
    streak_bonus = max_streak * 2
    
    # Step 6: Use dictionary operations to count action frequencies
    freq_map = {}
    for act in actions:
        freq_map[act] = freq_map.get(act, 0) + 1
    
    # Step 7: Apply penalty for excessive 'delete' actions
    delete_penalty = freq_map.get('delete', 0) * 4
    
    # Step 8: Final computation
    raw_performance = weighted_sum + streak_bonus - delete_penalty
    
    # Step 9: Normalize using bitwise adjustment (simulate low-level tuning)
    adjusted = (raw_performance ^ 0x1F) & 0x7FFFFFFF  # Flip lower bits, ensure positive
    if adjusted & 0x80000000:
        adjusted -= 0x100000000
    
    # Step 10: Final scaling
    final_score = abs(adjusted) % 100000  # Bound within reasonable range
    
    # Distractor: call irrelevant functions with fake data
    _ = analyze_access_patterns(log_entries)
    _ = validate_checksum([1, 2, 3, 0])  # returns True, unused
    _ = extract_signals([6, 9, 12, 15])
    _ = compute_entropy([10, 20, 30])
    
    return final_score

# Simulated input data
log_entries = [
    {'timestamp': 1001, 'ip': '192.168.1.10', 'action': 'login'},
    {'timestamp': 1002, 'ip': '192.168.1.10', 'action': 'view'},
    {'timestamp': 1005, 'ip': '192.168.1.12', 'action': 'edit'},
    {'timestamp': 1010, 'ip': '192.168.1.15', 'action': 'delete'},
    {'timestamp': 1011, 'ip': '192.168.1.10', 'action': 'login'},
    {'timestamp': 1012, 'ip': '192.168.1.10', 'action': 'view'},
    {'timestamp': 1013, 'ip': '192.168.1.10', 'action': 'view'}
]

user_metrics = [1.5, 2.0, 0.5]

# Execution point of interest
final_score = aggregate_performance(log_entries, user_metrics)
print(f"Result: {final_score}")