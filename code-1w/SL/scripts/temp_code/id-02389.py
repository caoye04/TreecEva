from collections import defaultdict, Counter

# Simulated quantum sensor array data processing with diagnostic routines
def generate_quantum_signature(base_freq, harmonics):
    signature = []
    for i in range(harmonics):
        val = (base_freq ** i) % (i + 1 + base_freq)
        if i % 3 == 0:
            val = val ^ (i * 2)
        signature.append(val)
    return signature

def evaluate_coherence(sequence):
    coherence_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            coherence_score += 1
        else:
            coherence_score -= 1
    return abs(coherence_score)

def filter_anomalies(log_entries):
    # Irrelevant filtering routine (dead-end path)
    filtered = []
    for entry in log_entries:
        if 'ERR' not in entry and 'CRIT' not in entry:
            filtered.append(entry)
    return filtered

def compute_entropy(data):
    # Unused entropy calculation (distractor)
    freqs = {}
    for d in data:
        freqs[d] = freqs.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p).bit_length()  # Simplified pseudo-entropy
    return round(entropy, 4)

def extract_timings(event_log):
    # Distractor function - appears relevant but unused
    timings = []
    for event in event_log:
        if 'T=' in event:
            try:
                t_val = int(event.split('T=')[1].split()[0])
                timings.append(t_val)
            except:
                continue
    return timings

def analyze_phase_shifts(signal):
    # Another red herring function
    shifts = []
    for i in range(1, len(signal)):
        shift = signal[i] - signal[i-1]
        if shift != 0:
            shifts.append(shift % 7)
    return shifts

def rolling_window_op(data, window_size=3):
    results = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        op_result = (window[0] + window[2]) * window[1]
        results.append(op_result)
    return results

def build_correlation_map(seq_a, seq_b):
    # Complex-looking but irrelevant mapping
    corr_map = defaultdict(int)
    for a, b in zip(seq_a, seq_b):
        key = (a % 5, b % 4)
        corr_map[key] += 1
    return dict(corr_map)

def detect_resonance_patterns(signature):
    # Real usage: used in final analysis
    patterns = 0
    for i in range(2, len(signature)):
        if (signature[i] + signature[i-2]) % 5 == 0 and signature[i-1] % 2 == 1:
            patterns += 1
    return patterns

def calculate_stability_index(freq_seq):
    # Contributes to final answer
    total_variation = 0
    for i in range(1, len(freq_seq)):
        diff = abs(freq_seq[i] - freq_seq[i-1])
        total_variation += diff
    avg_diff = total_variation / len(freq_seq) if freq_seq else 0
    return int(avg_diff * 10)

def validate_frame_sync(signal):
    # Dead code path (never called)
    sync_points = 0
    for s in signal:
        if bin(s).count('1') % 2 == 0:
            sync_points += 1
    return sync_points

def analyze_system_state(q_sequence, logs):
    # Core logic begins
    stage_weights = defaultdict(lambda: 0.5)
    stage_weights['initial'] = 0.8
    stage_weights['final'] = 1.2

    # Real computation branch
    stability = calculate_stability_index(q_sequence)
    resonance = detect_resonance_patterns(q_sequence)

    # Intermediate decoy variables
    temp_analysis = [x * 1.5 for x in q_sequence if x % 4 == 0]
    anomaly_flag = any(x > 100 for x in temp_analysis)
    compression_ratio = len(q_sequence) / (sum(q_sequence) / max(q_sequence)) if q_sequence else 0

    # Meaningful transformation
    processed = list(map(lambda x: (x ^ 3) + 1, q_sequence))
    enhanced_coherence = evaluate_coherence(processed)

    # Real contribution chain
    base_score = stability + resonance * 2
    adjustment_factor = 0
    for idx, val in enumerate(q_sequence):
        if idx % 4 == 0 and val % 3 == 2:
            adjustment_factor += 1

    # Final computation
    final_score = base_score - adjustment_factor + enhanced_coherence

    # Diagnostic wrapper
    diagnostics = {
        'raw_length': len(q_sequence),
        'stability_metric': stability,
        'resonance_count': resonance,
        'coherence_level': enhanced_coherence,
        'adjustment_applied': adjustment_factor,
        'final_diagnostic': final_score
    }

    return diagnostics['final_diagnostic']

# --- Main execution ---
if __name__ == '__main__':
    # Generate core data
    quantum_sequence = generate_quantum_signature(base_freq=7, harmonics=12)
    
    # Simulated system logs (used for appearance)
    system_log = [
        'OK: T=120', 'INFO: T=125', 'WARN: T=130', 'ERR: T=135',
        'OK: T=140', 'INFO: T=145', 'CRIT: T=150', 'OK: T=155'
    ]
    
    # Call auxiliary functions that produce unused results (distractors)
    filtered_log = filter_anomalies(system_log)
    timing_data = extract_timings(system_log)
    phase_shifts = analyze_phase_shifts(quantum_sequence)
    rolling_results = rolling_window_op(quantum_sequence)
    correlation_grid = build_correlation_map(quantum_sequence[:6], quantum_sequence[6:])
    computed_entropy = compute_entropy(quantum_sequence)
    
    # Key execution point
    final_diagnostic = analyze_system_state(quantum_sequence, system_log)
    
    # Output result
    print(f"Result: {final_diagnostic}")