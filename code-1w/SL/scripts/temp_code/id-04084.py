from collections import defaultdict, Counter
import math

# Simulated telemetry data from distributed nodes
def collect_telemetry(nodes):
    data = defaultdict(list)
    for i in range(len(nodes)):
        node = nodes[i]
        if i % 3 == 0:
            data[node].extend([1.1, 2.2, 3.3])
        elif i % 3 == 1:
            data[node].extend([4.4, 5.5])
        else:
            data[node].extend([6.6, 7.7, 8.8, 9.9])
    return data

# Misleading function: appears important but unused in final calculation
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Auxiliary diagnostic with red herring variables
def analyze_patterns(logs):
    pattern_score = 0
    sequence = [len(entry) for entry in logs if len(entry) > 2]
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            pattern_score += 2
        else:
            pattern_score -= 1
    
    # Dead code path - never reached due to prior logic
    if False and pattern_score < 0:
        correction_factor = 100
        pattern_score *= correction_factor
    
    return pattern_score

# Core stability evaluation with distractors
def evaluate_stability(entries, flags):
    base_score = 0
    temp_result = 0
    
    # Irrelevant transformation (distractor)
    normalized = [math.tanh(x / 10) for x in range(1, 5)]
    temp_result = sum(normalized)
    
    # Real computation begins
    critical_count = 0
    for log in entries:
        if 'ERROR' in log:
            critical_count += 1
        elif 'WARNING' in log:
            critical_count += 0.5
    
    # Bit manipulation red herring
    flag_state = 0
    for f in flags:
        if f == 'ACTIVE':
            flag_state |= 1
        flag_state <<= 1
    # Shift loop leaves flag_state with garbage value

    # Decoy aggregation (never used)
    stats_summary = {
        'max': max([critical_count, temp_result]),
        'min': min([critical_count, temp_result]),
        'range': abs(max([critical_count, temp_result]) - min([critical_count, temp_result]))
    }
    
    # Actual decision logic (nested conditionals + arithmetic)
    if critical_count >= 3:
        base_score = 100 * (4 - critical_count)
    elif critical_count > 1:
        adjustment = 0
        for i in range(5):
            if i % 2 == 0:
                adjustment += i ** 2
            else:
                adjustment -= i
        base_score = 50 + int(adjustment / 2)
    else:
        base_score = 20
    
    # Final interference: redundant transformation
    multiplier = 1
    history = [base_score]
    for _ in range(3):
        history.append(history[-1] + 2 * multiplier)
        multiplier *= -1
    
    # Key assignment - this is the real answer
    final_diagnostic = base_score + 17
    
    # Extra print to mislead tracing (not the target)
    # print(f'Debug: {temp_result}, {flag_state}, {stats_summary}')
    
    return final_diagnostic

# Unused utility: simulates load balancing (distractor)
def rebalance_tasks(tasks, workers):
   分配 = defaultdict(int)
    for i, task in enumerate(tasks):
        分配[workers[i % len(workers)]] += task
    return dict(分配)

# Main execution flow
if __name__ == '__main__':
    nodes = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    raw_logs = collect_telemetry(nodes)
    
    # Construct log entries with meaningful content
    log_entries = [
        ['INFO: boot', 'INFO: sync', 'WARNING: latency'],
        ['INFO: boot', 'ERROR: timeout', 'ERROR: disconnect'],
        ['INFO: boot', 'WARNING: retry'],
        ['INFO: boot', 'INFO: sync'],
        ['ERROR: timeout', 'WARNING: fallback']
    ]
    
    # System flags with mixed states
    system_flags = ['STANDBY', 'ACTIVE', 'IDLE', 'ACTIVE', 'HALTED']
    
    # Irrelevant counters (red herrings)
    anomaly_count = 0
    for log in log_entries:
        for entry in log:
            if 'timeout' in entry:
                anomaly_count += 1
    
    performance_snapshot = [1.1, 2.2, 3.3, 4.4]
    snapshot_sum = sum(performance_snapshot)
    
    # Critical execution point
    final_diagnostic = evaluate_stability(log_entries, system_flags)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")