def analyze_sequence(data):
    # Irrelevant helper: computes sum of squares (never used in final result)
    return sum(x ** 2 for x in data if x > 0)


def validate_integrity(checksum, reference):
    # Distractor function: looks important but unused
    return (checksum + 5) % 7 == reference % 7

# System state mappings (dictionary operations)
state_map = {
    'idle': 0,
    'active': 1,
    'paused': 2,
    'error': 3,
    'pending': 4
}

# Irrelevant historical codes
legacy_codes = {0: 'A', 1: 'B', 2: 'C'}

# Simulated transition log with metadata
transitions = [
    {'from': 'idle', 'to': 'active', 'ts': 100, 'delta': 1},
    {'from': 'active', 'to': 'paused', 'ts': 200, 'delta': -1},
    {'from': 'paused', 'to': 'active', 'ts': 250, 'delta': 1},
    {'from': 'active', 'to': 'error', 'ts': 300, 'delta': 0},
    {'from': 'error', 'to': 'idle', 'ts': 350, 'delta': -3}
]

# System log with auxiliary diagnostics (some relevant, some not)
system_log = [
    {'level': 'INFO', 'msg': 'startup', 'code': 200},
    {'level': 'WARN', 'msg': 'overload', 'code': 400},
    {'level': 'ERROR', 'msg': 'failure', 'code': 500},
    {'level': 'INFO', 'msg': 'recovery', 'code': 202}
]

# Dead code path — looks like it processes warnings but is never called
warning_tracker = []
def track_warnings(log):
    for entry in log:
        if entry['level'] == 'WARN':
            warning_tracker.append(entry['ts'])

# Auxiliary calculation: total energy (distractor)
total_energy = 0
for event in transitions:
    total_energy += abs(event['delta']) * 10

# Fake accumulator for cyclomatic complexity
complexity_score = 0
for t in transitions:
    if t['from'] in ['active', 'error']:
        complexity_score += 2
    else:
        complexity_score += 1

# Core logic disguised among distractions
current_state = state_map['idle']
state_changes = 0
error_count = 0
activation_depth = 0

for t in transitions:
    prev = current_state
    current_state = state_map[t['to']]
    if prev != current_state:
        state_changes += 1
    if t['to'] == 'error':
        error_count += 1
    if t['from'] == 'paused' and t['to'] == 'active':
        activation_depth += 1

# Secondary analysis: count critical logs
critical_events = 0
for log_entry in system_log:
    if log_entry['code'] >= 400:
        critical_events += 1

# Another red herring: sorting unrelated data
sorted_codes = sorted([entry['code'] for entry in system_log], reverse=True)
median_code = sorted_codes[len(sorted_codes) // 2] if sorted_codes else 0

# Simulate recursive depth counter (not actually recursive but looks involved)
max_stack_level = 0
temp_level = 0
for ev in transitions:
    temp_level += 1 if ev['delta'] > 0 else -1
    temp_level = max(1, temp_level)  # clamp
    max_stack_level = max(max_stack_level, temp_level)

# Bitwise manipulation distraction
mask = 0b1010
obfuscated = 0
for i, t in enumerate(transitions):
    obfuscated ^= (t['ts'] & mask) | (i << 2)

# Central processing function
def process_state(transition_list, log):
    base = 0
    recovery_bonus = 0

    # Real logic begins
    for t in transition_list:
        if t['to'] == 'active' and t['from'] != 'idle':
            base += 7
        if t['from'] == 'error' and t['to'] == 'idle':
            recovery_bonus += 5

    # Use dictionary to map states back (actual dependency)
    reverse_states = {v: k for k, v in state_map.items()}
    last_state = reverse_states[current_state]

    # Only certain transitions contribute
    valid_resets = 0
    for t in transition_list:
        if t['from'] == 'error' and t['to'] == 'idle':
            valid_resets += 1

    # Final computation
    output = base + recovery_bonus * 10 + valid_resets * 3

    # Additional fake components
    dummy = (total_energy + complexity_score) % 17
    debug_flag = (obfuscated & 1) == 0

    # This is the true answer; everything else distracts
    return output

# Execute main logic
final_output = process_state(transitions, system_log)

# Print result as required
print(f"Target result: {final_output}")