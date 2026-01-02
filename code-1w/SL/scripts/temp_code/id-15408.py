from collections import defaultdict, Counter
import math

# Simulated sensor calibration and diagnostic system
def generate_calibration_data():
    raw_samples = [i * 17 % 199 for i in range(150)]
    filtered = [x for x in raw_samples if x % 7 != 0]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    return normalized

# Irrelevant helper - distractor
def analyze_pattern(seq):
    freq = {}
    for i in range(len(seq)-1):
        pair = (seq[i], seq[i+1])
        freq[pair] = freq.get(pair, 0) + 1
    return freq

# Decoy function - never used
def legacy_compatibility(data):
    transformed = []
    for d in data:
        transformed.append((d ** 2 + 3*d + 1) % 97)
    return transformed

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def validate_sequence(seq):
    checksum = 0
    for i, val in enumerate(seq):
        if i % 3 == 0:
            checksum += val * 2
        elif i % 5 == 0:
            checksum -= val
    return checksum % 89

# Core processing with distractions
def process_metrics(signal, log_map):
    # Misleading initialization
    temp_buffer = defaultdict(int)
    for i in range(10):
        temp_buffer[f'buf_{i}'] = (i * 55) % 43
    
    # Real computation begins
    magnitude = sum(x for x in signal if x > 10 and x < 85)
    peak = max(signal)
    base_score = magnitude / (peak + 1e-8)
    
    # Distractor: unused transformation
    shifted_signal = [math.sin(math.radians(x)) for x in signal]
    avg_phase = sum(shifted_signal) / len(shifted_signal)
    
    # Another decoy structure
    metadata_index = {}
    for idx, val in enumerate(signal[:20]):
        metadata_index[f'ptr_{idx}'] = val * 13 % 101
    
    # Actual logic interwoven
    valid_windows = 0
    for i in range(0, len(signal) - 4, 4):
        window = signal[i:i+4]
        if all(w > 15 for w in window):
            valid_windows += 1
    
    # Critical branching logic
    if valid_windows > 10:
        adjustment = 1.75
    else:
        adjustment = 0.85
    
    intermediate = base_score * adjustment
    
    # Use of set operations - relevant
    unique_quarters = set()
    for val in signal:
        quarter = int(val // 25)
        unique_quarters.add(quarter)
    diversity_bonus = len(unique_quarters)

    # String-based distractor
    status_flag = "CALIBRATION_OK"
    if "ERROR" in status_flag:
        diversity_bonus = 0
    
    # Final computation
    final_score = intermediate + diversity_bonus * 2.5
    
    # Red herring: complex but unused dict
    detailed_analysis = {
        'metrics': {
            'window_count': valid_windows,
            'entropy': compute_entropy([int(s) for s in signal]),
            'validity': validate_sequence([int(s)%10 for s in signal])
        },
        'system': {
            'version': '2.1.7',
            'mode': 'diagnostic'
        }
    }
    
    # The actual answer variable
    final_diagnostic = int(round(final_score * 3.14159))
    return final_diagnostic

# Orchestration with irrelevant setup
def main():
    # Unused variables - red herrings
    system_uptime = 1274
    max_threshold = 98.6
    debug_trace = [0]*100
    recovery_vector = [i for i in range(50) if i % 4 == 0]
    
    # Relevant data
    calibration_sequence = generate_calibration_data()
    
    # Mock diagnostics log - partially used structure
    diagnostics_log = defaultdict(list)
    diagnostics_log['errors'].append('NONE')
    diagnostics_log['timestamp'] = 1678886400
    
    # Key execution point
    final_diagnostic = process_metrics(calibration_sequence, diagnostics_log)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == '__main__':
    main()