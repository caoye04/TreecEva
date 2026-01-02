from collections import defaultdict, Counter

# Simulated system telemetry data
def collect_telemetry(nodes):
    telemetry = defaultdict(list)
    for node_id in nodes:
        if node_id % 3 == 0:
            telemetry['voltage'].append(12.1 + (node_id % 5))
        elif node_id % 4 == 0:
            telemetry['voltage'].append(11.8)
        else:
            telemetry['voltage'].append(12.0)
        telemetry['latency'].append((node_id * 7) % 101)
    return telemetry

def analyze_stability(metrics):
    stable_count = 0
    fluctuation_score = 0.0
    for i, v in enumerate(metrics['voltage']):
        if 11.9 <= v <= 12.1:
            stable_count += 1
        fluctuation_score += abs(v - 12.0)
    return stable_count, fluctuation_score

def compute_health_index(stable_count, score, size):
    # Irrelevant transformation (red herring)
    temp_offset = sum([i**2 for i in range(size//10)]) if size > 10 else 0
    base_index = (stable_count * 100) / size
    adjusted = base_index - (score / 5)
    return max(adjusted, 0)

def apply_calibration(data_list):
    # Dead code path - never actually used in final calculation
    calibrated = []
    for x in data_list:
        if isinstance(x, float):
            calibrated.append(round(x * 1.02, 3))
    return calibrated

def generate_diagnostics(flags):
    # Distractor function: generates unused diagnostics
    report = {}
    for flag in flags:
        report[f'flag_{flag}'] = (flag ^ 15) & 7
    # This function appears important but is not used in main logic
    return report

def extract_patterns(sequence):
    # Another decoy function analyzing bit patterns
    pattern_freq = Counter()
    for num in sequence:
        bin_rep = bin(num)[2:]
        ones = bin_rep.count('1')
        zeros = bin_rep.count('0')
        parity_bit = ones % 2
        pattern_freq[(ones, zeros, parity_bit)] += 1
    return dict(pattern_freq)

def filter_critical_nodes(node_data, threshold=50):
    critical = []
    for k, v_list in node_data.items():
        for v in v_list:
            if v > threshold:
                critical.append(k)
    return set(critical)

def process_metrics(entries, flags):
    # Core logic begins here
    voltage_data = [e['sensor_v'] for e in entries if 'sensor_v' in e]
    latency_data = [e['response_time'] for e in entries]
    
    # Bit manipulation red herring
    masked_values = []
    for val in voltage_data:
        shifted = int(val) << 2
        masked = shifted & 0xFF
        masked_values.append(masked)
    
    # Real processing starts
    avg_latency = sum(latency_data) / len(latency_data)
    median_voltage = sorted(voltage_data)[len(voltage_data)//2]
    
    # Key intermediate (misleading)
    preliminary_diag = (avg_latency * median_voltage) % 100
    
    # More distractions
    entropy_score = 0
    for i in range(1, len(latency_data)):
        diff = abs(latency_data[i] - latency_data[i-1])
        entropy_score += diff % 3
    
    # Actual key computation
    flag_sum = sum(f for f in flags)
    combined_key = 0
    for i, v in enumerate(voltage_data):
        if i % 2 == 0:
            combined_key ^= int(v * 10)  # Use every other voltage reading
    
    # Final integration
    result_component = (combined_key + flag_sum) & 0xFFFF
    final_diagnostic = (result_component * 7) % 98765
    
    # This print is required to expose the answer
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    node_ids = list(range(17, 32))
    raw_telemetry = collect_telemetry(node_ids)
    
    # Generate fake log structure
    log_entries = []
    for i in range(len(raw_telemetry['voltage'])):
        entry = {
            'timestamp': 1623456000 + i * 60,
            'sensor_v': raw_telemetry['voltage'][i],
            'response_time': raw_telemetry['latency'][i],
            'node': f'N{node_ids[i]}'
        }
        log_entries.append(entry)
    
    # System flags with meaningful values
    system_flags = [5, 8, 12, 14, 9]
    
    # Unused but plausible operations (distractors)
    stability_results = analyze_stability(raw_telemetry)
    health_index = compute_health_index(*stability_results, len(node_ids))
    critical_set = filter_critical_nodes(raw_telemetry, threshold=95)
    patterns = extract_patterns(system_flags)
    
    # Decoy diagnostic generation
    unused_diagnostics = generate_diagnostics(system_flags)
    
    # ACTUAL TARGET EXECUTION POINT
    final_diagnostic = process_metrics(log_entries, system_flags)