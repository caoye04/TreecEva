def analyze_sensor_node(temp_data, threshold_config):
    baseline = sum(temp_data) / len(temp_data)
    deviation = [abs(t - baseline) for t in temp_data]
    spike_count = sum(1 for d in deviation if d > threshold_config['spike'])
    
    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(temp_data)):
        window = temp_data[max(0, i-2):min(i+3, len(temp_data))]
        smoothed.append(sum(window) / len(window))
    smoothed_avg = sum(smoothed) / len(smoothed)

    # Dead code path - never used (red herring)
    def legacy_calibration(x):
        return (x * 0.87) + 3.14

    # Unused transformation chain
    calibrated_readings = [legacy_calibration(t) for t in temp_data]
    
    # Core logic disguised among distractions
    if spike_count > threshold_config['critical']:
        status_flag = 3
    elif spike_count > threshold_config['warning']:
        status_flag = 2
    else:
        status_flag = 1
    
    return {'baseline': baseline, 'spikes': spike_count, 'flag': status_flag}


def transform_dataset(raw_sequence, mode='encode'):
    # Bit manipulation decoy
    magic_key = 0b101010
    transformed = []
    for val in raw_sequence:
        masked = val ^ magic_key
        rotated = ((masked << 1) & 0b111111) | ((masked >> 5) & 0b111111)
        transformed.append(rotated)
    
    # Unused checksum (misleading)
    checksum = sum(transformed) % 256
    
    # Real but indirect contribution to final result
    entropy_estimate = sum(1 for x in transformed if x % 2 == 1) / len(transformed)
    
    return {'data': transformed, 'entropy': entropy_estimate}


def aggregate_metrics(chains, key):
    # Complex data fusion with red herrings
    fused_score = 0
    
    # Decoy normalization
    norm_factor = max(len(chain) for chain in chains) if chains else 1
    dummy_normalized = [len(c)/norm_factor for c in chains]
    
    # Irrelevant string-based identifier generation (distraction)
    import hashlib
    ids = [hashlib.md5(str(chain).encode()).hexdigest()[:8] for chain in chains]
    
    # Meaningful computation buried here
    valid_flags = []
    for entry in chains:
        if 'flag' in entry and entry['flag'] == 3:
            valid_flags.append(entry['spikes'])
    
    # Conditional expression (required feature)
    adjustment = 10 if any(f > 5 for f in valid_flags) else 5
    
    # Real metric calculation
    base_metric = sum(valid_flags) * adjustment
    
    # Fake obfuscation layer
    obfuscation_pool = [base_metric ^ i for i in range(8)]
    selected_index = key % 8
    deobfuscated = obfuscation_pool[selected_index] ^ selected_index
    
    # Final answer derivation
    final_output = int(base_metric + deobfuscated) // 2
    
    # Unused high-complexity transformation (dead path)
    def deep_analysis(x):
        if x < 100:
            return x ** 2
        else:
            return sum(int(d)**3 for d in str(x))
    
    return final_output

# Main execution flow
if __name__ == '__main__':
    # Simulated sensor inputs (real data)
    temperatures = [23.5, 24.1, 22.8, 26.9, 23.0, 24.5, 28.7, 23.2, 24.0, 25.1]
    
    # Threshold configuration (used)
    config = {
        'spike': 2.5,
        'warning': 2,
        'critical': 4
    }
    
    # Process sensor node (used)
    node_diagnostics = analyze_sensor_node(temperatures, config)
    
    # Generate fake encoded stream (distractor)
    raw_stream = [12, 45, 33, 67, 29]
    encoded_data = transform_dataset(raw_stream, mode='encode')
    
    # Build processing chain with mixed real and fake components
    processing_chain = [
        node_diagnostics,
        {'data': [1,2,3], 'source': 'simulated'},
        {'flag': 3, 'spikes': 7},
        {'flag': 3, 'spikes': 4},
        {'irrelevant': 'entry'}
    ]
    
    # Critical key derived from bit math (actually used)
    validation_key = (0b1101 ^ 0b1010) + (17 & 7)
    
    # Key assignment and target computation
    final_diagnostic = aggregate_metrics(processing_chain, validation_key)
    
    print(f"Result: {final_diagnostic}")