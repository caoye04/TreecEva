import itertools

def analyze_sequence(data):
    # Irrelevant function: analyzes character frequency but not used in final result
    freq = {}
    for item in data:
        for c in str(item):
            if c.isdigit():
                freq[c] = freq.get(c, 0) + 1
    return {k: v for k, v in sorted(freq.items())}

def validate_checksum(sequence):
    # Unused validation logic (dead code path)
    total = 0
    for i, val in enumerate(sequence):
        total += val * (i + 1)
    return total % 7 == 0

def transform_record(record_list):
    # Distractor transformation with bit manipulation
    shifted = []
    for x in record_list:
        temp_val = (x << 2) ^ 5
        if temp_val > 100:
            temp_val = temp_val // 3
        shifted.append(temp_val % 47)
    return shifted

def compute_health_score(entries):
    # Complex but irrelevant health scoring with string processing
    labels = ['stable', 'warning', 'critical', 'info']
    score = 0
    for entry in entries:
        text = entry.get('msg', '')
        lower_text = text.lower()
        words = lower_text.split()
        for word in words:
            cleaned = word.strip('.,!?"')
            if cleaned in labels:
                score += len(cleaned)
    return score * 1.5

def filter_anomalies(data_stream):
    # Red herring filtering based on modular arithmetic
    anomalies = []
    for item in data_stream:
        if isinstance(item, dict) and 'value' in item:
            val = item['value']
            if val % 13 == 0 or (val & 7) == 4:
                anomalies.append(val)
    return anomalies

def extract_signatures(event_log):
    # Unused signature extraction using itertools
    groups = []
    sorted_log = sorted(event_log, key=lambda x: x['timestamp'])
    for key, group in itertools.groupby(sorted_log, key=lambda x: x['type']):
        groups.append(list(group))
    signatures = []
    for g in groups:
        sig = sum(e['code'] for e in g) * len(g)
        signatures.append(sig)
    return signatures

def process_metrics(log_entries, system_flags):
    # Core logic buried within distractions
    base_accumulator = 0
    trigger_count = 0

    # Key data processing loop
    for entry in log_entries:
        if not isinstance(entry, dict):
            continue
        if 'status' not in entry or 'retry' in entry:
            continue

        status_code = entry['status']
        timestamp = entry['timestamp']

        # Critical condition: only count specific patterns
        if status_code >= 400 and timestamp % 2 == 1:
            base_accumulator += status_code // 100
            trigger_count += 1

        # Secondary path - appears important but contributes minimally
        if 'details' in entry and isinstance(entry['details'], list):
            sub_val = 0
            for d in entry['details']:
                if isinstance(d, dict) and 'flag' in d:
                    sub_val ^= d['flag']
            base_accumulator += sub_val & 3  # Minor contribution

    # Final computation using system flags
    flag_modifier = 0
    for flag in system_flags:
        # Only specific flag values affect outcome
        if isinstance(flag, str):
            upper_flag = flag.upper()
            if 'DEBUG' in upper_flag:
                flag_modifier += 2
            elif 'TRACE' in upper_flag:
                flag_modifier -= 1

    # Real answer computed here
    intermediate = (base_accumulator * 17) + (trigger_count * 5)
    final_diagnostic = intermediate - (flag_modifier * 4)

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data with red herrings
log_entries = [
    {'status': 503, 'timestamp': 101, 'msg': 'Service Unavailable'},
    {'status': 404, 'timestamp': 102, 'retry': True, 'msg': 'Not Found'},
    {'status': 400, 'timestamp': 103, 'details': [{'flag': 7}, {'flag': 3}]},
    {'status': 500, 'timestamp': 105, 'msg': 'Server Error'},
    {'status': 200, 'timestamp': 107, 'msg': 'OK'},  # ignored (status < 400)
    {'status': 401, 'timestamp': 109, 'timestamp_extra': 999},  # no effect
    {'status': 403, 'timestamp': 111, 'details': []},
]

system_flags = ['DEBUG_MODE_ON', 'NETWORK_TRACE_ENABLED', 'STANDBY']

# Dead code invocations (distractors)
dead_freq = analyze_sequence([1123, 456, 789])
health_score = compute_health_score(log_entries)
anomaly_list = filter_anomalies(log_entries)
transformed_data = transform_record([10, 20, 30, 40, 50])
unused_sigs = extract_signatures([
    {'type': 'auth', 'code': 401, 'timestamp': 1000},
    {'type': 'api', 'code': 200, 'timestamp': 1001},
])

# Key execution point
final_diagnostic = process_metrics(log_entries, system_flags)