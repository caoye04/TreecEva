from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'CPU:85|MEM:45|NET:up|TEMP:62',
    'CPU:70|MEM:50|NET:down|TEMP:58',
    'CPU:90|MEM:60|NET:up|TEMP:75',
    'CPU:40|MEM:30|NET:up|TEMP:45'
]

# Irrelevant lookup table for deprecated systems
legacy_mapping = {
    'A1': 'X001', 'A2': 'X002', 'B1': 'Y100', 'B2': 'Y101',
    'C1': 'Z999', 'D4': 'W004', 'E5': 'V888', 'F6': 'U777'
}

# Fake checksum validator (never used)
def validate_checksum(data):
    acc = 0
    for c in data:
        if c.isalpha():
            acc += ord(c) % 17
        elif c.isdigit():
            acc += int(c) * 3
    return acc % 13 == 0

# Misleading preprocessing function that looks important but is partially unused
def parse_telemetry(stream):
    records = []
    temp_stats = defaultdict(int)
    usage_histogram = [0]*100
    
    for line in stream:
        parts = line.split('|')
        record = {}
        for part in parts:
            k, v = part.split(':')
            if k == 'CPU' or k == 'MEM' or k == 'TEMP':
                record[k] = int(v)
                usage_histogram[int(v)] += 1
            else:
                record[k] = v
        
        # Real computation
        record['risk'] = 'high' if record['CPU'] > 80 and record['TEMP'] > 70 else 'normal'
        
        # Dead code path - never accessed later
        if record.get('NET') == 'down':
            temp_stats['network_outage'] += 1

        records.append(record)
    
    # Red herring computation
    avg_temp = sum(r['TEMP'] for r in records) / len(records)
    peak_cpu = max(r['CPU'] for r in records)
    
    # This mutation has no effect on final result
    for r in records:
        if r['TEMP'] > avg_temp:
            r['cooling_needed'] = True

    return records

# Decoy function - looks related but unused in main flow
def analyze_failures(parsed):
    failures = 0
    for r in parsed:
        if r['risk'] == 'high' and r.get('NET') == 'down':
            failures += 1
    return failures

# Core processing function with subtle logic
system_state = {'mode': 'active', 'version': '3.7.1', 'nodes': 4}

def compute_stability_index(records, state):
    base_score = 100.0
    penalty = 0
    
    # Real logic starts here
    high_risk_count = 0
    for r in records:
        if r['risk'] == 'high':
            high_risk_count += 1
            penalty += 15

    # Conditional bonus based on node count
    if state['nodes'] >= 4:
        base_score += 10
    
    # Nested adjustment
    if high_risk_count > 1:
        base_score -= penalty
        if state['version'].startswith('3'):
            base_score -= 5
            # Critical branch
            if base_score > 50:
                base_score = 50 + (base_score - 50) * 0.5  # dampen
    else:
        base_score -= penalty // 2
    
    return round(base_score, 4)

# Another decoy transformation
def transform_records(data_list):
    flattened = []
    for item in data_list:
        flat = {}
        for k, v in item.items():
            if isinstance(v, str):
                flat[f'str_{k}'] = v.upper()
            else:
                flat[f'num_{k}'] = v * 1.1
        flattened.append(flat)
    return flattened

# Main diagnostic processor - this is where the answer comes from
def process_metrics(logs, sys_state):
    parsed_logs = parse_telemetry(logs)
    
    # Extract meaningful metrics
    cpu_loads = [r['CPU'] for r in parsed_logs]
    mem_uses = [r['MEM'] for r in parsed_logs]
    
    # Real computation chain
    avg_cpu = sum(cpu_loads) / len(cpu_loads)
    avg_mem = sum(mem_uses) / len(mem_uses)
    
    # Intermediate distraction
    sorted_cpu = sorted(cpu_loads)
    median_cpu = (sorted_cpu[1] + sorted_cpu[2]) / 2
    
    # Key metric: efficiency ratio
    if avg_mem > 0:
        efficiency = avg_cpu / avg_mem
    else:
        efficiency = float('inf')
    
    # Data structure manipulation red herring
    resource_counter = Counter()
    for r in parsed_logs:
        resource_counter['total'] += 1
        if r['risk'] == 'high':
            resource_counter['high_risk'] += 1
    
    # Dead assignment
    resource_summary = dict(resource_counter)
    
    # Final stability index is the real answer source
    stability = compute_stability_index(parsed_logs, sys_state)
    
    # Final diagnostic calculation - depends only on stability and efficiency
    if efficiency > 1.5:
        final_value = stability * 1.2
    else:
        final_value = stability * 0.8
    
    # THIS IS THE TARGET VARIABLE
    final_diagnostic = int(round(final_value))

    # Unrelated print that looks important
    debug_dump = {"stability": stability, "efficiency": efficiency}
    
    # Only this matters
    return final_diagnostic

# Execution flow
log_data = telemetry_stream
final_diagnostic = process_metrics(log_data, system_state)
print(f"Result: {final_diagnostic}")