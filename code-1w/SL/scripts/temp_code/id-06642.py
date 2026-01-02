import math

# Simulated sensor data processing with red herrings and distractions
def analyze_signal_strength(raw_readings):
    if not raw_readings:
        return 0
    filtered = [x for x in raw_readings if x > 0]
    avg = sum(filtered) / len(filtered) if filtered else 0
    # Distractor: irrelevant transformation
    transformed = [math.log(abs(x) + 1) * 0.5 for x in raw_readings]
    return avg

def decode_frequency_pattern(sequence):
    # Unused function - dead code path (distractor)
    return sum([sequence[i] * (i + 1) for i in range(len(sequence))])

def validate_checksum(data):
    # Another misleading computation that looks important but isn't used in final logic
    checksum = 0
    for d in data:
        checksum ^= int(d * 100) % 255
    return checksum == 42

def extract_features(signal_slice):
    # Real but indirectly relevant processing
    magnitude = sum(abs(x) for x in signal_slice)
    peak = max(signal_slice, default=0)
    normalized = magnitude / (peak + 1e-8)
    # Decoy calculation
    entropy = -sum((x/magnitude) * math.log(x/magnitude + 1e-8) for x in signal_slice if x > 0)
    return normalized, entropy  # Only first return value is actually used later

def compute_dynamic_weight(length, mode='standard'):
    weights = {'standard': 0.8, 'boosted': 1.2, 'reduced': 0.5}
    base = weights.get(mode, 0.8)
    # Complex-looking weight adjustment (partially irrelevant)
    adjustment = math.sin(math.pi * length / 10) ** 2
    return base + adjustment * 0.2

def process_segments(data, config):
    # Core logic begins here — heavily masked by prior noise
    segment_size = config['chunk_size']
    threshold = config['activation_threshold']
    total_segments = len(data) // segment_size
    
    # Actual relevant variables
    active_count = 0
    accumulated_score = 0.0
    
    # Irrelevant tracking variables (distractors)
    anomaly_flags = []
    temporal_drift = 0.0
    
    for i in range(total_segments):
        start = i * segment_size
        end = start + segment_size
        segment = data[start:end]
        
        # Real processing step
        avg_val = sum(segment) / len(segment)
        if avg_val > threshold:
            active_count += 1
            # Use slicing to extract center portion
            mid_start = len(segment) // 4
            mid_end = 3 * len(segment) // 4
            core_segment = segment[mid_start:mid_end]
            core_avg = sum(core_segment) / len(core_segment)
            
            # Secondary condition using string-based flag (conditional expression)
            mode = 'boosted' if config['flags'][i % len(config['flags'])] == 'HIGH' else 'standard'
            weight = compute_dynamic_weight(len(core_segment), mode)
            
            # Accumulate only this score
            accumulated_score += core_avg * weight
        
        # Distractor: update unrelated metrics
        drift_step = abs(segment[-1] - segment[0])
        temporal_drift += drift_step * 0.1
        anomaly_flags.append(drift_step > 50)
    
    # Final output depends only on these two
    stability_factor = 1.0 if active_count > 0 else 0.0
    final_output = math.floor(accumulated_score * stability_factor)
    
    # Red herring print (not part of logic)
    debug_info = {
        'drift_total': temporal_drift,
        'anomalies': sum(anomaly_flags),
        'active_ratio': active_count / total_segments if total_segments else 0
    }
    
    return final_output

# Main execution
if __name__ == '__main__':
    # Simulated input data
    raw_sensor_stream = [
        12.1, 15.3, 8.7, 23.4, 19.2, 11.0, 5.5, 30.1,
        25.6, 18.9, 14.3, 20.0, 22.5, 17.8, 13.2, 24.7,
        21.3, 16.9, 10.4, 27.8, 26.1, 19.7, 15.2, 23.0
    ]
    
    # Distractor: unused derived array
    frequency_spectrum = [math.cos(x / 5) * 10 for x in range(len(raw_sensor_stream))]
    
    # Configuration with mixed relevance
    system_config = {
        'chunk_size': 6,
        'activation_threshold': 14.0,
        'flags': ['NORMAL', 'HIGH', 'NORMAL', 'HIGH']
    }
    
    # Call analysis function (irrelevant to final result)
    avg_signal = analyze_signal_strength(raw_sensor_stream)
    
    # Extract features from first slice (partial use, mostly distraction)
    first_slice = raw_sensor_stream[:8]
    features, _ = extract_features(first_slice)
    
    # The real key computation
    final_output = process_segments(raw_sensor_stream, system_config)
    
    # Print required output
    print(f"Result: {final_output}")
