import math

# Simulated quantum sensor data and diagnostic framework
def generate_quantum_sequence(length):
    seq = []
    for i in range(length):
        val = (i ** 2 + 3 * i + 7) % 100
        if i % 5 == 0:
            val = (val * 2) ^ 15
        seq.append(val)
    return seq

def compute_entropy(vector):
    total = sum(vector)
    if total == 0:
        return 0.0
    probs = [v / total for v in vector if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 6)

def validate_readings(readings):
    # Irrelevant validation (red herring)
    return all(r >= 0 and r < 100 for r in readings)

def transform_coordinates(x, y, z):
    # Unused transformation function (dead code path)
    return ((x ^ y) + z) % 256, ((y | z) ^ x) % 256

def analyze_subsystem_tensions(seq):
    tension_map = {}
    for idx, val in enumerate(seq):
        if idx % 3 == 0:
            tension_map[idx] = (val ^ 7) + 13
        elif idx % 4 == 0:
            tension_map[idx] = (val + 17) ^ 3
    # Only some values are used later
    return tension_map

def extract_signature_peaks(data):
    peaks = []
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks[:5]  # Limit to top 5

def build_diagnostics_log(sequence):
    log = {
        'length': len(sequence),
        'max_val': max(sequence),
        'min_val': min(sequence),
        'range': max(sequence) - min(sequence),
        'median_guess': sorted(sequence)[len(sequence)//2],
        'checksum': sum(x ^ (x << 1) for x in sequence[:10]),  # Bit manipulation red herring
        'entropy': compute_entropy(sequence),
        'peaks': extract_signature_peaks(sequence),
        'baseline_shift': sum(sequence[::2]) - sum(sequence[1::2]),
        'ignored_metadata': {'version': '2.1', 'mode': 'QX'}  # Distractor field
    }
    return log

def auxiliary_correlation_test(a, b):
    # Completely irrelevant function (decoy)
    if len(a) != len(b):
        return 0
    return sum(x * y for x, y in zip(a, b)) / len(a)

def filter_anomalies(tension_map, threshold=20):
    # Filters but only one entry matters
    anomalies = {k: v for k, v in tension_map.items() if v > threshold}
    return anomalies or {0: 0}  # Default fallback

def analyze_system_state(q_seq, log_entry):
    # Core logic embedded within distractions
    
    # Distraction block 1: Unrelated signal processing
    filtered_signal = [x for x in q_seq if x % 4 != 0]
    offset_correction = sum(filtered_signal[i] - filtered_signal[i-1] 
                           for i in range(1, len(filtered_signal)) if i % 3 == 0)
    
    # Distraction block 2: Fake subsystem analysis
    dummy_pairs = [(q_seq[i], q_seq[-i-1]) for i in range(len(q_seq)//4)]
    correlation = auxiliary_correlation_test(dummy_pairs, dummy_pairs)
    
    # Relevant computation begins here
    tension_profile = analyze_subsystem_tensions(q_seq)
    significant_tensions = filter_anomalies(tension_profile, threshold=25)
    
    # Key logic step: use only the FIRST anomaly key's value
    first_key = min(significant_tensions.keys())
    base_score = significant_tensions[first_key]
    
    # Secondary influence from diagnostic log entropy
    entropy_factor = int(log_entry['entropy'] * 100)
    
    # Additional red herring: complex tuple unpacking with unused vars
    stats_summary = (
        log_entry['max_val'],
        log_entry['min_val'],
        log_entry['range'],
        len(log_entry['peaks'])
    )
    peak_count = stats_summary[3]
    _, _, _, _ = stats_summary  # Unused destructuring
    
    # Another distraction: set operations with no impact
    unique_peaks = set(log_entry['peaks'])
    peak_synergy = len(unique_peaks & {base_score % 50}) * 7
    
    # Final calculation - depends only on base_score and entropy_factor
    intermediate = (base_score * 3) + entropy_factor
    final_diagnostic = intermediate - (peak_count * 2) + peak_synergy  # peak_synergy = 0 in this case
    
    # Dead code branch - never executed due to logic above
    if 'phantom_mode' in log_entry.get('ignored_metadata', {}):
        final_diagnostic ^= 255
        
    return final_diagnostic

# Main execution flow
quantum_sequence = generate_quantum_sequence(23)
diagnostics_log = build_diagnostics_log(quantum_sequence)

# Critical statement
final_diagnostic = analyze_system_state(quantum_sequence, diagnostics_log)
print(f"Result: {final_diagnostic}")