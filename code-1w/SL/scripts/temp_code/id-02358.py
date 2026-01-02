import itertools

def analyze_response_time(times):
    avg = sum(times) / len(times)
    variance = sum((t - avg) ** 2 for t in times) / len(times)
    return avg, variance

def encode_signal(x):
    # Irrelevant bit manipulation red herring
    return ((x << 3) & 0xFF) ^ 0b10101010

def validate_checksum(data):
    # Unused function - dead code path
    chk = 0
    for b in data:
        chk ^= b
    return chk == 0

def transform_sequence(seq):
    # Distractor: complex-looking but unused transformation
    paired = list(itertools.pairwise(seq))
    rotated = [((a + b) * 2) % 256 for a, b in paired]
    return [encode_signal(x) for x in rotated]

def flag_anomalies(metrics, threshold=0.75):
    anomalies = []
    for i, (t, m) in enumerate(metrics.items()):
        if m['response'] > threshold and not m['redundant']:
            anomalies.append(i * m['weight'])
    # Misleading intermediate result
    temp_result = sum(anomalies) * 0.95
    return temp_result

def aggregate_metrics(log, flags):
    base_score = 0
    adjustment = 0.0

    for entry in log:
        key = entry['id']
        if key in flags['active'] and entry['valid']:
            raw = entry['timing']
            # Real computation begins
            if raw < 0.1:
                base_score += 3
            elif raw < 0.25:
                base_score += 2
            else:
                base_score += 1

            # Nested logic with actual impact
            if entry['mode'] == 'async' and flags['config']['delay_compensate']:
                adjustment += 0.4
            elif entry['mode'] == 'sync':
                adjustment -= 0.1

    # Actual answer contribution
    adjustment *= base_score
    final_value = base_score + adjustment

    # Decoy operation that looks important
    final_value = round(final_value + flags['config']['bias_offset'], 3)

    return int(final_value)

# Main execution flow
if __name__ == '__main__':
    # Simulated system telemetry data
    timing_log = [
        {'id': 'A1', 'timing': 0.08, 'mode': 'async', 'valid': True},
        {'id': 'B2', 'timing': 0.22, 'mode': 'async', 'valid': True},
        {'id': 'C3', 'timing': 0.35, 'mode': 'sync', 'valid': True},
        {'id': 'D4', 'timing': 0.12, 'mode': 'async', 'valid': False},
        {'id': 'E5', 'timing': 0.19, 'mode': 'async', 'valid': True},
        {'id': 'F6', 'timing': 0.27, 'mode': 'sync', 'valid': True}
    ]

    # System configuration with meaningful and irrelevant fields
    system_flags = {
        'active': ['A1', 'B2', 'C3', 'E5', 'F6'],
        'standby': ['X7', 'Y8'],
        'config': {
            'delay_compensate': True,
            'bias_offset': 0.05,
            'gain_factor': 1.2,
            'debug_trace': False
        }
    }

    # Irrelevant preprocessing - distractor
    extracted_times = [entry['timing'] for entry in timing_log if entry['valid']]
    avg_response, var_response = analyze_response_time(extracted_times)
    signal_codes = [encode_signal(int(t * 100)) for t in extracted_times]

    # Unused data structure - red herring
    timing_pairs = list(itertools.combinations(extracted_times, 2))
    close_pairs = [p for p in timing_pairs if abs(p[0] - p[1]) < 0.1]

    # Another decoy metric
    stability_index = len(close_pairs) / (len(extracted_times) or 1)

    # Core diagnostic dictionary - partially used
    diagnostics = {}
    for i, t in enumerate(extracted_times):
        diagnostics[f'entry_{i}'] = {
            'response': t,
            'weight': 1.0 + (t * 2),
            'redundant': False
        }
    
    # Trigger anomaly detection - looks important but not used in final result
    _ = flag_anomalies(diagnostics, threshold=0.2)

    # Key statement: this determines the final answer
    final_diagnostic = aggregate_metrics(timing_log, system_flags)

    # Print final result as required
    print(f"Target result: {final_diagnostic}")