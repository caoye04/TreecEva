import itertools

def simulate_network_traffic(base_load, duration):
    # Irrelevant simulation function (dead end)
    traffic = []
    for t in range(duration):
        fluctuation = (t % 7) ** 2 % 11
        traffic.append(base_load + fluctuation - 5)
    return traffic

def collect_metrics(raw_logs):
    # Distractor: processes logs but returns unused structure
    parsed = [line.split(',') for line in raw_logs if 'ERROR' not in line]
    timestamps = [p[0] for p in parsed if len(p) > 0]
    levels = {p[1] for p in parsed if len(p) > 1}  # set operation (irrelevant)
    return {'timestamps': timestamps, 'levels': levels}

def compute_health_score(nodes):
    # Misleading function with intermediate result that looks important
    scores = []
    for node in nodes:
        raw = sum(ord(c) for c in node) % 100
        adjusted = raw * 0.95 if 'backup' in node else raw * 1.05
        scores.append(adjusted)
    return sum(scores) / len(scores) if scores else 0

def detect_anomalies(stream):
    # Looks useful but not part of critical path
    anomalies = []
    for i in range(1, len(stream)):
        if abs(stream[i] - stream[i-1]) > 15:
            anomalies.append(i)
    return anomalies

def find_root_cause(data):
    # Core logic buried among distractions
    windowed = [sum(data[i:i+3]) for i in range(len(data)-2)]
    filtered = [w for w in windowed if w > 60]
    if not filtered:
        return max(data)
    pivot = filtered[len(filtered)//2]
    shifted = pivot >> 2  # Bit manipulation red herring
    masked = shifted & 0xFF
    return masked + 17

def analyze_path(triage_code):
    # Critical transformation
    seq = list(range(triage_code - 4, triage_code + 4))
    chunks = [seq[i:i+3] for i in range(0, len(seq), 3)]
    transposed = list(itertools.zip_longest(*chunks, fillvalue=0))  # itertools basic use
    flattened = [item for sublist in transposed for item in sublist]
    trimmed = flattened[2:-2]  # slicing operation
    aggregate = sum(trimmed) // len(trimmed)
    
    # Decoy conditional
    if aggregate < 100:
        secondary_check = set(trimmed)  # set operation
        aggregate += len(secondary_check)
    
    return aggregate * 2

def main():
    # Initialization with plausible but partially irrelevant data
    raw_logs = [
        '12:00,INFO,serverA',
        '12:05,WARN,serverB',
        '12:10,INFO,serverC'
    ]
    
    system_nodes = ['router_main', 'switch_core', 'firewall_edge', 'backup_nas']
    base_latency_spike = [23, 45, 67, 89, 34, 78, 91, 12, 56]
    extended_load = base_latency_spike * 2
    
    # Irrelevant calls
    _ = collect_metrics(raw_logs)
    _ = compute_health_score(system_nodes)
    _ = detect_anomalies(extended_load)
    _ = simulate_network_traffic(10, 20)
    
    # Critical path starts here
    latency_data = [x + (x % 10) for x in base_latency_spike if x % 2 == 1]
    root_cause_code = find_root_cause(latency_data)
    final_diagnostic = analyze_path(root_cause_code)
    
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()