import itertools

def analyze_signal_integrity(raw_samples, thresholds):
    accumulated_noise = 0
    signal_quality = 0
    transient_spikes = []
    
    for i, sample in enumerate(raw_samples):
        if i % 7 == 0:
            accumulated_noise += (sample * 0.03) ** 2
        if sample > thresholds['critical'] and i < 50:
            transient_spikes.append(sample * 0.9)
        elif sample < thresholds['baseline']:
            signal_quality -= 1
        else:
            signal_quality += 2
    
    efficiency_ratio = len(transient_spikes) / (accumulated_noise + 1)
    return {'quality': signal_quality, 'ratio': efficiency_ratio, 'spikes': len(transient_spikes)}


def compute_harmonic_envelope(frequencies, phase_shifts):
    total_envelope = 0
    harmonic_peaks = []
    
    for f, p in zip(frequencies, phase_shifts):
        adjusted = (f ** 0.5) * (p + 1)
        if adjusted > 25:
            harmonic_peaks.append(adjusted)
        total_envelope += adjusted
    
    average_peak = sum(harmonic_peaks) / len(harmonic_peaks) if harmonic_peaks else 0
    return total_envelope * (1 + average_peak * 0.01)


def generate_synthetic_load(profiles):
    dummy_result = 0
    for p in profiles:
        for k, v in p.items():
            if 'temp' in k:
                dummy_result += v * 0.1
    return dummy_result  # Irrelevant to final result


def validate_calibration_sequence(seq):
    valid_count = 0
    for s in seq:
        if s % 3 == 0 and s % 5 != 0:
            valid_count += 1
    return valid_count == 4  # Dead-end logic


def aggregate_metrics(chains, diagnostics):
    base_score = 0
    adjustment_factor = 0.0
    
    for chain in chains:
        for step in chain['steps']:
            if step['type'] == 'filter':
                base_score += step['gain']
            elif step['type'] == 'amplify' and step['active']:
                base_score += step['level'] * 2
    
    diagnostic_sum = sum(diagnostics.values())
    
    if diagnostic_sum > 100:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.85
    
    # Red herring variables
    temp_buffer = [base_score * 1.1, diagnostic_sum * 0.7, adjustment_factor * 50]
    scaling_proxy = temp_buffer[0] + temp_buffer[2]
    
    # Actual answer computation
    final_value = int((base_score * adjustment_factor) + diagnostic_sum)
    
    # Unused complex transformation
    decoy_map = {i: (v ** 2) % 37 for i, v in enumerate(temp_buffer)}
    
    return final_value

# Main execution with extensive distractors
raw_data = [i * 1.5 + (i % 4) * 0.7 for i in range(100)]
signal_thresholds = {'critical': 85.0, 'baseline': 20.0, 'warning': 60.0}

# Irrelevant data structures
system_log = [{'event': 'init', 'ts': t, 'val': t*2} for t in range(10)]
resource_pool = list(itertools.permutations([1, 2, 3], 3))  # Unused

analysis_results = analyze_signal_integrity(raw_data, signal_thresholds)
freq_bands = [12 + i*8 for i in range(15)]
phase_offsets = [i % 6 for i in range(15)]
envelope_score = compute_harmonic_envelope(freq_bands, phase_offsets)

# More distractions
workload_profiles = [
    {'cpu_temp': 65, 'gpu_temp': 70, 'fan_speed': 2000},
    {'cpu_temp': 75, 'gpu_temp': 80, 'fan_speed': 2500}
]
synthetic_load = generate_synthetic_load(workload_profiles)

# Fake validation
calibration_steps = [3, 6, 9, 12, 18, 21]
is_valid_sequence = validate_calibration_sequence(calibration_steps)

# Core processing chain (relevant)
processing_chain = [
    {
        'id': 'chain_1',
        'steps': [
            {'type': 'filter', 'gain': 8, 'weight': 0.5},
            {'type': 'amplify', 'level': 12, 'active': True, 'mode': 'boost'},
            {'type': 'filter', 'gain': 5, 'weight': 0.3}
        ]
    },
    {
        'id': 'chain_2',
        'steps': [
            {'type': 'amplify', 'level': 7, 'active': True, 'mode': 'normal'},
            {'type': 'filter', 'gain': 3, 'weight': 0.1}
        ]
    }
]

# Diagnostic values (partially derived, partially hardcoded)
diagnostics = {
    'integrity': analysis_results['quality'],
    'envelope': int(envelope_score),
    'spike_count': analysis_results['spikes'],
    'noise_floor': int(analysis_results['ratio'] * 10),
    'dummy_metric': 42  # Meant to distract
}

diagnostics['composite'] = (diagnostics['integrity'] + diagnostics['envelope']) // 2

# Key assignment - this is where the answer is determined
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

print(f"Target result: {final_diagnostic}")