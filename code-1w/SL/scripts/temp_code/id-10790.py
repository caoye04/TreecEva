import itertools

def analyze_access_pattern(sequences):
    # Irrelevant function: analyzes access patterns but not used in final calculation
    freq_map = {}
    for seq in sequences:
        for i, val in enumerate(seq):
            freq_map[i] = freq_map.get(i, 0) + 1
    return {k: v for k, v in freq_map.items() if v > 2}


def generate_diagnostics(data_stream):
    # Dead code path: generates diagnostics never used
    anomalies = []
    running_avg = 0
    count = 0
    for x in data_stream:
        if x < 0:
            anomalies.append(x)
        running_avg = (running_avg * count + x) / (count + 1) if count > 0 else x
        count += 1
    return {'avg': running_avg, 'anomalies': len(anomalies)}

# Misleading intermediate variables
temp_offset = 37
scaling_factor = 1.85
base_modifier = -9

# Simulated log entry structure: timestamp, user_id, action_type, duration_secs, error_flag
dummy_logs = [
    (1623456780, 101, 'READ', 12, False),
    (1623456785, 102, 'WRITE', 8, True),
    (1623456790, 101, 'READ', 15, False),
    (1623456795, 103, 'EXEC', 30, False),
    (1623456800, 102, 'READ', 5, False),
]

# Decoy transformation using list comprehension and lambda — unused later
transformed = [(lambda x: (x[0] % 1000, x[3] ** 0.5))(entry) for entry in dummy_logs if entry[2] != 'EXEC']

# Real data input
log_entries = [
    'USER_001|ACTION_LOGIN|DURATION_30|ERR_FALSE',
    'USER_002|ACTION_LOGOUT|DURATION_5|ERR_TRUE',
    'USER_001|ACTION_READ|DURATION_45|ERR_FALSE',
    'USER_003|ACTION_WRITE|DURATION_20|ERR_FALSE',
    'USER_002|ACTION_READ|DURATION_10|ERR_FALSE',
    'USER_001|ACTION_READ|DURATION_60|ERR_FALSE'
]

user_threshold = 40

# Unused sorting operation — distractor
sorted_logs = sorted(log_entries, key=lambda x: int(x.split('|')[2].split('_')[1]))

# Complex data transformation with red herrings
action_weights = {
    'LOGIN': 2.0,
    'LOGOUT': -1.0,
    'READ': 1.5,
    'WRITE': 2.5,
    'EXEC': 3.0
}

irrelevant_combinations = list(itertools.combinations(['LOGIN', 'LOGOUT', 'READ'], 2))

weight_adjuster = lambda w: w * 1.1 if w > 2.0 else w * 0.9
adjusted_weights = {k: weight_adjuster(v) for k, v in action_weights.items()}

# Core logic buried among distractions
def extract_duration(log):
    try:
        return int(log.split('|')[2].split('_')[1])
    except:
        return 0

def is_error_free(log):
    return 'ERR_FALSE' in log

def get_action(log):
    return log.split('|')[1].split('_')[1]

# Heavily nested aggregation with decoy conditions
def aggregate_performance(entries, threshold):
    total_duration = 0
    bonus_count = 0
    penalty_count = 0
    temp_sum = 0  # Red herring accumulator

    for entry in entries:
        duration = extract_duration(entry)
        action = get_action(entry)
        error_free = is_error_free(entry)

        # Meaningful condition
        if duration >= threshold and error_free:
            total_duration += duration
            if action == 'READ' or action == 'WRITE':
                bonus_count += 1

        # Distractor branch — looks important but unused
        if duration < 10:
            temp_sum += duration * 0.5
            if 'LOGIN' in entry:
                temp_sum -= 1

        # Dead logic with misleading comment
        # Apply decay factor for repeated actions (never actually implemented)
        last_action = None  # Unused tracking
        consecutive = 0     # Unused counter

    # Real computation hidden here
    base_score = total_duration * (1 + 0.1 * bonus_count)
    
    # Fake adjustment path
    if penalty_count > 0:
        base_score *= 0.9
    
    # Final score computed from non-obvious combination
    final = int(base_score - 123)  # Critical offset
    
    return final

# Unused itertools product — creates illusion of complex analysis
cross_analysis = list(itertools.product([1, 2], ['A', 'B']))

# Key execution point
final_score = aggregate_performance(log_entries, user_threshold)

# Print result as required
print(f"Result: {final_score}")