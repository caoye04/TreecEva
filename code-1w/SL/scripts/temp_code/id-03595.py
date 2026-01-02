import itertools
import math

# Simulate a system health monitoring module with diagnostic calculations

def analyze_response_time(rt):
    if rt < 0:
        return 'invalid'
    elif rt < 50:
        return 'optimal'
    elif rt < 200:
        return 'acceptable'
    else:
        return 'degraded'

def compute_entropy(data):
    # Irrelevant function: computes Shannon entropy but not used in final result
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def detect_anomalies(log_entries):
    # Dead code path — never called
    anomalies = []
    for entry in log_entries:
        if entry.get('response_time', 0) > 500:
            anomalies.append(entry['timestamp'])
    return anomalies

def generate_sequence(n):
    # Distractor: generates Fibonacci-like sequence but unused
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def validate_checksum(record):
    # Misleading intermediate: looks important but not part of main logic
    raw = str(record['timestamp']) + record['status']
    checksum = sum(ord(c) for c in raw) % 256
    return checksum == record.get('checksum', 0)

def filter_critical_events(events):
    # Unused filtering logic — red herring
    return [e for e in events if e['severity'] == 'CRITICAL']

def aggregate_metrics(log, error_list):
    base_score = 1000
    penalty = 0
    timing_adjustment = 0

    # Real logic begins here — deeply nested and mixed with noise
    for entry in log:
        rt = entry['response_time']
        status = entry['status']

        if status == 'FAIL':
            penalty += 15

        category = analyze_response_time(rt)

        if category == 'degraded':
            timing_adjustment += rt // 10
        elif category == 'acceptable':
            timing_adjustment += 5
        else:
            timing_adjustment += 2

        # Spurious internal calculation — distracts from real flow
        temp_flag = (rt % 7) == 0 and status == 'OK'
        if temp_flag:
            base_score -= 3  # minor hit, but misleading

    # Irrelevant character counting — mimics useful analysis
    all_statuses = ''.join(e['status'] for e in log)
    retry_count = all_statuses.count('RETRY')
    penalty += retry_count * 4

    # Core answer derivation buried in complexity
    final_diagnostic = base_score - penalty + timing_adjustment

    # Decoy mutation of final_diagnostic — never executed
    if False:
        final_diagnostic = int(math.sqrt(final_diagnostic) * 10)

    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated timing log — relevant data
    timing_log = [
        {'timestamp': 1678880001, 'response_time': 32, 'status': 'OK', 'checksum': 123},
        {'timestamp': 1678880002, 'response_time': 195, 'status': 'OK', 'checksum': 124},
        {'timestamp': 1678880003, 'response_time': 450, 'status': 'FAIL', 'checksum': 125},
        {'timestamp': 1678880004, 'response_time': 120, 'status': 'RETRY', 'checksum': 126},
        {'timestamp': 1678880005, 'response_time': 600, 'status': 'FAIL', 'checksum': 127}
    ]

    # Errors list — relevant
    errors_occurred = ['E_TIMEOUT', 'E_NETWORK']

    # Irrelevant data structures — distract with plausible context
    user_sessions = [{'uid': 'a1', 'duration': 300}, {'uid': 'a2', 'duration': 450}]
    system_flags = {"maintenance": False, "audit_mode": True, "debug_level": 9}
    entropy_data = [1, 1, 2, 2, 3, 3, 4]

    # Unused itertools operation — looks sophisticated but irrelevant
    rolling_windows = list(itertools.pairwise(generate_sequence(6)))

    # Key computation embedded among distractions
    final_diagnostic = aggregate_metrics(timing_log, errors_occurred)

    # Print required output
    print(f"Target result: {final_diagnostic}")