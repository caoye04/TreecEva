def analyze_sequence(data, mask):
    """Irrelevant transformation function (dead code path)"""
    return [x ^ mask for x in data if x % 2 == 0]


def generate_primes(n):
    """Decoy function: generates primes but not used in main logic"""
    sieve = [True] * n
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]

# Irrelevant prime list (distractor)
prime_lookup = generate_primes(100)

# System event log with diagnostic codes and timestamps
event_log = [
    {'code': 101, 'time': 1623456780, 'level': 'ERROR'},
    {'code': 205, 'time': 1623456785, 'level': 'WARNING'},
    {'code': 101, 'time': 1623456790, 'level': 'ERROR'},
    {'code': 304, 'time': 1623456795, 'level': 'INFO'},
    {'code': 205, 'time': 1623456800, 'level': 'WARNING'}
]

# System flags with bit-encoded states (some relevant, some not)
system_flags = {
    'ACTIVE': True,
    'DEBUG_MODE': False,
    'REDUNDANCY_CHECK': True,
    'OVERFLOW_LOCK': False,
    'CRC_ENABLED': True
}

# Misleading intermediate calculation (unused)
temporal_drift = sum(entry['time'] % 100 for entry in event_log) // len(event_log)

# Character frequency map for codes (red herring)
frequency_map = {}
code_strings = [str(entry['code']) for entry in event_log]
for code_str in code_strings:
    for char in code_str:
        frequency_map[char] = frequency_map.get(char, 0) + 1

# Real processing begins here — count occurrences of each error codedef count_codes(log):
    counts = {}
    for entry in log:
        c = entry['code']
        counts[c] = counts.get(c, 0) + 1
    return counts

# Extract unique codes in order of appearance
seen_codes = []
for entry in event_log:
    code = entry['code']
    if code not in seen_codes:
        seen_codes.append(code)

# Compute pairwise XOR of consecutive codes (distraction)
xor_chain = []
for i in range(len(seen_codes) - 1):
    xor_chain.append(seen_codes[i] ^ seen_codes[i+1])

# Actual core logic: compute weighted diagnostic score
def compute_integrity_score(log_entries, flags):
    # Step 1: Count occurrences
    code_count = count_codes(log_entries)
    
    # Step 2: Assign weights based on severity
    weight_map = {101: 3.0, 205: 1.5, 304: 0.5}
    total_weight = 0.0
    for code, count in code_count.items():
        if code in weight_map:
            total_weight += weight_map[code] * count
    
    # Step 3: Apply flag-based modifiers
    if flags['CRC_ENABLED']:
        total_weight *= 1.1
    if flags['DEBUG_MODE']:
        total_weight -= 5.0  # Not triggered
    
    # Step 4: Adjust based on redundancy policy
    if flags['REDUNDANCY_CHECK']:
        # Bonus for repeated errors (indicates detection)
        repeats = sum(1 for count in code_count.values() if count > 1)
        total_weight += repeats * 0.7
    
    # Step 5: Normalize by number of unique event types
    unique_event_types = len(set(entry['level'] for entry in log_entries))
    normalized_score = total_weight / unique_event_types
    
    # Step 6: Final adjustment using character pattern (actual use of frequency_map)
    max_freq = max(frequency_map.values())
    min_freq = min(frequency_map.values())
    imbalance_factor = (max_freq - min_freq) * 0.05
    final_score = normalized_score + imbalance_factor
    
    return final_score

# Dead code: recursive checksum (never called)
def recursive_checksum(seq, acc=0):
    if not seq:
        return acc % 256
    return recursive_checksum(seq[1:], acc ^ seq[0])

# Another distraction: zipped time differences (computed but unused)
time_deltas = [event_log[i+1]['time'] - event_log[i]['time'] for i in range(len(event_log)-1)]
zip_result = [t for t, e in zip(time_deltas, event_log[:-1]) if e['level'] == 'ERROR']

# Key execution point
final_diagnostic = compute_integrity_score(event_log, system_flags)

# Output result as required
print(f"Target result: {final_diagnostic}")