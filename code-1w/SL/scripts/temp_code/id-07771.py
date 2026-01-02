import itertools

# Simulated system telemetry data for performance analysis
def collect_telemetry():
    timestamps = list(range(100, 200, 3))
    cpu_loads = [t % 77 + (t * 0.1) % 5 for t in timestamps]
    memory_usage = [(t + 50) % 88 for t in timestamps]
    disk_reads = [abs((t * 2) % 100 - 45) for t in timestamps]
    network_events = [t % 13 == 0 for t in timestamps]  # unused distractor
    return list(zip(timestamps, cpu_loads, memory_usage, disk_reads))

def filter_anomalies(data):
    # Filter entries where CPU > 60 and memory > 50
    filtered = [d for d in data if d[1] > 60 and d[2] > 50]
    # Dead path: never used
    if len(filtered) > 100:
        return filtered[:50]
    return filtered

def compute_efficiency_ratio(entries):
    total_cpu = sum(e[1] for e in entries)
    total_mem = sum(e[2] for e in entries)
    count = len(entries)
    if count == 0:
        return 0.0
    base_ratio = total_cpu / (total_mem + 1)
    adjustment = (total_cpu % 7) / 10.0
    return round(base_ratio + adjustment, 4)

def generate_combinations(entries):
    # Irrelevant combinatorial explosion - red herring
    indices = list(range(len(entries)))
    combos = list(itertools.combinations(indices, 3))
    hashed = sum(hash(c) % 1000 for c in combos[:100]) if combos else 0
    _ = [x * 2 for x in combos]  # dead computation
    return len(combos)

def assess_stability(cpu_series):
    diffs = [abs(cpu_series[i+1] - cpu_series[i]) for i in range(len(cpu_series)-1)]
    volatility = sum(diffs) / len(diffs) if diffs else 0
    return volatility < 15

def extract_key_signals(telemetry_data):
    signals = []
    for entry in telemetry_data:
        ts, cpu, mem, disk = entry
        if cpu > 70 or mem > 75:
            signals.append((ts, int(cpu), int(mem)))
    return signals

def mock_calibration(signal_data):
    # Useless calibration with set operations
    times = {s[0] for s in signal_data}
    cpu_set = {s[1] for s in signal_data}
    mem_set = {s[2] for s in signal_data}
    intersections = cpu_set & mem_set
    union_all = cpu_set | mem_set | times
    diff_ops = len(union_all) - len(intersections)
    _ = {x - 5 for x in intersections if x > 50}  # unused
    return diff_ops * 0.1  # minor decoy influence

def aggregate_performance(log_entries, system_flags):
    # Core logic begins
    anomalies = filter_anomalies(log_entries)
    efficiency = compute_efficiency_ratio(anomalies)
    signals = extract_key_signals(log_entries)
    stability = assess_stability([e[1] for e in log_entries])
    
    # Critical distractor block
    combo_count = generate_combinations(log_entries)
    calibration_factor = mock_calibration(signals)
    entropy_proxy = combo_count % 100
    
    # Real calculation chain
    base_score = efficiency * 100
    adjusted_score = base_score + (entropy_proxy * 0.5)
    
    # Conditional modulation based on stability
    if stability:
        adjusted_score *= 1.15
    else:
        adjusted_score *= 0.85
    
    # Final interference: irrelevant flag interaction
    flag_value = sum(system_flags) % 3
    if flag_value == 1:
        adjusted_score += 10
    elif flag_value == 2:
        adjusted_score -= 5
    # flag_value == 0 has no effect - adds branching confusion
    
    final_score = int(round(adjusted_score))
    return final_score

# Main execution flow
telemetry_logs = collect_telemetry()
system_flags = [1, 0, 1, 1, 0, 0, 1]  # arbitrary flags

# Key statement
final_score = aggregate_performance(telemetry_logs, system_flags)
print(f"Result: {final_score}")