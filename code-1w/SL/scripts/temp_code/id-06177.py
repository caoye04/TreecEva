import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [i * 0.5 for i in range(40) if i % 3 != 0]
    offset = 12.8
    adjusted = [x + offset for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function - dead code path
def deprecated_filter(data):
    result = []
    for x in data:
        if x > 100:  # Never true
            result.append(x * 0.1)
    return result

# Data windowing with overlapping logic
def create_overlapping_frames(signal):
    frames = []
    for i in range(0, len(signal) - 5, 2):
        frame = signal[i:i+7]
        frames.append(frame)
    return frames

# Signal transformation using multiple paradigms
def transform_frame(f):
    squared = [x**2 for x in f]
    magnitude = sum(squared) ** 0.5
    normalized = [x / magnitude for x in f if magnitude > 0]
    return normalized

# Decoy analysis function with misleading intermediate values
def compute_legacy_metric(seq):
    total = 0
    for idx, val in enumerate(seq):
        if idx % 5 == 0:
            total += math.sin(val) * 0.1
    return total * 1000  # Large number distraction

# Core processing pipeline
def process_frames(frames):
    processed = []
    temp_cache = {}
    for i, f in enumerate(frames):
        key = f'trans_{i % 3}'
        transformed = transform_frame(f)
        if key not in temp_cache:
            temp_cache[key] = []
        temp_cache[key].append(len(transformed))
        processed.append({
            'index': i,
            'data': transformed,
            'size': len(transformed),
            'tag': f'T{i}_X'
        })
    
    # Sorting by index (redundant but realistic)
    sorted_processed = sorted(processed, key=lambda x: x['index'])
    return sorted_processed

# Diagnostic engine with red herring metrics
def evaluate_integrity(items):
    scores = []
    anomalies = 0
    for item in items:
        s = sum([abs(x) for x in item['data']])
        if s > 10:
            anomalies += 1
        scores.append(s)
    
    # Compute decoy statistic
    avg_score = sum(scores) / len(scores) if scores else 0
    peak = max(scores) if scores else 0
    
    # Real metric used later
    return len(scores) - anomalies

# String-based tagging system - distractor
def generate_tags(count):
    labels = []
    for i in range(count):
        tag = f"DIAG_{''.join([chr((i+j) % 26 + 65) for j in range(3)])}"
        labels.append(tag.upper().strip())
    return labels

# Main analyzer combining multiple concepts
def analyze_signal(readings):
    # Step 1: Frame the signal
    frames = create_overlapping_frames(readings)
    
    # Step 2: Process frames
    processed_frames = process_frames(frames)
    
    # Step 3: Evaluate structural integrity
    integrity = evaluate_integrity(processed_frames)
    
    # Step 4: Generate metadata tags (unused)
    tags = generate_tags(len(processed_frames))
    meta_info = []
    for idx, (t, f) in enumerate(zip(tags, processed_frames)):
        info_str = f"{t}:{f['tag']}@{idx}"
        meta_info.append(info_str.replace('@', '_'))
    
    # Step 5: Apply legacy metric on wrong data (misleading)
    fake_risk = 0
    for p in processed_frames:
        fake_risk += compute_legacy_metric(p['data'])
    
    # Step 6: Final diagnostic based on actual logic chain
    base = 0
    for p in processed_frames:
        if p['size'] == 7:
            base += 1
    
    final_diagnostic = base * 3 - integrity
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Collect raw sensor input
    sensor_data = collect_sensor_readings()
    
    # Create time-shifted frames
    signal_frames = create_overlapping_frames(sensor_data)
    
    # Process each frame through transformation pipeline
    processed_frames = process_frames(signal_frames)
    
    # Analyze final diagnostic state
    final_diagnostic = analyze_signal(processed_frames)
    
    # Output target result
    print(f"Result: {final_diagnostic}")