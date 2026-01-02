from collections import defaultdict, Counter
import math

def analyze_pattern(sequence):
    freq_map = defaultdict(int)
    for item in sequence:
        freq_map[item] += 1
    return dict(freq_map)

def compute_entropy(values):
    total = sum(values)
    entropy = 0.0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * math.log2(prob)
    return round(entropy, 6)

def generate_shift_sequence(n):
    # Irrelevant helper - dead path
    result = []
    for i in range(n):
        result.append((i << 2) ^ 7)
    return result

def evaluate_threshold(data, limit=5):
    # Unused function - red herring
    count = 0
    for x in data:
        if x > limit:
            count += 1
    return count

def track_transitions(arr):
    # Distractor: counts state changes but not used in final result
    changes = 0
    state = arr[0] > 0
    for val in arr[1:]:
        new_state = val > 0
        if new_state != state:
            changes += 1
        state = new_state
    return changes

def extract_peaks(signal):
    # Decoy function - looks important but unused
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def main_processing_chain(input_data):
    # Step 1: Filter valid entries
    filtered = [x for x in input_data if x % 2 == 1 and x > 0]
    
    # Step 2: Transform using bitwise and arithmetic
    transformed = []
    shift_key = 3
    for num in filtered:
        shifted = (num >> 1) ^ shift_key
        transformed.append(shifted)
    
    # Step 3: Count frequencies (relevant)
    freq_analysis = analyze_pattern(transformed)
    frequency_values = list(freq_analysis.values())
    
    # Step 4: Compute entropy (used later)
    entropy_value = compute_entropy(frequency_values)
    
    # Step 5: Create log with metadata (distraction)
    entropy_log = []
    temp_sum = 0
    for idx, (k, v) in enumerate(sorted(freq_analysis.items()), start=1):
        # Mix in irrelevant computation
        fake_entropy = math.sin(idx * 0.5) ** 2
        normalized = v / sum(frequency_values)
        entropy_log.append({
            'index': idx,
            'key': k,
            'count': v,
            'norm': round(normalized, 4),
            'aux': fake_entropy  # Red herring field
        })
        temp_sum += v * idx  # Dead-end accumulator
    
    # Step 6: Simulate diagnostic chain
    def compute_diagnostic(log_entries):
        raw_counts = []
        index_sum = 0
        for entry in log_entries:
            raw_counts.append(entry['count'])
            index_sum += entry['index']
        
        # Real computation path
        base_score = compute_entropy(raw_counts)
        adjustment = 0
        for i, entry in enumerate(log_entries):
            if entry['key'] % 2 == 0:  # Only odd keys were possible due to transform
                adjustment += entry['norm']
        # Adjustment remains 0 - misleading?
        
        # Critical step: use zip and enumerate together
        cumulative = 0
        for i, (a, b) in enumerate(zip(raw_counts, raw_counts[1:])):
            cumulative += (a * b) % (i + 2)  # Avoid division by zero
        
        # Final formula: combines entropy, index_sum, and cumulative
        result = int((base_score * 1000) + index_sum + (cumulative % 100))
        return result
    
    # Misleading side analysis
    dummy_seq = generate_shift_sequence(8)
    peak_vals = extract_peaks(dummy_seq)
    transitions = track_transitions(input_data)
    
    # Actual target computation
    final_diagnostic = compute_diagnostic(entropy_log)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Unused global variables - distractors
GLOBAL_OFFSET = 17
CALIBRATION_FACTOR = 0.987
MAX_ITERATIONS = 500

# Input with mixed properties
initial_stream = [12, 7, -3, 9, 14, 7, 8, 5, 9, 11, 6, 7, 9, 13, -1, 4]

# Execute
main_processing_chain(initial_stream)
