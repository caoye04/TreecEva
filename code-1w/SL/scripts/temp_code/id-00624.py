def analyze_permissions(flags):
    read_count = 0
    write_count = 0
    exec_count = 0
    for flag in flags:
        if flag & 1:
            read_count += 1
        if flag & 2:
            write_count += 1
        if flag & 4:
            exec_count += 1
    return (read_count, write_count, exec_count)


def validate_hierarchy(level_map):
    max_depth = 0
    current_path = []
    for level in level_map.values():
        while current_path and current_path[-1] >= level:
            current_path.pop()
        current_path.append(level)
        max_depth = max(max_depth, len(current_path))
    return max_depth


def calculate_final_score(data, flags):
    temp_stats = {}
    redundant_sum = 0
    for k, v in data.items():
        if len(k) % 2 == 0:
            redundant_sum += len(v)
        temp_stats[k] = len(v) * (hash(k) % 5)
    
    # Irrelevant aggregation
    unused_aggregate = sum(temp_stats.values()) // (len(temp_stats) or 1)

    base_score = 0
    penalty = 0
    
    # Real scoring logic begins
    active_users = set()
    role_groups = {'admin': set(), 'moderator': set(), 'user': set()}
    
    for user_id, attrs in data.items():
        role = attrs.get('role', 'user')
        if role in role_groups:
            role_groups[role].add(user_id)
        active_users.add(user_id)
        
        if attrs.get('verified'):
            base_score += 10
        if attrs.get('age', 0) > 30:
            base_score += 5
        if attrs.get('tenure', 0) > 365:
            base_score += 7

    # Bitwise flag analysis
    r, w, x = analyze_permissions(flags)
    if r >= 2:
        base_score += 8
    if w >= 1:
        base_score += 6
    if x == 0:
        penalty += 3
    
    # Dictionary-based bonus calculation
    group_bonus = 0
    for role, members in role_groups.items():
        if len(members) >= 2 and role != 'user':
            group_bonus += 12
    
    # Dummy structure processing (distraction)
    metadata_summary = {}
    for user_id in data:
        segment = ''.join([c for c in user_id if c.isdigit()])
        bucket = int(segment) % 100 if segment else 0
        metadata_summary[bucket] = metadata_summary.get(bucket, 0) + 1
    
    # Unused nested loop
    total_pairs = 0
    for u1 in active_users:
        for u2 in active_users:
            if u1 < u2 and abs(hash(u1) - hash(u2)) % 13 == 0:
                total_pairs += 1

    # Final score computation
    final_score = base_score + group_bonus - penalty
    
    # These do not affect final_score
    debug_info = {
        'redundant_sum': redundant_sum,
        'unused_aggregate': unused_aggregate,
        'total_pairs': total_pairs
    }
    
    return final_score

# Main execution
user_data = {
    'alice': {'role': 'admin', 'verified': True, 'age': 35, 'tenure': 730},
    'bob': {'role': 'moderator', 'verified': False, 'age': 28, 'tenure': 200},
    'carol': {'role': 'admin', 'verified': True, 'age': 45, 'tenure': 1000},
    'dave': {'role': 'user', 'verified': True, 'age': 32, 'tenure': 800}
}
access_flags = [3, 7, 5, 1]  # R/W, R/W/X, R/X, R only

hierarchy_levels = {'section_A': 1, 'subsection_A1': 2, 'item_A1a': 3, 'item_A1b': 3}
validate_hierarchy(hierarchy_levels)

final_score = calculate_final_score(user_data, access_flags)
print(f"Target result: {final_score}")