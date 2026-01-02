import math

# Simulated sensor data processing pipeline for aerospace telemetry
def main():
    raw_readings = [3, 5, 7, 11, 13, 17, 19, 23]
    calibration_offset = 0.87
    temporal_weights = [0.1, 0.2, 0.15, 0.25, 0.05, 0.1, 0.05, 0.05]
    
    # Irrelevant statistical moment calculations (distractor)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    skewness = sum((x - mean_val) ** 3 for x in raw_readings) / (len(raw_readings) * variance ** 1.5)
    kurtosis = sum((x - mean_val) ** 4 for x in raw_readings) / (len(raw_readings) * variance ** 2) - 3
    
    # Signal amplification with frequency masking (partially relevant)
    amplified_signal = []
    for i, val in enumerate(raw_readings):
        if i % 2 == 0:
            amplified_signal.append(int(val * 1.5 + calibration_offset))
        else:
            amplified_signal.append(int(val * 0.8 - calibration_offset))
    
    # Decoy transformation using set operations (mostly irrelevant)
    unique_amps = set(amplified_signal)
    shifted_set = {x + 2 for x in unique_amps if x > 10}
    filtered_set = shifted_set.difference({x for x in shifted_set if x % 3 == 0})
    set_median = sorted(filtered_set)[len(filtered_set)//2] if filtered_set else 0
    
    # Frame packing with zip and enumerate (core path)
    frames = []
    for idx, (val, weight) in enumerate(zip(amplified_signal, temporal_weights)):
        frame_id = f"F{idx+1}"
        weighted_val = round(val * weight, 3)
        checksum = (idx + 1) * (val % 4)
        frames.append({'id': frame_id, 'data': val, 'weighted': weighted_val, 'chk': checksum})
    
    # Redundant dictionary aggregation (distractor)
    frame_summary = {}
    for f in frames:
        frame_summary[f['id']] = {
            'raw': f['data'],
            'norm': f['weighted'],
            'meta': {'index': int(f['id'][1:]), 'flag': f['chk'] > 5}
        }
    
    # Signal harmonics analysis (dead path)
    harmonic_peaks = []
    for i in range(1, len(amplified_signal)):
        if amplified_signal[i] > amplified_signal[i-1] and i % 3 == 0:
            harmonic_peaks.append(i)
    peak_magnitude = sum(amplified_signal[i] for i in harmonic_peaks) if harmonic_peaks else 0
    
    # Critical signal processing chain
    processed_frames = preprocess_frames(frames, set_median)
    final_diagnostic = analyze_signal(processed_frames)
    
    # Unused diagnostic branches (misleading paths)
    security_hash = 0
    for c in "aerospace_v2":
        security_hash += ord(c) ^ (set_median + 5)
    
    debug_trace = []
    for i, f in enumerate(frames):
        debug_trace.append(f"Step{i}: {f['data'] >> (i % 3)}")
    
    # OUTPUT REQUIRED VALUE
    print(f"Result: {final_diagnostic}")


def preprocess_frames(frame_list, mask_value):
    # Apply conditional filtering based on dynamic criteria
    result = []
    base_shift = 3
    
    # Use enumerate to track position
    for pos, item in enumerate(frame_list):
        temp_val = item['data']
        
        # Complex conditional bypass
        if pos % 4 == 0:
            temp_val = temp_val ^ 7
        elif pos % 4 == 1:
            temp_val = temp_val & 15
        elif pos % 4 == 2:
            temp_val = temp_val | base_shift
        else:
            temp_val = temp_val + (pos // 2)
        
        # Additional transformation
        if item['weighted'] > 4.0:
            temp_val = int(math.sqrt(temp_val ** 2 + mask_value))
        
        result.append({'seq': pos, 'value': temp_val, 'tag': item['id']})
    
    return result

def analyze_signal(data_blocks):
    # Final computation using transformed values
    accumulator = 0
    pattern_match = 0
    
    # Dictionary-based state tracking
    state_log = {}
    for block in data_blocks:
        seq = block['seq']
        val = block['value']
        
        # Key arithmetic logic
        if seq % 3 == 0:
            accumulator += val * 2
        elif seq % 3 == 1:
            accumulator -= (val // 2)
        else:
            accumulator += (val % 7) * 3
        
        # State recording (irrelevant to final result)
        state_log[seq] = {
            'input': val,
            'acc': accumulator,
            'phase': seq % 3
        }
        
        # Pattern detection red herring
        if val > 15 and seq < 5:
            pattern_match += 1
    
    # Final adjustment based on logical conditions
    if pattern_match >= 2:
        accumulator = accumulator ^ 255  # Bitwise distraction
    else:
        accumulator = accumulator + (pattern_match * 10)  # Actual path taken
    
    # Secondary validation (unused)
    validation_key = sum(v['acc'] for v in state_log.values()) % 1000
    
    return accumulator

if __name__ == '__main__':
    main()