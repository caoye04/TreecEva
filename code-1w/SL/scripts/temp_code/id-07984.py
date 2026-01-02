import math

# Simulated sensor data processing system
def collect_samples(count):
    return [math.sin(i * 0.5) + 0.5 * math.cos(i * 0.3) for i in range(count)]

# Irrelevant helper: spectrogram analysis (dead end)
def generate_spectrogram(data):
    n = len(data)
    spec = []
    for i in range(n // 2):
        val = sum(data[j] * math.exp(-2j * math.pi * i * j / n).real for j in range(n))
        spec.append(abs(val))
    return spec

# Distractor function: unused in final flow
def normalize_signal(x, min_val=-1.5, max_val=1.5):
    return (x - min_val) / (max_val - min_val)

# Real processing path begins

def filter_outliers(data, limit=2.0):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    # Return filtered data within 'limit' standard deviations
    return [x for x in data if abs(x - mean_val) <= limit * std_dev], mean_val

# Signal segmentation - relevant

def segment_signal(data, size=5):
    segments = []
    for i in range(0, len(data) - size + 1, size):
        segments.append(data[i:i+size])
    return segments

# Bit manipulation red herring

def encode_timestamp(seconds):
    s = int(seconds % 60)
    m = int((seconds // 60) % 60)
    h = int(seconds // 3600)
    # Pack into single integer using bit shifts (not used later)
    return (h << 12) | (m << 6) | s

# Decoy state tracking

class BufferState:
    def __init__(self):
        self.timestamp = encode_timestamp(12345)
        self.status_flag = 0b101010
        self.version = 2

# Core diagnostic logic

def evaluate_segment(segment):
    if len(segment) == 0:
        return 0.0
    peak = max(segment)
    trough = min(segment)
    dynamic_range = peak - trough
    avg = sum(segment) / len(segment)
    stability_score = 1 / (1 + abs(avg))  # favors values near zero
    return (dynamic_range * 0.6) + (stability_score * 0.4)

# Orchestration with distractors

def analyze_signal_quality(raw_buffer, threshold):
    # Step 1: Filter noise
    cleaned_data, base_mean = filter_outliers(raw_buffer, limit=1.8)
    
    # Step 2: Segment
    segments = segment_signal(cleaned_data, size=5)
    
    # Step 3: Evaluate each segment
    scores = [evaluate_segment(seg) for seg in segments]
    
    # Step 4: Aggregate quality metric
    avg_score = sum(scores) / len(scores) if scores else 0.0
    
    # Step 5: Apply threshold logic
    if avg_score >= threshold:
        flag_code = 0b1100
    else:
        flag_code = 0b0011
    
    # Irrelevant set operation (distractor)
    known_flags = {0b0001, 0b0010, 0b0100, 0b1000}
    compatible_flags = known_flags & {flag_code}  # Always empty
    
    # Unused recursive red herring
    def count_bits(n):
        if n == 0:
            return 0
        return 1 + count_bits(n & (n-1))
    
    # Final diagnostic value (this is the answer)
    final_value = round(avg_score * 10000)  # Scale for precision
    
    # Dead code path
    if False:
        fallback = generate_spectrogram(cleaned_data)
        final_value -= sum(fallback[:3])
    
    return final_value

# Simulate system boot
sensor_buffer = collect_samples(50)

# Initialize unused state
state_tracker = BufferState()

# Main execution
processed_buffer, _ = filter_outliers(sensor_buffer, limit=1.8)
segmented = segment_signal(processed_buffer, size=5)

# Key statement
final_diagnostic = analyze_signal_quality(diagnostic_buffer := processed_buffer, threshold=0.75)

print(f"Target result: {final_diagnostic}")