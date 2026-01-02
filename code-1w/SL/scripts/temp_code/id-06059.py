import math

# Simulated sensor data processing pipeline for aerospace telemetry
def acquire_signal(raw_id, duration_ms):
    raw_samples = [((i * 7) % 23) + (raw_id * 3) for i in range(duration_ms // 10)]
    offset = 127
    scaled = [math.sin(s / 10.0) * offset + offset for s in raw_samples]
    return [int(s) for s in scaled]

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(x):
    return (x >> 1) ^ 0xAA

# Signal conditioning with red herring transformations
def filter_noise(data, threshold=15):
    filtered = []
    temp_cache = []  # Unused but misleading
    for val in data:
        if abs(val - 127) > threshold:
            adjusted = val ^ 0x55  # Bit manipulation red herring
            if adjusted > 100:
                adjusted = int(math.sqrt(adjusted) * 10)
            filtered.append(adjusted)
    return filtered

# Frame segmentation with decoy logic
def segment_frames(noise_filtered, frame_size=4):
    frames = []
    for i in range(0, len(noise_filtered) - frame_size + 1, frame_size):
        frame = noise_filtered[i:i + frame_size]
        checksum = sum(frame) % 256
        # Decoy validation that looks important but isn't used
        parity_valid = bin(checksum).count('1') % 2 == 0
        frames.append({'data': frame, 'cs': checksum})
    return frames

# Data enrichment with irrelevant computations
def enrich_frame_metadata(segmented):
    enriched = []    
    base_factor = 1.618
    for idx, f in enumerate(segmented):
        entropy = 0.0
        freq_map = {}
        for d in f['data']:
            freq_map[d] = freq_map.get(d, 0) + 1
        for count in freq_map.values():
            p = count / len(f['data'])
            entropy -= p * math.log2(p) if p > 0 else 0
        # Seemingly important metric, not actually used later
        security_flag = (f['cs'] ^ idx) & 0x0F
        # Actual relevant transformation: scale entropy
        normalized_entropy = int(entropy * 100)
        enriched.append({
            'payload': f['data'],
            'score': normalized_entropy,  # This will be used later
            'meta': {'idx': idx, 'ent': entropy}
        })
    return enriched

# Core diagnostic analysis — where the real computation happens
def compute_health_index(enriched_list):
    total_severity = 0
    for item in enriched_list:
        raw_score = item['score']
        # Real logic begins: classify severity based on score
        if raw_score < 30:
            level = 1
        elif raw_score < 60:
            level = 2
        elif raw_score < 85:
            level = 3
        else:
            level = 4  # Critical
        # Accumulate weighted severity
        total_severity += level * raw_score
    return total_severity

# Higher-order analysis with list comprehension and filtering
def identify_anomalies(enriched):
    # List comprehension with complex condition (partially irrelevant)
    anomalies = [
        e for e in enriched 
        if (e['score'] > 70 and sum(e['payload']) % 17 == 0)
    ]
    return len(anomalies) * 100  # Distractor output

# Final diagnostic aggregation — key function containing answer source
def analyze_signal(clean_data):
    # Re-process to extract frames (redundant call, distractor)
    noiseless = filter_noise(clean_data, threshold=10)
    frames = segment_frames(noiseless)
    meta_frames = enrich_frame_metadata(frames)
    
    # REAL computation branch
    health_index = compute_health_index(meta_frames)
    
    # DEAD-END branches with misleading calculations
    prediction_vector = [math.tanh(h['score'] / 100.0) for h in meta_frames]
    stability_metric = sum(prediction_vector) / len(prediction_vector) if prediction_vector else 0
    risk_projection = int(stability_metric * 1000) ^ 0xFF  # Looks important
    
    # Final assembly — only health_index contributes to result
    final_value = health_index + 1337
    
    # Unused but plausible-looking diagnostic fusion
    fusion_score = (final_value * 0.7) + (risk_projection * 0.3)
    
    return final_value  # Only this matters

# Entry point with dummy setup
if __name__ == '__main__':
    # Initial signal acquisition
    raw_telemetry = acquire_signal(raw_id=7, duration_ms=120)
    
    # Begin processing chain
    processed_signal = filter_noise(raw_telemetry, threshold=15)
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_signal)
    
    # Output target result
    print(f"Result: {final_diagnostic}")