from collections import defaultdict, Counter
import math

# Simulated bioinformatics sequence analysis with red herrings
def preprocess_sequence(raw_seq):
    base_count = defaultdict(int)
    for base in raw_seq:
        base_count[base] += 1
    
    # Irrelevant transformation (dead path)
    temp_weight = 0
    for b in 'ACGT':
        temp_weight += base_count[b] * (ord(b) % 7)
    
    normalized = {k: v / len(raw_seq) for k, v in base_count.items()}
    return normalized

def compute_entropy(profile):
    entropy = 0.0
    for prob in profile.values():
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return round(entropy, 6)

def shift_sequence(seq, offset):
    # Unused decoy function
    return seq[offset:] + seq[:offset]

def evaluate_strand_energy(seq):
    # Misleading energy calculation (not used in final result)
    energy_map = {'A': -0.7, 'C': -1.2, 'G': -1.5, 'T': -0.8}
    total = 0.0
    for i, base in enumerate(seq):
        total += energy_map.get(base, 0) * ((i+1) % 5)
    return total

def transform_signal(values):
    # Distractor: signal processing not used
    smoothed = []
    for i in range(len(values)):
        window = values[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))
    return [round(x, 3) for x in smoothed]

def analyze_pattern(data, flags):
    pattern_value = 0
    
    # Core logic embedded in noise
    if flags['enable_filter']:
        threshold = flags['threshold']
        filtered = [x for x in data if x > threshold]
        if len(filtered) > 0:
            avg = sum(filtered) / len(filtered)
            pattern_value += int(avg * 100)
    
    # Red herring branch
    if flags['use_legacy']:
        legacy_sum = 0
        for i in range(100):
            legacy_sum += (i * i) % 47
        pattern_value -= legacy_sum // 10  # Decoy subtraction
    
    # Key conditional (actually modifies outcome)
    if flags['invert_phase']:
        pattern_value = abs(pattern_value) * -1
    
    return pattern_value

# Main execution flow
if __name__ == "__main__":
    # Simulated genomic sequence
    sequence = "ACGTACGTACGTACGTACGTACGT" * 4
    
    # Real preprocessing
    freq_profile = preprocess_sequence(sequence)
    entropy = compute_entropy(freq_profile)
    
    # Generate transformed data (this IS used)
    transformed_data = []
    for i, p in enumerate(freq_profile.values()):
        val = p * 1000 + (i * entropy)
        transformed_data.append(round(val, 4))
    
    # Control flags - only some are active
    control_flags = {
        'enable_filter': True,
        'threshold': 25.0,
        'use_legacy': False,           # This disables the decoy branch
        'invert_phase': True,
        'debug_mode': True,
        'cache_enabled': False
    }
    
    # Dead code block (misleading)
    if control_flags['debug_mode']:
        debug_log = []
        for _ in range(3):
            debug_log.append("DEBUG: System check passed")
    
    # Energy calculation (never assigned to anything critical)
    strand_energy = evaluate_strand_energy(sequence)
    
    # Signal transformation on unrelated data
    dummy_signal = [1.1, 2.5, 3.7, 4.2, 5.8]
    processed_signal = transform_signal(dummy_signal)
    
    # Key assignment point
    final_score = analyze_pattern(transformed_data, control_flags)
    
    # Print required output
    print(f"Result: {final_score}")