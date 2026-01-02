import itertools

# Simulated sensor data processing with embedded diagnostics
def acquire_signal(base_freq, sample_rate, duration):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    signal = [round(3 * (i % 2) + (-1)**i * 0.5, 3) for i in range(len(timesteps))]  # Square-ish wave
    return list(zip(timesteps, signal))

# Irrelevant helper - dead path
def deprecated_filter(data):
    return [x for x in data if x > 1.5]

# Unused transformation
def time_warp(sequence, factor=2):
    return [(t * factor, v) for t, v in sequence]

# Core frame processor
def extract_features(snapshot):
    times, values = zip(*snapshot)
    avg_val = sum(values) / len(values)
    peak = max(values)
    zero_crossings = sum((values[i] * values[i+1] < 0) for i in range(len(values)-1))
    return {'mean': avg_val, 'peak': peak, 'zero_cross': zero_crossings}

# Misleading diagnostic (looks important but unused)
def legacy_diagnostic(metrics):
    score = 0
    if metrics['mean'] > 1.0:
        score += 20
    if metrics['peak'] == 3.0:
        score += 45
    if metrics['zero_cross'] % 2 == 0:
        score += 35
    return score  # Never actually used

# Real-time frame validation
def validate_frame(integrity_log):
    valid_count = 0
    for entry in integrity_log:
        timestamp = entry[0]
        checksum = entry[1]
        if timestamp % 0.001 < 0.0005 and checksum % 3 == 0:
            valid_count += 1
    return valid_count > 5

# Main processing pipeline
def process_frames(raw_data, window_size=10):
    frames = []    
    for i in range(0, len(raw_data) - window_size + 1, window_size // 2):
        chunk = raw_data[i:i + window_size]
        features = extract_features(chunk)
        frames.append(features)
    
    # Distraction: complex-looking but unused structure
    dummy_map = {i: {'ref': f'F{i}', 'meta': pow(2, i % 8)} for i in range(len(frames))}
    
    # Actual relevant transformation
    processed = []
    for idx, f in enumerate(frames):
        adjusted_peak = f['peak'] - (f['mean'] * 0.1)
        processed.append({
            'id': idx,
            'magnitude': round(adjusted_peak + f['zero_cross'] * 0.05, 3),
            'valid': True
        })
        
    return processed

# Signal analyzer - key function
def analyze_signal(signals):
    cumulative_score = 0
    for s in signals:
        # Critical computation
        if s['valid']:
            cumulative_score += s['magnitude'] * 100
    
    # Red herring: elaborate but unused logic
    anomalies = []
    for s in signals:
        if s['magnitude'] < 0:
            anomalies.append(s)
    correction_factor = len(anomalies) * -5 if anomalies else 0
    
    # Final result - only this matters
    final_score = int(cumulative_score + correction_factor)
    return final_score

# Decoy analysis tree (never called)
def recursive_diagnostic(data, depth=0):
    if depth >= 3 or not data:
        return 999
    mid = len(data) // 2
    left = recursive_diagnostic(data[:mid], depth+1)
    right = recursive_diagnostic(data[mid:], depth+1)
    return (left + right) // 2

# Primary execution block
if __name__ == '__main__':
    # Generate raw sensor input
    raw_stream = acquire_signal(base_freq=50, sample_rate=1000, duration=0.1)
    
    # Compute auxiliary metadata (distractor)
    timestamps, readings = zip(*raw_stream)
    stats_summary = {
        'count': len(readings),
        'total': sum(readings),
        'variance': sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    }
    
    # Frame processing
    processed_frames = process_frames(raw_stream, window_size=8)
    
    # Validation log generation (partially relevant)
    log_entries = []
    for i, frame in enumerate(processed_frames):
        chksum = (i * 3) + (hash(str(frame)) % 7)
        log_entries.append((timestamps[i % len(timestamps)], chksum))
    
    # Validate transmission integrity (looks critical but doesn't affect answer)
    is_stable = validate_frame(log_entries)
    
    # MAIN COMPUTATION - THIS DETERMINES THE ANSWER
    final_diagnostic = analyze_signal(processed_frames)
    
    # Output target result
    print(f"Result: {final_diagnostic}")