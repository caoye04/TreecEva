from collections import defaultdict
import math

# Simulate a bioinformatics signal processing pipeline with noise filtering and pattern detection

def generate_reference_map(patterns):
    ref_map = defaultdict(int)
    for p in patterns:
        ref_map[p] = len(p) * 2
    return ref_map

def analyze_gc_content(sequence):
    # Irrelevant function: computes GC content but not used in final logic
    if not sequence:
        return 0.0
    gc_count = sum(1 for base in sequence if base in 'GC')
    return round((gc_count / len(sequence)) * 100, 2)

def detect_repeats(seq, min_length=3):
    # Dead-end analysis: finds repeating subsequences but unused
    repeats = []
    for i in range(len(seq) - min_length + 1):
        sub = seq[i:i+min_length]
        if seq.count(sub) > 1 and sub not in repeats:
            repeats.append(sub)
    return len(repeats)

def compute_entropy(data_list):
    # Distractor: calculates Shannon entropy of character frequencies (not used)
    freq = defaultdict(float)
    for item in data_list:
        freq[item] += 1
    total = len(data_list)
    entropy = 0.0
    for f in freq.values():
        prob = f / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 4)

def validate_sequence(seq):
    # Misleading validation that returns True for most cases
    valid_bases = set('ACGT')
    return all(base in valid_bases for base in seq) and len(seq) > 5

def filter_noise(sequence, threshold=10):
    # Applies arbitrary filtering rule; partially relevant but obfuscated
    filtered = ''.join(
        base for i, base in enumerate(sequence)
        if (i + 1) % 3 != 0 or ord(base) % 5 < threshold // 5
    )
    return filtered[:len(sequence)//2]  # Truncate to half

def extract_features(signal_str):
    # Extract numeric features from string using ordinal values and positions
    feature_vector = []
    for idx, char in enumerate(signal_str):
        val = (ord(char) + idx) * (idx % 4 + 1)
        if val % 7 != 0:
            feature_vector.append(val)
    return feature_vector

def integrate_signals(features, mode='advanced'):
    # Complex transformation with conditional branching
    accumulator = 0
    temp_log = []
    for i, x in enumerate(features):
        if i % 5 == 0:
            accumulator += int(math.sqrt(abs(x) + 1))
        elif i % 3 == 0:
            accumulator -= (x % 9)
        else:
            accumulator ^= (x % 16)
        temp_log.append(accumulator)  # logged but not used
    
    # Apply secondary weighting
    if len(features) > 10:
        adjustment = sum(f % 4 for f in features[:5])
        accumulator += adjustment * 2
    
    return accumulator

def process_transmission(raw_sequence, sensitivity):
    # Core logic buried among distractions
    if not raw_sequence:
        return -1
    
    # Step 1: Filter out noisy positions
    clean_seq = filter_noise(raw_sequence, threshold=sensitivity)
    
    # Step 2: Extract numerical features from remaining bases
    feat = extract_features(clean_seq)
    
    # Step 3: Integrate into single signal
    integrated = integrate_signals(feat)
    
    # Step 4: Apply final bias correction based on length parity
    correction = len(clean_seq) % 11
    if len(clean_seq) % 2 == 0:
        final_value = integrated + correction
    else:
        final_value = integrated - correction
    
    return final_value

# Irrelevant data structures (distractors)
pattern_library = ['ATG', 'CGA', 'TAA', 'GCT', 'ACC']
ref_db = generate_reference_map(pattern_library)
noise_profile = [0.1, 0.3, 0.2, 0.5, 0.7, 0.8]
baseline_entropy = compute_entropy(noise_profile)

# Input sequence (meaningful)
sequence = "AGCTAGCTAGCTAGCTAGCTAGCTAGCT"
key_threshold = 12

# Unused analyses (red herrings)
gc_content = analyze_gc_content(sequence)
repeat_count = detect_repeats(sequence, min_length=4)
is_valid = validate_sequence(sequence)

# Main execution path
filtered_sequence = filter_noise(sequence, key_threshold)  # Used indirectly
features = extract_features(filtered_sequence)
signal_strength = integrate_signals(features)

# Critical statement
final_signal = process_transmission(sequence, key_threshold)

print(f"Result: {final_signal}")