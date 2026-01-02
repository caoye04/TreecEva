def process_entries(entries):
    processed = []
    temp_sum = 0
    for entry in entries:
        cleaned = entry.strip().lower()
        if 'error' in cleaned:
            continue
        words = cleaned.split(' ')
        valid_parts = [w for w in words if w.isalpha()]
        temp_sum += len(valid_parts)
        processed.append(' '.join(valid_parts))
    return processed, temp_sum


def transform_data(seq):
    reversed_chunks = []
    for i in range(0, len(seq), 3):
        chunk = seq[i:i+3][::-1]
        reversed_chunks.extend(chunk)
    return reversed_chunks

# Simulate log data parsing and scoring
raw_logs = [
    'User Login Attempt FAILED',
    'INFO: System Check OK',
    'WARNING: High Memory Usage',
    'ERROR: Disk Read Failure',
    'Success! Backup Completed'
]

parsed_logs, total_keywords = process_entries(raw_logs)

# Misleading intermediate transformation (not directly used)
dummy_transformation = transform_data([c for c in 'abcde'])
shadow_value = sum([len(log) for log in parsed_logs]) * 0.5

# Core computation begins
base_values = []
for log in parsed_logs:
    tokens = log.split()
    score = 0
    for token in tokens:
        if token.startswith('warn'):
            score += 10
        elif token.startswith('fail'):
            score -= 5
        elif token.startswith('success') or token == 'ok':
            score += 15
        else:
            score += len(token) % 4
    base_values.append(score)

aggregated = sum(base_values)

# Bonus logic with string-based condition
status_flags = ''.join([log.split()[0] for log in parsed_logs if log])
bonus_multiplier = 2 if 'success' in status_flags.lower() else 1

# Distractor: complex but unused calculation
complex_distractor = 0
for i in range(len(parsed_logs)):
    for j in range(i + 1, len(parsed_logs)):
        complex_distractor += len(parsed_logs[i]) ^ len(parsed_logs[j])

# Final scoring function
def calculate_final_score(data, multiplier):
    raw_total = sum(data)
    adjustment = len(data) * 3
    # Apply multiplier only if conditions met
    if multiplier > 1 and raw_total > 0:
        return (raw_total + adjustment) * multiplier
    else:
        return raw_total + adjustment

final_score = calculate_final_score(base_values, bonus_multiplier)
print(f"Result: {final_score}")