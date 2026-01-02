from collections import defaultdict, Counter
import itertools

# Simulate sensor diagnostics with encoded signal patterns
def decode_signal_pattern(raw_data):
    decoded = 0
    for bit in raw_data:
        decoded ^= bit  # XOR accumulation (irrelevant to final result)
    return decoded + 3

def analyze_frequency(profile):
    freq_count = defaultdict(int)
    for val in profile:
        freq_count[val] += 1
    # Dead code path — never used later
    sorted_freq = sorted(freq_count.items(), key=lambda x: -x[1])
    return [k for k, v in sorted_freq]

def validate_checksum(sequence):
    # Irrelevant validation function
    total = sum(sequence)
    return total % 7 == 0

def filter_anomalies(data_stream, limit):
    # Misleading filtering logic that isn't actually used
    return [x for x in data_stream if x < limit]

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)  # Computed but unused

def extract_critical_bandwidth(signal_group):
    # Extracts every third element — distractor operation
    bandwidth = []
    for i in range(0, len(signal_group), 3):
        if i < len(signal_group):
            bandwidth.append(signal_group[i])
    return bandwidth  # Never assigned to anything important

def process_signals(log_entries, criteria):
    state_log = defaultdict(list)
    temp_result = 0
    flip_mode = False
    
    # Real computation begins here — core logic mixed with noise
    for entry in log_entries:
        tag = entry['tag']
        sequence = entry['data']
        
        # Actual relevant step 1: Count occurrences of threshold-crossing values
        high_freq = [x for x in sequence if x > criteria['high']]
        spike_count = len(high_freq)
        
        # Actual relevant step 2: Track how many entries exceed dynamic threshold
        if spike_count > criteria['spike_limit']:
            state_log[tag].append(spike_count)
            if not flip_mode:
                temp_result += spike_count * 2
            else:
                temp_result -= 1
            flip_mode = not flip_mode  # Toggle
        
        # Distractor: Bitwise manipulation with no impact
        masked_val = 0
        for num in sequence:
            masked_val |= (num & 0xF) ^ 5  # Some bitwise red herring
        
        # Distractor: Use of itertools to create permutations (no effect)
        for pair in itertools.permutations(sequence[:2], 2):
            diff = abs(pair[0] - pair[1])
            temp_result += diff % 3  # Minimal side effect, mostly noise
    
    # Actual relevant step 3: Final adjustment based on number of logged tags
    modifier = len(state_log.keys())
    final_output = temp_result + modifier * 5
    
    # Print required output
    print(f"Result: {final_output}")
    return final_output

# Input data setup
diagnostics = [
    {'tag': 'A', 'data': [12, 15, 8, 23, 19]},
    {'tag': 'B', 'data': [6, 4, 11, 9, 21]},
    {'tag': 'C', 'data': [17, 14, 25, 30, 8]},
    {'tag': 'D', 'data': [5, 3, 9, 7, 12]}
]

thresholds = {
    'high': 10,
    'spike_limit': 2
}

# Call the main processing function
final_output = process_signals(diagnostics, thresholds)