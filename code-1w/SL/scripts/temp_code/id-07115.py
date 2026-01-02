from collections import defaultdict, Counter
import math

# Simulated sensor data acquisition (distractor: some values are irrelevant)
sensor_readings = [144, 178, 201, 144, 256, 321, 178, 400, 201, 256, 512]

# Irrelevant preprocessing path (dead code)
def legacy_normalize(data):
    return [x / max(data) for x in data]

# Unused transformation function (decoy)
calculate_entropy = lambda lst: sum(-p * math.log2(p) for p in Counter(lst).values() if p > 0)

# Core processing pipeline
def filter_outliers(data, threshold=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Misleading intermediate analysis (red herring)
def compute_trend_score(values):
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    return sum(1 for d in diffs if d > 0) - sum(1 for d in diffs if d < 0)

# Real signal processor: extracts power signatures
def extract_signatures(raw):
    sig_map = defaultdict(int)
    for val in raw:
        root = int(math.sqrt(val))
        if root * root == val:  # Perfect squares only
            sig_map[root] += 1
    return dict(sig_map)

# Distractor: unused frequency analyzer
def analyze_frequency_pattern(seq):
    freq_pairs = [(seq[i], seq[i+1]) for i in range(len(seq)-1)]
    return Counter(freq_pairs)

# Critical processing function
def process_signal_chunk(chunk):
    chunk_filtered = filter_outliers(chunk)
    chunk_signatures = extract_signatures(chunk_filtered)
    aggregate = 0
    for k, v in chunk_signatures.items():
        if k % 2 == 1:  # Only odd roots contribute
            aggregate += k * v
    return aggregate

# Simulated multi-channel input (only channel_1 matters)
channel_1 = sensor_readings[::2]
channel_2 = [x * 0.1 for x in sensor_readings]  # Low-amplitude noise
channel_3 = [x ** 0.5 for x in reversed(sensor_readings)]

# Apply real processing to correct channel
processed_data = process_signal_chunk(channel_1)

# Secondary distractor: spatial correlation (irrelevant)
def compute_spatial_coherence(channels):
    return math.cos(len(channels)) * 100

# Real diagnostic engine
def analyze_signal(signal_value):
    if signal_value == 0:
        return -1
    
    # Complex diagnostic logic with nested conditions
    phase_a = int(math.log(abs(signal_value), 2))
    phase_b = signal_value % 7
    
    if phase_a > 10:
        adjustment = 3
    elif phase_a > 5:
        adjustment = 5
    else:
        adjustment = 8
    
    temp_result = (phase_a * 13) ^ (phase_b * 7)  # Bitwise mix
    temp_result -= adjustment
    
    # Final nonlinear transformation
    final_score = temp_result ** 2 / (phase_b + 1)
    
    # Tertiary distraction: unused feedback loop simulation
    feedback_weights = [0.1, 0.3, 0.6]
    accumulated = sum(w * final_score for w in feedback_weights)
    
    # The actual answer derivation
    return int(final_score) + 117  # Offset added deterministically

# Dead code path: never called
optimize_pipeline = lambda f: (lambda x: f(x) * 1.05)

# Key execution point
final_diagnostic = analyze_signal(processed_data)

# Output result as required
print(f"Result: {final_diagnostic}")