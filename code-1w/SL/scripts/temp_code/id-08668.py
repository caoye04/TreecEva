from collections import defaultdict, Counter
import math

# Simulated system telemetry data (irrelevant to final result)
telemetry_buffer = [0.1, 0.4, 0.3, 0.9, 0.2]
buffer_sum = sum(telemetry_buffer)
normalized_power = buffer_sum / len(telemetry_buffer)

def analyze_telemetry(data):
    return sum(x ** 2 for x in data)  # Unused function - red herring

# Legacy diagnostic counters (distractor variables)
diag_counter_a = 0
diag_counter_b = 0
for i in range(50):
    if i % 10 == 0:
        diag_counter_a += 1
    if i % 25 == 0:
        diag_counter_b += 2

# Core data structure: process metrics log
def generate_metrics_log():
    log = defaultdict(float)
    log['throughput'] = 120.5
    log['latency'] = 45.2
    log['errors'] = 3
    log['retries'] = 1
    log['timeout_count'] = 0
    return log

metrics_log = generate_metrics_log()

# Irrelevant bit manipulation sequence (misleading intermediate)
temp_flag = 0b1010
mask = 0b1100
masked = temp_flag & mask
twisted = masked ^ 0b1111
shifted = twisted << 2

# Unused statistical transform (dead code path)
def compute_zscore(val, mean=50, std=15):
    return (val - mean) / std

# Spurious list processing (distractor logic)
event_queue = ['start', 'init', 'load', 'run', 'halt']
event_counter = Counter(event_queue)
event_entropy = 0
for count in event_counter.values():
    if count > 0:
        event_entropy -= (count / len(event_queue)) * math.log2(count / len(event_queue))

# Adjustment factor computed from unrelated formula (looks important)
raw_adjustment = math.sqrt(16) + math.log(1)
adjustment_factor = int(raw_adjustment)  # Results in 4

# Decoy function that appears related but is never called
def calculate_system_health(log):
    base = log['throughput'] - log['latency']
    penalty = log['errors'] * 10 + log['retries'] * 5
    return max(0, base - penalty)

# Key evaluation logic with nested conditions and dictionary access
def evaluate_performance(log, adj):
    base_score = 0
    
    # Criterion 1: throughput bonus
    if log['throughput'] > 100:
        base_score += 25
    
    # Criterion 2: latency penalty
    if log['latency'] > 40:
        base_score -= 10
    
    # Criterion 3: error penalties
    base_score -= log['errors'] * 7
    base_score -= log['retries'] * 3
    
    # Apply adjustment multiplier only if no timeouts
    if log['timeout_count'] == 0:
        base_score *= adj  # adj is 4
    else:
        base_score += 20
    
    # Nested bitwise check on transformed score (appears complex but deterministic)
    temp_score = int(abs(base_score))
    if (temp_score & 1) == 0:  # if even
        temp_score = temp_score ^ 0b1010  # toggle some bits
    temp_score = temp_score + (temp_score >> 2)  # add shifted version
    
    return temp_score

# Execute main logic
temp_var = math.sin(math.pi / 2)  # Red herring computation: equals 1.0
dummy_list = [x for x in range(10) if x % 3 == 0]  # Unused list

final_score = evaluate_performance(metrics_log, adjustment_factor)

print(f"Result: {final_score}")