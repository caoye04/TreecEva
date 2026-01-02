def analyze_access_pattern(sequence):
    # Irrelevant function: analyzes string patterns in user agent logs
    if not sequence:
        return 0
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            count += 1
    return count

# Decoy data structures
temp_cache = [0] * 100
debug_trace = {'level': 'INFO', 'active': False}
baseline_offset = 42

# Real input data
log_entries = [
    '2023-06-01|userA|action=edit|status=success',
    '2023-06-01|userB|action=view|status=fail',
    '2023-06-02|userA|action=delete|status=success',
    '2023-06-02|userC|action=edit|status=success',
    '2023-06-03|userB|action=edit|status=success'
]

user_weights = {
    'userA': 1.2,
    'userB': 0.8,
    'userC': 1.5
}

# Misleading accumulation (dead path)
cumulative_risk_score = 0
for entry in log_entries:
    parts = entry.split('|')
    action = parts[2].split('=')[1]
    if action == 'delete':
        cumulative_risk_score += 3.1
    elif action == 'edit':
        cumulative_risk_score += 1.2

# Unused helper function
def compute_entropy(s):
    from math import log
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return -sum((f / len(s)) * log(f / len(s)) for f in freq.values())

# Real logic begins here
def extract_status(entry):
    return entry.split('|')[-1].split('=')[1]

def extract_user(entry):
    return entry.split('|')[1]

def extract_date(entry):
    return entry.split('|')[0]

# Bit manipulation red herring
def obscure_value(x):
    return ((x << 3) & 255) ^ 17

obfuscation_keys = [obscure_value(i) for i in range(10)]

# Core processing with distractions
daily_success_tally = {}
success_count_map = {}  # duplicate structure (distractor)

for log in log_entries:
    date = extract_date(log)
    status = extract_status(log)
    user = extract_user(log)
    
    # Real logic
    if date not in daily_success_tally:
        daily_success_tally[date] = 0
    if status == 'success':
        daily_success_tally[date] += 1

    # Irrelevant nested condition
    if user == 'userX':  # never occurs
        debug_trace['active'] = True
        temp_cache[0] += 1

# Process weights and success rates
user_success_rate = {u: 0 for u in user_weights.keys()}
user_action_count = {u: 0 for u in user_weights.keys()}

for log in log_entries:
    user = extract_user(log)
    status = extract_status(log)
    if user in user_success_rate:
        user_action_count[user] += 1
        if status == 'success':
            user_success_rate[user] += 1

# Normalize rates
for u in user_success_rate:
    if user_action_count[u] > 0:
        user_success_rate[u] /= user_action_count[u]

# High interference: complex unused transformation
weighted_vector = []
for i, u in enumerate(user_weights):
    w = user_weights[u]
    r = user_success_rate[u]
    # This entire vector is unused
    transformed = (w * r * 100) + baseline_offset
    weighted_vector.append(int(transformed) ^ obfuscation_keys[i % 10])

# Critical real computation hidden among noise
def aggregate_performance(entries, weights):
    total_score = 0.0
    user_contributions = []
    
    # Real accumulation
    for entry in entries:
        user = extract_user(entry)
        status = extract_status(entry)
        weight = weights.get(user, 1.0)
        
        # Scoring logic
        if status == 'success':
            total_score += weight * 10
        else:
            total_score -= weight * 2
        
        # Dead code inside critical function
        date_slice = entry[12:14]
        if date_slice.isdigit():
            hour = int(date_slice)
            if hour % 3 == 0:
                total_score += 0.1  # Never meaningfully affects result due to rarity
    
    # Additional distraction: sorting irrelevant list
    user_contributions.sort(reverse=True)
    
    # Final adjustment based on pattern analysis (irrelevant but looks important)
    pattern_test = ''.join([e.split('|')[1][0] for e in entries])
    autocorrelation = analyze_access_pattern(pattern_test)
    
    # ACTUAL final score (autocorrelation is always 0 in this case)
    total_score -= autocorrelation * 1.5
    
    return total_score

# Execute main logic
final_score = aggregate_performance(log_entries, user_weights)

# Print required output
print(f"Target result: {final_score}")