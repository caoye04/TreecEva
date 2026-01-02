import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration_ms, sample_rate):
    return [int(50 * math.sin(i * 0.1)) + 25 for i in range(0, duration_ms, 100 // sample_rate)]

def filter_outliers(raw_samples, limit=75):
    cleaned = []
    for x in raw_samples:
        if -limit < x < limit:
            cleaned.append(x)
    return cleaned

def compute_moving_avg(data, window=3):
    if len(data) < window:
        return [0]
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def extract_features(signal):
    # Irrelevant feature extraction (distractor)
    magnitude = sum(abs(x) for x in signal)
    peaks = [i for i in range(1, len(signal)-1) if signal[i] > signal[i-1] and signal[i] > signal[i+1]]
    energy = sum(x*x for x in signal) / len(signal)
    return {'mag': magnitude, 'peaks': len(peaks), 'energy': energy}

def generate_key(length):
    # Dead function - never used but looks important
    key = ''
    for i in range(length):
        key += chr(97 + (i * 7) % 26)
    return key

def encrypt_sequence(seq, codebook):
    # Unused encryption logic - red herring
    return [seq[i] ^ codebook.get(i % 5, 10) for i in range(len(seq))]

def normalize_range(values, low=-100, high=100):
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0 for _ in values]
    return [low + (x - min_val) * (high - low) / (max_val - min_val) for x in values]

def build_threshold_map(config_str):
    # Parse configuration string to create threshold levels
    parts = config_str.split('|')
    levels = {}
    for part in parts:
        if ':' in part:
            k, v = part.split(':')
            levels[k] = float(v)
    return levels

def analyze_signal(data, thresholds):
    base_score = 0
    segment_size = len(data) // 4 or 1
    segments = [data[i:i+segment_size] for i in range(0, len(data), segment_size)]
    
    # Decoy variables that look important
    temp_analysis = set()
    checksum = 0
    anomaly_count = 0
    
    for i, seg in enumerate(segments):
        avg = sum(seg) / len(seg)
        if avg > thresholds.get('warning', 40):
            base_score += 10
        elif avg < thresholds.get('critical', 10):
            base_score -= 5
        
        # Bit manipulation distractor
        packed = 0
        for val in seg[:4]:
            packed = (packed << 3) | (abs(val) & 7)
        checksum ^= packed
        
        # String slicing red herring
        tag = f"SEG{i:02d}-X"
        category = tag[4:5]
        temp_analysis.add(category)
    
    # Real logic embedded among distractions
    total_variation = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    if total_variation > thresholds.get('variation_cap', 200):
        base_score += 15
    
    # Hidden correction factor based on set size
    adjustment = len(temp_analysis) * 3  # Only indirectly related
    final_score = base_score + adjustment
    
    # This is actually unused — misleading!
    encoded_result = ''.join([hex(n)[-1] for n in data[:8]])[::-1]
    
    return final_score

# --- Main execution with multiple distraction paths ---
raw_signal = collect_samples(800, 10)
cleaned_signal = filter_outliers(raw_signal)
moving_averages = compute_moving_avg(cleaned_signal, 4)
normalized_signal = normalize_range(moving_averages, -50, 50)

# Unused transformation chains
feature_set = extract_features(normalized_signal)
key_string = generate_key(12)
code_lookup = {0: 17, 1: 23, 2: 19, 3: 29, 4: 31}
encrypted_seq = encrypt_sequence([len(normalized_signal)], code_lookup)

# Critical data structure built from string operations
config_layout = 'level:35|warning:42|critical:8|variation_cap:187|nodes:4'
threshold_config = build_threshold_map(config_layout)

# String slicing and set operations as required python features
tag_pool = {config_layout[5:10], config_layout[20:26], 'warning', 'nodes'}
flag_segments = [t.upper() for t in tag_pool if 'v' not in t]

# Actual core computation path
processed_data = [int(x) for x in normalized_signal if abs(x) > 5]

# Key execution point
final_diagnostic = analyze_signal(processed_data, threshold_config)

# Output result as required
print(f"Target result: {final_diagnostic}")