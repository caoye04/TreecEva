def calculate_thermal_output(state, log_entries):
    base_output = 17
    modifier = 0
    
    # Analyze reactor state sequence
    state_sequence = [s for s in state if s in 'ACGT']
    activation_peaks = ''.join(state_sequence).count('AG')
    
    # Irrelevant string processing (distractor)
    nucleotide_map = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement_strand = ''.join(nucleotide_map.get(nuc, nuc) for nuc in state_sequence)
    palindrome_check = complement_strand == complement_strand[::-1]
    
    # Efficiency analysis with list comprehension
    valid_logs = [entry for entry in log_entries if entry['status'] == 'OK']
    efficiency_values = [e['value'] for e in valid_logs]
    avg_efficiency = sum(efficiency_values) / len(efficiency_values) if efficiency_values else 1.0
    
    # Dead code path (misleading)
    if palindrome_check:
        base_output *= 0.9  # Never reached due to data
    
    # Core calculation logic
    peak_factor = activation_peaks * 3
    modifier += peak_factor
    
    # Secondary adjustment from filtered data
    recent_entries = [e for e in valid_logs if e['timestamp'] > 1625000000]
    if len(recent_entries) > 2:
        modifier += int(avg_efficiency * 4)
    
    # Unused intermediate variables (distraction)
    projected_yield = base_output * avg_efficiency * (1 + modifier / 10)
    safety_margin = 1.0 - sum(1 for e in log_entries if e['status'] != 'OK') * 0.05
    
    final_output = base_output + modifier
    return final_output

# Simulated reactor monitoring data
reactor_state = 'AGCTAGGTCAG'
efficiency_log = [
    {'timestamp': 1624980000, 'value': 8.5, 'status': 'OK'},
    {'timestamp': 1624990000, 'value': 9.2, 'status': 'OK'},
    {'timestamp': 1625000000, 'value': 7.8, 'status': 'OK'},
    {'timestamp': 1625010000, 'value': 9.6, 'status': 'OK'},
    {'timestamp': 1625020000, 'value': 0.0, 'status': 'ERROR'},  # Invalid entry
]

# Misleading pre-computations
baseline_metric = sum(len(entry['status']) for entry in efficiency_log)
diagnostic_flag = any('ERROR' in entry['status'] for entry in efficiency_log)

# Key statement
thermal_capacity = calculate_thermal_output(reactor_state, efficiency_log)

Result: {thermal_capacity}