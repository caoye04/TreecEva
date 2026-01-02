from itertools import groupby

def analyze_log_patterns(log_data):
    # Irrelevant preprocessing: counts per character (distractor)
    char_frequency = {}
    for entry in log_data:
        for char in entry:
            char_frequency[char] = char_frequency.get(char, 0) + 1

    # Semi-relevant transformation: extract numeric codes
    numeric_codes = []
    for entry in log_data:
        digits = ''.join([c for c in entry if c.isdigit()])
        if digits:
            numeric_codes.append(int(digits) % 100)

    return sorted(numeric_codes)

def calculate_remaining_capacity(log_entries, system_threshold):
    # Extract operation codes from logs
    op_codes = [int(''.join(filter(str.isdigit, entry))[:2]) for entry in log_entries if any(c.isdigit() for c in entry)]
    
    # Track state with distractor variables
    temp_snapshot = set()
    historical_load = []
    for code in op_codes:
        temp_snapshot.add(code % 13)  # Distractor: tracks modulo pattern
        historical_load.append(code * 0.95)  # Irrelevant floating point trail

    # Core logic: group and filter meaningful operations
    filtered_ops = [code for code in op_codes if code > 25]
    grouped_ops = [list(group) for k, group in groupby(sorted(filtered_ops)) if k != 0]
    
    # Real computation: capacity based on unique group sizes and threshold
    base_capacity = len(filtered_ops)
    modifier = sum(len(g) for g in grouped_ops if sum(g) > system_threshold)
    adjustment = len(temp_snapshot.intersection({5, 7, 11}))  # Minor influence from distractor set
    
    # Final capacity calculation
    final_capacity = base_capacity * 2 - modifier + adjustment
    return final_capacity

# Simulated system log entries
logs = [
    "ERR_45_CRITICAL", "WARN_32_RESET", "INFO_12_NOOP", "TASK_67_START",
    "SYNC_45_RETRY", "FLOW_89_INIT", "META_07_SKIP", "DATA_67_COMMIT",
    "LOCK_23_WAIT", "EXEC_91_RUN"
]

system_limit = 50

# Call analysis (irrelevant to final result but adds interference)
usage_pattern = analyze_log_patterns(logs)

# Key statement that produces the answer
final_capacity = calculate_remaining_capacity(logs, system_limit)

print(f"Result: {final_capacity}")