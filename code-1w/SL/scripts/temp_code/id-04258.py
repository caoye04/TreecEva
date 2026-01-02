import itertools

# Simulated sensor data processing with diagnostic flags
def collect_sensor_data():
    raw_samples = [0.8, 1.2, -0.5, 3.1, 2.7, -1.3, 0.9, 1.1]
    baseline_offset = 0.25
    adjusted = [x - baseline_offset for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function - dead code path (distractor)
def deprecated_filter(x):
    return x > 1.0 and x < 2.0

# Signal conditioning with multiple red herrings
def clean_signal(data):
    filtered = []
    noise_floor = 0.1
    spike_threshold = 2.5
    temp_result = 0

    for val in data:
        if abs(val) < noise_floor:
            continue  # Remove low-amplitude noise
        if abs(val) > spike_threshold:
            val = spike_threshold * (val / abs(val))  # Clamp spikes
        filtered.append(round(val, 2))
    
    # Distractor computation - looks important but unused
    outlier_count = sum(1 for x in data if abs(x) > 3.0)
    temp_result += outlier_count * 100

    return filtered

# Frame segmentation with itertools - actual usage
def segment_into_frames(signal):
    frame_size = 3
    frames = []
    for i in range(0, len(signal), frame_size):
        frame = signal[i:i + frame_size]
        if len(frame) == frame_size:
            frames.append(frame)
    
    # Misleading transformation - not used later
    padded_frames = [list(itertools.chain(f, [0] * (frame_size - len(f)))) for f in signal[::2]]
    
    return frames

# Processing step that appears critical but contains decoy logic
def compute_health_metrics(frames):
    metrics = []
    for idx, frame in enumerate(frames):
        avg = sum(frame) / len(frame)
        variance = sum((x - avg) ** 2 for x in frame) / len(frame)
        stability_score = 1 / (1 + variance)  # Higher is more stable
        
        # Decoy assignment - looks like it's tracking something important
        if idx % 2 == 0:
            dummy_flag = 1 << idx
        else:
            dummy_flag = -(1 << (idx + 1))
        
        metrics.append({'index': idx, 'stability': stability_score, 'average': avg})
    
    # Another red herring: complex calculation with no downstream effect
    total_entropy = 0.0
    for m in metrics:
        if m['stability'] > 0.5:
            total_entropy += m['stability'] * 0.7
        else:
            total_entropy -= m['stability'] * 0.3
    
    return metrics

# Core analysis function - only this matters for final result
def analyze_signal(metrics):
    cumulative_weight = 0.0
    weight_factor = 1.5
    
    for m in metrics:
        # Only even-indexed frames contribute to final result
        if m['index'] % 2 == 0:
            cumulative_weight += m['average'] * weight_factor
        else:
            # This branch modifies a local variable but has no real impact
            temp_adjust = m['stability'] * 0.1
            cumulative_weight += temp_adjust
    
    # Final transformation applied unconditionally
    final_diagnostic = int((cumulative_weight + 0.5) * 100)
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect and adjust raw data
    raw_data = collect_sensor_data()
    
    # Step 2: Clean signal (remove noise and clamp extremes)
    cleaned_signal = clean_signal(raw_data)
    
    # Step 3: Segment into fixed-size frames
    processed_frames = segment_into_frames(cleaned_signal)
    
    # Step 4: Extract health metrics (contains distractions)
    health_metrics = compute_health_metrics(processed_frames)
    
    # Step 5: Analyze signal - key statement
    final_diagnostic = analyze_signal(processed_frames)
    
    print(f"Result: {final_diagnostic}")