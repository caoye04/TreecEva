def analyze_access_patterns(log_data):
    # Irrelevant function: analyzes access patterns but not used in final computation
    frequency_map = {}
    for entry in log_data:
        ip = entry['ip']
        frequency_map[ip] = frequency_map.get(ip, 0) + 1
    return {k: v for k, v in frequency_map.items() if v > 1}


def validate_checksums(data_blocks):
    # Dead code path: checksum validation not used in main logic
    def compute_crc(block):
        crc = 0
        for b in block.encode():
            crc ^= b << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc <<= 1
        return crc & 0xFFFF
    
    valid_count = 0
    for block in data_blocks:
        if compute_crc(block) % 7 != 0:  # arbitrary condition
            valid_count += 1
    return valid_count

# Unused data structures acting as distractors
temporal_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
access_categories = {'read': 1, 'write': 2, 'delete': 3, 'exec': 4}
dummy_mapping = {i: chr(65 + i % 26) for i in range(50)}

# Decoy variables with plausible names
cached_results = []
running_aggregate = 0
normalization_factor = 1.0

# Core data
log_entries = [
    {'user': 'alice', 'action': 'read', 'duration': 120, 'success': True, 'tags': ['fast', 'local']},
    {'user': 'bob', 'action': 'write', 'duration': 45, 'success': True, 'tags': ['short']},
    {'user': 'alice', 'action': 'read', 'duration': 300, 'success': False, 'tags': ['long', 'remote']},
    {'user': 'carol', 'action': 'read', 'duration': 90, 'success': True, 'tags': ['short']},
    {'user': 'bob', 'action': 'read', 'duration': 60, 'success': True, 'tags': ['short']}
]

user_weights = {
    'alice': (0.8, 1.2),  # (base_weight, multiplier)
    'bob': (0.6, 1.5),
    'carol': (1.0, 1.1)
}

# Real logic begins here — deeply nested and mixed with distractions
recent_threshold = 200
penalty_rate = 0.25
bonus_credit = 0.05

status_flags = set()
if any(e['success'] for e in log_entries):
    status_flags.add('HAS_SUCCESS')
if all(e['duration'] < 300 for e in log_entries if e['success']):
    status_flags.add('ALL_FAST_SUCCESS')

# Key intermediate structure
user_stats = {}
for idx, entry in enumerate(log_entries):
    user = entry['user']
    action = entry['action']
    duration = entry['duration']
    success = entry['success']
    
    if user not in user_stats:
        user_stats[user] = {
            'attempts': 0,
            'successes': 0,
            'total_duration': 0,
            'recent_bonus': 0,
            'tag_count': {}
        }
    
    stats = user_stats[user]
    stats['attempts'] += 1
    if success:
        stats['successes'] += 1
    stats['total_duration'] += duration
    
    # Accumulate tag counts using tuple unpacking distraction
    for tag in entry.get('tags', []):
        prev_count = stats['tag_count'].get(tag, 0)
        stats['tag_count'][tag] = prev_count + 1
    
    # Bonus logic for short durations
    if duration < recent_threshold:
        stats['recent_bonus'] += bonus_credit

# Compute derived metrics with zip and enumerate
user_performance = {}
for i, (user, stats) in enumerate(zip(user_stats.keys(), user_stats.values())):
    base_weight, multiplier = user_weights.get(user, (0.5, 1.0))
    
    attempt_score = stats['attempts'] * 0.1
    success_rate = stats['successes'] / stats['attempts'] if stats['attempts'] > 0 else 0
    duration_efficiency = 1 / (1 + stats['total_duration'] / 100)
    
    # Weighted combination
    raw_score = (
        base_weight + 
        success_rate * 2.0 + 
        duration_efficiency * 0.5 + 
        stats['recent_bonus']
    ) * multiplier
    
    user_performance[user] = raw_score

# Aggregate across users with combinatorics distraction
combination_count = 0
for r in range(1, len(user_performance) + 1):
    combination_count += 2 ** r  # Simulating combinatorial growth, unused

# Final aggregation — this is the critical point
def aggregate_performance(logs, weights):
    total = 0.0
    count = 0
    for entry in logs:
        u = entry['user']
        s = entry['success']
        d = entry['duration']
        if s:
            score = user_performance[u]
            penalty = 0
            if d > 200:
                penalty = score * penalty_rate
            total += score - penalty
            count += 1
    return int(total * 100) // 100  # Discretized final score

# Critical execution point
final_score = aggregate_performance(log_entries, user_weights)

# Misleading print statements to distract
print(f"Validation check: {validate_checksums([e['action'] for e in log_entries])}")
print(f"Access frequencies: {analyze_access_patterns(log_entries)}")
print(f"Status flags active: {status_flags}")

# Required output format
print(f"Target result: {final_score}")