from itertools import combinations, filterfalse
import math

# Simulated dataset: user activity logs with noise and irrelevant fields
test_logs = [
    {'user': 'A', 'actions': [3, 1, 4], 'time': 127, 'corrupted': False, 'checksum': 8},
    {'user': 'B', 'actions': [2, 2], 'time': 130, 'corrupted': True, 'checksum': 6},
    {'user': 'C', 'actions': [5], 'time': 125, 'corrupted': False, 'checksum': 5},
    {'user': 'D', 'actions': [1, 1, 1, 1], 'time': 135, 'corrupted': False, 'checksum': 4},
    {'user': 'E', 'actions': [3, 3], 'time': 128, 'corrupted': False, 'checksum': 6}
]

# Irrelevant statistical tracker (distractor)
avg_time = sum(log['time'] for log in test_logs) / len(test_logs)
adjusted_avg = avg_time * 0.95

# Noise generator: creates decoy data that looks meaningful
noise_data = []
for i in range(3):
    entry = {}
    entry['seq'] = [i*2 + j for j in range(4)]
    entry['meta'] = {'flag': i ^ 7, 'valid': (i % 2 == 0)}
    noise_data.append(entry)

# Checksum verifier (partially used, misleading intermediate)
def verify_checksum(record):
    expected = sum(record['actions'])
    return expected == record['checksum']

# Decoy function - appears useful but unused in critical path
def decrypt_sequence(seq):
    return [int(x ** 0.5) if x > 1 else x for x in seq]

# Real validation: filters corrupted and verifies integrity
def validate_log(log):
    if log['corrupted']:
        return False
    if not verify_checksum(log):
        return False
    return True

# Scoring mechanism with multiple red herrings
base_weights = [1.1, 0.9, 1.0, 1.2]
decoy_weights = [w ** 2 for w in base_weights]  # Looks important but unused

# Critical processing function
def compute_action_score(actions):
    raw = sum(a ** 2 for a in actions)
    penalty = len(list(filterfalse(lambda x: x > 1, actions))) * 0.5
    return raw - penalty

# Advanced filtering using itertools - real use case
potential_combos = list(combinations([1, 2, 3, 4], 3))
combo_sum_set = {sum(c): c for c in potential_combos}  # dictionary comprehension red herring

# Core logic obscured by surrounding noise
def process_entry(entry):
    score = compute_action_score(entry['actions'])
    time_bonus = 0
    if entry['time'] < 130:
        time_bonus = 1.5
    return {'user': entry['user'], 'score': score, 'bonus': time_bonus}

# Another decoy transformation
transformed_noise = []
for item in noise_data:
    transformed = [x | 3 for x in item['seq']]
    transformed_noise.append(transformed)

# Main processing pipeline
validated_entries = []
for log in test_logs:
    if validate_log(log):
        processed = process_entry(log)
        validated_entries.append(processed)

# Aggregation with misleading intermediate normalizations
max_possible = max((e['score'] + e['bonus']) for e in validated_entries)
scaled_entries = [{
    'user': e['user'], 
    'scaled': (e['score'] + e['bonus']) / max_possible * 100
} for e in validated_entries]

# Final computation - the actual answer source
final_score = 0
for entry in validated_entries:
    contribution = entry['score']
    if entry['bonus'] > 0:
        contribution *= 1.2  # performance multiplier
    final_score += int(contribution)  # integer truncation matters

# Spurious secondary calculation to distract
aggregate_metric = sum(se['scaled'] for se in scaled_entries) / len(scaled_entries)

# Output the required result
print(f"Result: {final_score}")