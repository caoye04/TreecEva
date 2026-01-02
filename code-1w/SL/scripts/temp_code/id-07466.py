def analyze_access_patterns(log_entries):
    # Irrelevant function: analyzes access patterns but not used in final calculation
    counts = {}
    for entry in log_entries:
        ip = entry['ip']
        if ip not in counts:
            counts[ip] = 0
        counts[ip] += 1
    return {k: v for k, v in counts.items() if v > 1}


def validate_checksum(sequence):
    # Distractor function: computes a checksum, never called
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val + i) * 3
    return chk % 256

# Unused data structures for misdirection
temp_cache = [{'id': i, 'state': 'pending'} for i in range(15)]
legacy_mapping = {x: x**2 for x in range(10, 20)}

# Decoy variables with plausible names
critical_threshold = 87.5
system_uptime = 99.98
emergency_override = False
fallback_mode = True

# Real input data
data_log = [
    {'user': 'alice', 'action': 'edit', 'timestamp': 1001, 'size': 120},
    {'user': 'bob', 'action': 'view', 'timestamp': 1003, 'size': 45},
    {'user': 'alice', 'action': 'save', 'timestamp': 1005, 'size': 120},
    {'user': 'carol', 'action': 'edit', 'timestamp': 1008, 'size': 80},
    {'user': 'bob', 'action': 'export', 'timestamp': 1012, 'size': 200}
]

user_profile = {
    'alice': {'tier': 'premium', 'active': True, 'flags': ['fast', 'secure']},
    'bob': {'tier': 'basic', 'active': True, 'flags': []},
    'carol': {'tier': 'premium', 'active': False, 'flags': ['secure']}
}

# Secondary distractor: unused transformation
reindexed_log = dict(zip(range(len(data_log)), data_log))

# Auxiliary function that looks important but is partially irrelevant
def compute_engagement_metric(logs):
    user_actions = {}
    for record in logs:
        u = record['user']
        if u not in user_actions:
            user_actions[u] = 0
        user_actions[u] += 1
    
    total_interactions = sum(user_actions.values())
    unique_users = len(user_actions)
    
    # This intermediate result looks meaningful but isn't directly used
    fake_ratio = total_interactions / max(unique_users, 1) if unique_users else 0
    
    # Only return active premium users count — the actual relevant part
    active_premium = 0
    for u, cnt in user_actions.items():
        profile = user_profile.get(u, {})
        if profile.get('tier') == 'premium' and profile.get('active'):
            active_premium += cnt
    return active_premium

# Core logic buried among noise
def calculate_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = 0.0
    n = len(values)
    for f in freq.values():
        p = f / n
        entropy -= p * log2(p)
    return round(entropy, 4)

# Main computation function with red herrings
def calculate_final_score(log_entries, profile_map):
    # Step 1: Extract action types and sizes
    actions = [entry['action'] for entry in log_entries]
    sizes = [entry['size'] for entry in log_entries]
    
    # Step 2: Compute action frequency using dictionary
    action_count = {}
    for act in actions:
        action_count[act] = action_count.get(act, 0) + 1
    
    # Step 3: Determine unique users and their tiers
    observed_users = set(entry['user'] for entry in log_entries)
    premium_users = {u for u in observed_users if profile_map.get(u, {}).get('tier') == 'premium'}
    active_premium_count = 0
    for u in premium_users:
        if profile_map[u].get('active'):
            active_premium_count += 1
    
    # Step 4: Use enumerate to find first export index (distractor)
    first_export_idx = -1
    for idx, entry in enumerate(log_entries):
        if entry['action'] == 'export':
            first_export_idx = idx
            break
    
    # Step 5: Compute size parity flags (irrelevant)
    size_parity = [1 if s % 2 == 0 else 0 for s in sizes]
    parity_balance = abs(sum(size_parity) - (len(sizes) - sum(size_parity)))
    
    # Step 6: Calculate action diversity via set operations
    unique_actions = set(actions)
    action_entropy = calculate_entropy(actions)  # Relevant
    
    # Step 7: Apply tier-based weights
    weighted_score = 0
    for entry in log_entries:
        user_tier = profile_map[entry['user']]['tier']
        if user_tier == 'premium':
            weight = 2
        elif user_tier == 'basic':
            weight = 1
        else:
            weight = 0.5
        weighted_score += entry['size'] * weight
    
    # Step 8: Combine metrics (only some are used)
    base_score = len(log_entries) * 10
    diversity_bonus = len(unique_actions) * 5
    premium_bonus = active_premium_count * 20
    entropy_multiplier = max(1.0, action_entropy)  # Caps minimum multiplier
    
    # Final formula — only specific components matter
    raw_score = (base_score + diversity_bonus + premium_bonus) * entropy_multiplier
    
    # Distractor: normalize by fake ratio (unused)
    if first_export_idx > 0:
        dummy_normalizer = raw_score / (first_export_idx + 1)
    
    # Actual final score
    final_score = int(round(raw_score / 10 * (1 + 0.1 * len(profile_map.get('alice', {}).get('flags', []))), 0))
    
    # Dead code path (never reached due to above assignment)
    if fallback_mode:
        final_score = 999  # Misleading override

    return final_score

# Execution point of interest
final_score = calculate_final_score(data_log, user_profile)
print(f"Target result: {final_score}")