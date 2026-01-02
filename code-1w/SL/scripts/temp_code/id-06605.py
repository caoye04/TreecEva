import math

# Simulated telemetry data from distributed system nodes
def collect_telemetry():
    timestamps = [1623456780 + i*30 for i in range(20)]
    cpu_loads = [abs(math.sin(i * 0.3)) * 100 for i in range(20)]
    memory_usage = [abs(math.cos(i * 0.25)) * 8000 for i in range(20)]
    packet_loss = [(i % 7) * 0.01 for i in range(20)]
    return list(zip(timestamps, cpu_loads, memory_usage, packet_loss))

# Irrelevant auxiliary function - dead code path
def analyze_quantum_flux():
    base = 0.0
    for i in range(1000):
        base += (i % 97) * 0.001
    return round(base, 3)

# Secondary diagnostic chain with misleading intermediate values
def compute_stability_index(raw_data):
    stability_scores = []
    for t, cpu, mem, loss in raw_data:
        score = 100 - cpu * 0.5 - (mem / 100) * 0.3 - loss * 50
        stability_scores.append(max(score, 0))
    return stability_scores

# Distractor: unused transformation
def transform_coordinates(x, y):
    theta = math.atan2(y, x)
    r = math.sqrt(x*x + y*y)
    return r * math.cos(theta * 2), r * math.sin(theta * 2)

# Critical path: timing analysis with red herring variables
failure_flags = []
timing_log = []
dummy_buffer = [0] * 50

raw_telemetry = collect_telemetry()

for idx, (ts, cpu, mem, loss) in enumerate(raw_telemetry):
    # Real processing
    if loss > 0.03:
        failure_flags.append((idx, ts))
    
    # Distractor block: fills buffer with irrelevant data
    phase = idx % 5
    for j in range(phase * 2):
        dummy_buffer[idx + j] += (cpu * mem) % 7
    
    # Real timing logic
    if idx > 0 and idx % 4 == 0:
        time_diff = raw_telemetry[idx][0] - raw_telemetry[idx-4][0]
        timing_log.append(time_diff)

# Another decoy function that is never called
def calculate_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Misleading precomputation with plausible but unused result
baseline_shift = sum([math.tan(i * 0.1) for i in range(10)]) / 10
adjusted_timing = [t - baseline_shift for t in timing_log]

# Core algorithm disguised among distractors
sequence_weights = [1, 2, 1, 3]
def weighted_pattern_match(data, weights):
    if len(data) < len(weights):
        return 0
    return sum(d * w for d, w in zip(data[-len(weights):], weights))

# Critical aggregation function containing answer derivation
intermediate_result = 0
def aggregate_metrics(times, failures):
    global intermediate_result
    cumulative = 0
    
    # Real contribution
    for t in times:
        cumulative += t // 100
    
    # Distractor: complex but unused bitwise logic
    flag_state = 0
    for pos, _ in failures:
        flag_state ^= pos << 2
        flag_state += pos * 3
    
    # More misdirection: combinatorics with no impact
    combinations = 0
    for i in range(len(failures)):
        for j in range(i+1, len(failures)):
            combinations += (failures[i][0] + failures[j][0]) % 5
    
    # Actual answer computation buried here
    pattern_value = weighted_pattern_match(timing_log, sequence_weights)
    intermediate_result = pattern_value
    
    # Final result combines relevant and irrelevant elements
    # BUT only pattern_value matters
    result = pattern_value * 7 - len(dummy_buffer) + flag_state // 100
    return result

# Execute main logic
stability_data = compute_stability_index(raw_telemetry)
system_baseline = sum(stability_data) / len(stability_data)

# Key statement - target of the question
final_diagnostic = aggregate_metrics(timing_log, failure_flags)

# Print required output
print(f"Result: {final_diagnostic}")