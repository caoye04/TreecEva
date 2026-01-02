from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental monitoring
def analyze_readings(raw_readings):
    processed = []
    temp_accum = 0
    spike_count = 0

    for idx, val in enumerate(raw_readings):
        if val > 75:
            spike_count += 1
        temp_accum += val * 0.85
        processed.append(temp_accum / (idx + 1) if idx >= 0 else val)

    return processed


def filter_anomalies(data_stream):
    # Irrelevant filtering function (dead code path)
    cleaned = [x for x in data_stream if 10 < x < 90]
    frequency_map = Counter(cleaned)
    return [k for k, v in frequency_map.items() if v > 1]


def calculate_entropy(sequence):
    # Unused mathematical distraction
    probs = [sequence.count(val) / len(sequence) for val in set(sequence)]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def shift_buffer(buffer, offset):
    # Bit manipulation red herring
    shifted = []
    for b in buffer:
        bit_modified = (b << 2) ^ offset
        bit_modified = bit_modified & 0xFF
        shifted.append(bit_modified)
    return shifted


def accumulate_trends(values):
    trend_line = []
    cumulative = 0
    for i, v in enumerate(values):
        cumulative += v + (i % 3)
        trend_line.append(cumulative)
    return trend_line


def compute_diagnostic(log_entries):
    readings = [entry['value'] for entry in log_entries]
    
    # Core processing chain
    stage1 = analyze_readings(readings)
    stage2 = accumulate_trends(stage1)
    
    # Distractor: complex but unused transformations
    decoy_map = defaultdict(int)
    for r in readings:
        decoy_map[r % 7] += 1
    
    shifted_decoy = shift_buffer(list(decoy_map.values()), 5)
    entropy_fake = calculate_entropy(shifted_decoy)
    
    # Critical computation path
    diagnostic_score = 0
    for i, val in enumerate(stage2):
        if i % 4 == 0 and val > 50:
            diagnostic_score += int(val // (i + 1))
        elif i % 3 == 2:
            diagnostic_score -= int(math.sqrt(val))

    # Final adjustment using zip and enumerate (required features)
    aux_weights = [1.1, 2.3, 1.4, 3.1, 2.2]
    adjustments = 0
    for j, (a, w) in enumerate(zip(stage2[::5], aux_weights)):
        adjustments += a * w * 0.1

    final_diagnostic = int(diagnostic_score + adjustments)
    
    # Unused variables - misleading intermediates
    summary_stats = {
        'max_raw': max(readings),
        'spike_ratio': sum(1 for x in readings if x > 70) / len(readings),
        'buffer_len': len(shifted_decoy)
    }
    
    return final_diagnostic

# Main execution sequence
if __name__ == '__main__':
    # Input data - deterministic sensor log
    reading_log = [
        {'id': 'S1', 'value': 68, 'ts': 1001},
        {'id': 'S2', 'value': 73, 'ts': 1002},
        {'id': 'S3', 'value': 77, 'ts': 1003},
        {'id': 'S4', 'value': 69, 'ts': 1004},
        {'id': 'S5', 'value': 81, 'ts': 1005},
        {'id': 'S6', 'value': 74, 'ts': 1006},
        {'id': 'S7', 'value': 66, 'ts': 1007},
        {'id': 'S8', 'value': 83, 'ts': 1008},
        {'id': 'S9', 'value': 70, 'ts': 1009},
        {'id': 'S10', 'value': 75, 'ts': 1010}
    ]

    # Trigger key computation
    final_diagnostic = compute_diagnostic(reading_log)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")