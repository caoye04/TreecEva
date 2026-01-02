def preprocess_log_entry(entry):
    # Irrelevant preprocessing function (dead code path)
    return entry.strip().lower()


def calculate_checksum(data):
    # Distractor: checksum calculation not used in final result
    checksum = 0
    for char in data:
        checksum ^= ord(char)
    return checksum


def decode_signal_pattern(pattern):
    # Another decoy function with complex but unused logic
    decoded = 0
    for i, bit in enumerate(reversed(pattern)):
        if bit == '1':
            decoded += (2 ** i) * (i % 3 + 1)
    return decoded


def count_critical_events(logs):
    # Relevant function: counts events where severity > 7
    count = 0
    for log in logs:
        if 'severity' in log and log['severity'] > 7:
            count += 1
    return count


def apply_threshold_filter(value, thresholds, category):
    # Used in main logic; applies dynamic threshold from dict
    base = thresholds.get(category, 0)
    return value > base * 1.5


def recursive_data_fold(values, depth=0):
    # Complex-looking but ultimately irrelevant recursion
    if depth >= 3 or len(values) < 2:
        return len(values)
    mid = len(values) // 2
    left = recursive_data_fold(values[:mid], depth + 1)
    right = recursive_data_fold(values[mid:], depth + 1)
    return left ^ right


def analyze_system_faults(logs, thresholds):
    # Core logic hidden among distractions
    fault_tally = {}
    temp_buffer = []

    for log in logs:
        tag = log['tag']
        code = log['code']
        severity = log['severity']

        # Real logic begins here
        if tag not in fault_tally:
            fault_tally[tag] = 0

        # Meaningful condition using dictionary and comparison
        if apply_threshold_filter(severity, thresholds, tag):
            fault_tally[tag] += 1

        # Red herring: appending to unused buffer
        temp_buffer.append(f"{tag}:{code}-{calculate_checksum(str(code))}")

    # Real aggregation step
    total_faults = sum(fault_tally.values())

    # Decoy transformation chain
    transformed = ''
    for key in fault_tally:
        transformed += chr((ord(key[0]) + fault_tally[key]) % 26 + 97)

    # Final computation involving bitwise and arithmetic mix
    magic_offset = 1337
    entropy_seed = len(transformed) ^ 5

    # Actual answer derivation
    intermediate = (total_faults * 42) + (entropy_seed << 2)
    final_diagnostic = intermediate - (magic_offset & 255)

    # Unused recursive call (distractor)
    _ = recursive_data_fold([final_diagnostic, total_faults])

    return final_diagnostic

# Simulated system logs (real input data)
system_logs = [
    {'tag': 'power', 'code': 501, 'severity': 8},
    {'tag': 'network', 'code': 603, 'severity': 6},
    {'tag': 'power', 'code': 502, 'severity': 9},
    {'tag': 'sensor', 'code': 801, 'severity': 10},
    {'tag': 'network', 'code': 605, 'severity': 8},
    {'tag': 'sensor', 'code': 802, 'severity': 7},  # Below threshold after scaling
    {'tag': 'thermal', 'code': 701, 'severity': 11},
]

# Threshold configuration (dictionary operation)
threshold_map = {
    'power': 5,
    'network': 4,
    'sensor': 6,
    'thermal': 7
}

# Dead variable assignments (irrelevant)
dummy_logs = [preprocess_log_entry(f"LOG_{i}") for i in range(5)]
raw_patterns = ['1010', '1100', '0011']
processed_signals = [decode_signal_pattern(p) for p in raw_patterns]

# Key execution point
final_diagnostic = analyze_system_faults(system_logs, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")