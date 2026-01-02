def analyze_sequence(seq):
    return sum(x ** 2 for x in seq if x % 2 == 0)

system_state = {
    'active': True,
    'level': 3,
    'flags': [1, 0, 1],
    'threshold': 42
}

log_data = [
    'ERROR: disk full',
    'INFO: user login',
    'WARNING: high temp',
    'INFO: backup started',
    'ERROR: timeout'
]

# Irrelevant helper function (decoy)
def validate_entry(entry):
    parts = entry.split(': ')
    if len(parts) < 2:
        return False
    severity = parts[0]
    return severity in ['ERROR', 'WARNING', 'INFO']

# Distractor computation chain
raw_counts = {level: 0 for level in ['ERROR', 'WARNING', 'INFO']}
for entry in log_data:
    if ': ' in entry:
        severity, _ = entry.split(': ', 1)
        if severity in raw_counts:
            raw_counts[severity] += 1

# Unused transformation path (dead code)
token_matrix = []
for entry in log_data:
    tokens = entry.lower().replace(':', '').split()
    token_matrix.append([t.upper() for t in tokens if len(t) > 3])

# Real processing begins here — deeply nested and mixed with noise
status_flags = []
for i, entry in enumerate(log_data):
    flag_value = 0
    if 'ERROR' in entry:
        flag_value = 3
    elif 'WARNING' in entry:
        flag_value = 2
    elif 'INFO' in entry:
        flag_value = 1
    status_flags.append((i, flag_value))

# Character analysis red herring
total_chars = sum(len(e) for e in log_data)
filtered_logs = [e for e in log_data if 'ERROR' not in e]

# Bit manipulation decoy (appears relevant but isn't used in final result)
bit_accumulator = 0
for i, flag in enumerate(system_state['flags']):
    bit_accumulator |= (flag << i)

# Core diagnostic logic buried under distractions
def extract_signatures(data_list):
    sigs = []
    for idx, item in enumerate(data_list):
        clean = item.replace(':', ' ').lower()
        words = clean.split()
        # Use enumerate and string method
        for pos, word in enumerate(words):
            if word == 'error':
                sigs.append(idx + pos)
    return sigs

# Secondary irrelevant transform
def count_caps(text_list):
    return sum(1 for t in text_list for c in t if c.isupper())

# Main metric processor — only this matters
relevance_scores = []  
for line in log_data:
    score = 0
    if 'ERROR' in line:
        score += 10
    if 'high' in line:
        score += 3
    if 'backup' in line:
        score += 2
    relevance_scores.append(score)

# Critical data transformation using zip and enumerate
combined_index = 0
for i, (score, entry) in enumerate(zip(relevance_scores, log_data)):
    if 'temp' in entry:
        combined_index += score * (i + 1)

baseline = system_state['level'] * 7

# Another decoy: sequence analyzer on fake data
phantom_seq = [x - 2 for x in range(10) if x % 3 != 0]
analyze_sequence(phantom_seq)  # Called but result unused

# Final processing with hidden logic
interim = 0
for i, sc in enumerate(relevance_scores):
    if sc > 0:
        interim += sc * (i + 1)

adjustment = 0
if system_state['active']:
    adjustment = sum(system_state['flags']) * 2

# Key variable assignment buried in complexity
final_diagnostic = baseline + interim - adjustment + combined_index

# Output required format
print(f"Target result: {final_diagnostic}")