import itertools

def preprocess_logs(raw):
    # Irrelevant preprocessing (dead code path)
    cleaned = [entry.strip().lower() for entry in raw if entry]
    return [c for c in cleaned if 'error' not in c]

def validate_structure(data):
    # Distractor function: looks important but unused
    return all(isinstance(d, dict) and 'id' in d for d in data)

def generate_key_sequence(seeds):
    # Misleading computation: generates unused keys
    seq = []
    for s in seeds:
        temp = (s ^ 31) % 1000
        if temp > 500:
            seq.append(temp // 7)
    return seq

def filter_recent(entries, threshold=1000):
    # Partially relevant but overcomplicated filtering
    recent = []
    for e in entries:
        if isinstance(e, dict) and 'timestamp' in e:
            if e['timestamp'] > threshold:
                e['flagged'] = False  # Red herring field
                recent.append(e)
    return recent

def compute_integrity_score(logs, keys):
    # Core logic buried among distractions
    base = 0
    key_iter = itertools.cycle(keys)
    
    for log in logs:
        # Extract action length only from valid records
        if 'action' in log and isinstance(log['action'], str):
            action_len = len(log['action'])
            timestamp = log.get('timestamp', 0)
            priority = log.get('priority', 1)
            
            # Real computation: weighted XOR sum
            base ^= (action_len * priority + (timestamp & 255))
    
    # Secondary transformation using key stream
    for _ in range(len(keys)):
        base ^= next(key_iter) * 3
    
    # Final adjustment with bit manipulation
    base = (base << 1) ^ (base >> 2) ^ 9876
    return abs(base)  # Ensure positive result

# Main execution block
if __name__ == '__main__':
    # Input data setup
    raw_log_data = ['  USER_LOGIN ', 'DATA_EXPORT', '', 'SYSTEM_RESTART']
    log_entries = [
        {'timestamp': 1500, 'action': 'LOGIN', 'priority': 2},
        {'timestamp': 2000, 'action': 'EXPORT', 'priority': 5},
        {'timestamp': 800, 'action': 'HEARTBEAT', 'priority': 1},
        {'timestamp': 3000, 'action': 'SHUTDOWN', 'priority': 10}
    ]
    access_seeds = [123, 456, 789]
    
    # Irrelevant variables and operations (distractions)
    sanitized = preprocess_logs(raw_log_data)
    structure_ok = validate_structure(log_entries)
    dummy_keys = generate_key_sequence(access_seeds)
    filtered_logs = filter_recent(log_entries, threshold=1000)  # Only some logs used later
    
    # Unused intermediate values (misleading)
    temp_score = sum(len(log['action']) for log in log_entries) * 2
    checksum_alt = temp_score ^ 0xFFFF
    
    # Critical statement: actual answer computation
    final_checksum = compute_integrity_score(log_entries, access_seeds)
    
    # Output result as required
    print(f"Result: {final_checksum}")