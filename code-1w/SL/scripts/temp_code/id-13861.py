import math

# Simulated health monitoring system with redacted metrics
# Focus: neurological activity analysis using mixed computational paradigms

def analyze_pulse_sequence(seq):
    if len(seq) < 3:
        return 0
    result = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            result += 1
    return result

def evaluate_rhythm_pattern(pattern):
    # Irrelevant function - rhythm analysis not used in final calculation
    total_peaks = 0
    for val in pattern:
        if val > 0.5:
            total_peaks += 1
    return total_peaks

def compute_entropy(data):
    # Unused entropy calculation - distractor
    entropy = 0.0
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    for count in freq_map.values():
        p = count / len(data)
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def extract_burst_cycles(signal):
    # Dead code path - never called
    cycles = []
    start = None
    for i, s in enumerate(signal):
        if s > 0.7 and start is None:
            start = i
        elif s < 0.3 and start is not None:
            cycles.append(i - start)
            start = None
    return cycles

def filter_artifacts(readings, level=0.1):
    # Distractor: signal filtering not impacting main logic
    cleaned = []
    for r in readings:
        if abs(r - 0.5) > level:
            cleaned.append(r)
    return cleaned

# Lambda functions for dynamic thresholding (used)
thresh_util = lambda x, t: 1 if x > t else 0
threshold_func = lambda val: thresh_util(val, 0.65)

# Neurological burst detection parameters
base_threshold = 0.65
sampling_rate = 128
artifact_suppression = True
normalization_factor = 1.87

# Simulated multi-channel neural readings (some irrelevant)
channel_a = [0.31, 0.45, 0.67, 0.89, 0.72, 0.51, 0.33]
channel_b = [0.29, 0.53, 0.48, 0.61, 0.77, 0.83, 0.69]  # Unused
channel_c = [0.15, 0.22, 0.31, 0.43, 0.55, 0.62, 0.68]  # Partially used

# Composite health data structure (only first component used)
health_data = {
    'bursts': channel_a,
    'baseline_stability': [0.81, 0.79, 0.83],  # Unused
    'latency_profile': {'t1': 12, 't2': 18},  # Dead weight
    'auxiliary': {'x': 1, 'y': 2}  # Red herring
}

# Secondary data structures for distraction
historical_trends = [
    {'epoch': 1, 'value': 0.61},
    {'epoch': 2, 'value': 0.59}
]
summary_stats = set()
for trend in historical_trends:
    summary_stats.add(round(trend['value'], 2))

# Misleading intermediate processing
temp_aggregate = 0
for sample in channel_c:
    temp_aggregate += int(sample * 100)
adjustment_offset = temp_aggregate // 10  # Looks important, unused

# Decoy state tracking
state_flags = [False] * 5
state_flags[0] = len(channel_b) > 5
state_flags[2] = sum(channel_c) > 2.5

# Core diagnostic processor - only this affects final answer
def process_metrics(data, threshold_strategy):
    raw_signal = data['bursts']
    
    # Step 1: Detect pulse peaks
    peak_count = analyze_pulse_sequence(raw_signal)
    
    # Step 2: Apply dynamic threshold
    triggered = [threshold_strategy(x) for x in raw_signal]
    
    # Step 3: Count threshold crossings
    trigger_events = sum(triggered)
    
    # Step 4: Compute stability ratio
    stable_ratio = (len(raw_signal) - abs(len(raw_signal) - trigger_events)) / len(raw_signal)
    
    # Step 5: Integer division and rounding
    base_score = int(stable_ratio * 100) // 2
    
    # Step 6: Bit manipulation for obfuscation
    encoded = base_score ^ 15  # XOR with magic number
    
    # Step 7: Conditional amplification
    if trigger_events >= 3:
        encoded *= 2
    
    # Step 8: Final adjustment using mathematical function
    final_value = encoded + int(math.sqrt(peak_count + 1))
    
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_func)

# Output requirement
print(f"Result: {final_diagnostic}")