from collections import defaultdict, Counter

# Simulated sensor data stream with multiple diagnostic channels
def generate_telemetry():
    return [
        (1, 'CPU', 78), (2, 'MEM', 85), (3, 'CPU', 80), (4, 'NET', 45),
        (5, 'DISK', 90), (6, 'MEM', 88), (7, 'CPU', 82), (8, 'NET', 50),
        (9, 'DISK', 92), (10, 'MEM', 90), (11, 'CPU', 85), (12, 'NET', 55)
    ]

def analyze_sequence(seq):
    # Irrelevant transformation: creates a red herring using enumerate
    indexed = [(i, x) for i, x in enumerate(seq) if x[0] % 2 == 1]
    reversed_seq = [x[::-1] for x in seq]  # Distractor: never used
    return {k: [v for _, k, v in seq if k == 'CPU'] for _, k, v in seq}

def compute_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [float(x) / total for x in data]
    entropy = 0.0
    for p in probs:
        if p > 0:
            entropy -= p * __import__('math').log(p, 2)
    return round(entropy, 6)

def filter_critical(entries, threshold=85):
    # Dead code path: this function is defined but not used
    return [e for e in entries if e[2] >= threshold]

def build_lookup(telemetry):
    lookup = defaultdict(list)
    for ts, resource, val in telemetry:
        lookup[resource].append(val)
    return lookup

def evaluate_stability(trace):
    stability_score = 0
    for i in range(1, len(trace)):
        stability_score += abs(trace[i] - trace[i-1])
    return stability_score < 15

def aggregate_diagnostics(logs):
    # Misleading aggregation: looks important but unused in final result
    flat = [entry for entry in logs if entry[1] in ('CPU', 'MEM')]
    grouped = defaultdict(list)
    for t, r, v in flat:
        grouped[r].append(v)
    stats = {}
    for r, vals in grouped.items():
        stats[r] = {
            'avg': sum(vals) / len(vals),
            'peak': max(vals),
            'critical_count': len([v for v in vals if v > 85])
        }
    return stats  # Unused return

def process_metrics(trace, logbook):
    # Core logic embedded within distractions
    cpu_readings = [v for t, r, v in trace if r == 'CPU']
    mem_readings = [v for t, r, v in trace if r == 'MEM']
    
    # Distractor variables
    dummy_matrix = [[i*j for j in range(3)] for i in range(3)]
    temp_registry = {'init': True, 'stage': 'diagnostic'}
    
    # Key intermediate computation
    cpu_avg = sum(cpu_readings) / len(cpu_readings)
    mem_avg = sum(mem_readings) / len(mem_readings)
    
    # Another red herring: complex but unused structure
    zipped_data = list(zip(cpu_readings, mem_readings, strict=False))
    derived_features = [abs(a - b) for a, b in zipped_data[:len(cpu_readings)]]
    
    # Critical branching logic
    base_score = 0
    if cpu_avg > 80:
        base_score += 20
    if mem_avg > 85:
        base_score += 30
    
    # Decoy conditional block with misleading comments
    # NOTE: This block adjusts for network jitter (FALSE LEAD)
    net_vals = [v for t, r, v in trace if r == 'NET']
    if len(net_vals) > 0 and sum(net_vals) / len(net_vals) < 50:
        base_score += 10  # Never reached due to data
    
    # Real adjustment based on disk trend (subtle)
    disk_vals = [v for t, r, v in trace if r == 'DISK']
    disk_increasing = all(disk_vals[i] <= disk_vals[i+1] for i in range(len(disk_vals)-1))
    if disk_increasing:
        base_score -= 15  # Actual deduction
    
    # Final transformation using entropy (key concept)
    entropy_value = compute_entropy(cpu_readings + mem_readings)
    final_diagnostic = int(base_score + (entropy_value * 100))
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
telemetry_stream = generate_telemetry()
system_log = aggregate_diagnostics(telemetry_stream)  # Call with no effect
health_trace = analyze_sequence(telemetry_stream)
final_diagnostic = process_metrics(telemetry_stream, system_log)