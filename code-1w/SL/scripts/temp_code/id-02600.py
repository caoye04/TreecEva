from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'NODE_1|TEMP:78|STATUS:OK|LOAD:0.45',
    'NODE_2|TEMP:85|STATUS:WARN|LOAD:0.67',
    'NODE_3|TEMP:92|STATUS:FAIL|LOAD:0.89',
    'NODE_1|TEMP:79|STATUS:OK|LOAD:0.51',
    'NODE_4|TEMP:88|STATUS:WARN|LOAD:0.74',
    'NODE_2|TEMP:95|STATUS:FAIL|LOAD:0.92',
    'NODE_5|TEMP:73|STATUS:OK|LOAD:0.33'
]

# Irrelevant auxiliary mapping (distractor)
node_regions = {
    'NODE_1': 'NORTH', 'NODE_2': 'EAST',
    'NODE_3': 'WEST', 'NODE_4': 'SOUTH',
    'NODE_5': 'CENTRAL'
}

# Dead function - never called (red herring)
def calculate_geo_score(region):
    base = len(region) * 1.5
    return round(base ** 1.2, 2)

# Misleading intermediate aggregator (unused)
shadow_aggregate = defaultdict(list)
for entry in telemetry_stream:
    node = entry.split('|')[0]
    temp = float(entry.split('|')[1].split(':')[1])
    shadow_aggregate[node_regions[node]].append(temp)

# Primary parsing function
def parse_log_entry(entry):
    parts = entry.split('|')
    node_id = parts[0]
    temperature = float(parts[1].split(':')[1])
    status = parts[2].split(':')[1]
    load = float(parts[3].split(':')[1])
    return (node_id, temperature, status, load)

# Extract all logs
parsed_logs = [parse_log_entry(log) for log in telemetry_stream]

# Build node-specific history (used later)
node_history = defaultdict(list)
for record in parsed_logs:
    node_history[record[0]].append((record[1], record[3]))  # (temp, load)

# Decoy transformation using list comprehension (irrelevant)
normalized_pairs = [
    (round(math.log(rec[1] + 1), 3), rec[3] ** 0.5)
    for rec in parsed_logs if rec[2] == 'OK'
]

# Fake correlation matrix (dead code path)
correlation_hint = {
    (i, j): round(abs(0.5 + i*0.1 - j*0.05), 3)
    for i in range(3) for j in range(3)
}

# Unused statistical summary (distractor)
status_count = Counter([r[2] for r in parsed_logs])

# Core processing function with conditional logic and nesting
def analyze_node_risk(metrics_list, threshold_temp=80, critical_load=0.85):
    high_risk_events = 0
    for temp, load in metrics_list:
        # First condition: high temp or high load
        if temp > threshold_temp:
            # Second level: check severity
            if load > critical_load:
                # Third level: compound risk factor
                risk_factor = (temp / 100.0) * (load ** 2)
                if risk_factor > 0.7:
                    high_risk_events += 1
    return high_risk_events

# Secondary metric: stability score (partially used)
def compute_stability(records):
    if len(records) < 2:
        return 0.0
    temp_changes = [abs(records[i][0] - records[i-1][0]) for i in range(1, len(records))]
    avg_fluctuation = sum(temp_changes) / len(temp_changes)
    return round(10.0 / (1 + avg_fluctuation), 2) if avg_fluctuation > 0 else 10.0

# Auxiliary weight calculator (misleading intermediate)
def calculate_weighted_index(data):
    weights = [0.3, 0.5, 0.7, 1.0][:len(data)]
    weighted = sum(w * v[0] for w, v in zip(weights, data))
    return weighted / sum(weights) if weights else 0

# Main metric processor
def process_metrics(log_data, system_threshold):
    node_risks = {}
    stability_scores = {}
    
    for node, history in node_history.items():
        # Compute risk count
        risk_count = analyze_node_risk(history, threshold_temp=system_threshold)
        node_risks[node] = risk_count
        
        # Compute stability
        stability = compute_stability(history)
        stability_scores[node] = stability
    
    # Aggregate total risk events
    total_risks = sum(node_risks.values())
    
    # Composite diagnostic score
    raw_score = 0
    for node in node_risks:
        # Complex interaction between risk and stability
        if stability_scores[node] < 5.0 and node_risks[node] > 0:
            raw_score += node_risks[node] * 2
        elif node_risks[node] > 0:
            raw_score += node_risks[node]
    
    # Final nonlinear transformation
    final_score = int((raw_score ** 1.5) * 10)
    
    # Key assignment point
    final_diagnostic = final_score
    
    return final_diagnostic

# System threshold configuration
system_threshold = 82

# Execute main logic
final_diagnostic = process_metrics(telemetry_stream, system_threshold)

print(f"Result: {final_diagnostic}")