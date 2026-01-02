import math

def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing block (dead path)
    if len(raw_samples) == 0:
        return -1
    
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    if not filtered:
        return 0
    
    # Distractor: complex but unused transformation
    transformed = []
    for val in raw_samples:
        temp_a = math.sin(val * 0.5)
        temp_b = math.cos(val * 0.25)
        transformed.append(temp_a + temp_b if temp_a > 0 else temp_b)
    
    # Real logic begins: signal coherence calculation
    coherence_score = sum(1 for x in filtered if x > threshold) / len(filtered)
    spike_count = sum(1 for x in filtered if x > 1.5)
    
    # Bit manipulation red herring (appears important but unused later)
    packed_diagnostics = 0
    packed_diagnostics |= int(coherence_score * 100)
    packed_diagnostics <<= 8
    packed_diagnostics |= min(spike_count, 255)
    
    return coherence_score

def validate_calibration_frame(frame_data):
    # Unused validation function (decoy)
    checksum = 0
    for i, val in enumerate(frame_data):
        checksum ^= int(val * 100) + i
    return checksum % 16 == 0

def compute_adaptive_weight(sequence, base_factor=0.33):
    n = len(sequence)
    if n < 2:
        return base_factor
    
    # Red herring: entropy-like calculation
    entropy = 0.0
    freq_map = {}
    for x in sequence:
        freq_map[x] = freq_map.get(x, 0) + 1
    for count in freq_map.values():
        p = count / n
        entropy -= p * math.log2(p) if p > 0 else 0
    
    # Actual weight logic
    trend = sum(sequence[i] <= sequence[i+1] for i in range(n-1))
    stability = trend / (n - 1) if n > 1 else 1
    return base_factor * (0.5 + stability / 2)

def aggregate_metrics(chains, key):
    total = 0.0
    scaling_factor = key & 0xFF
    
    # Complex nested structure with distractors
    for idx, chain in enumerate(chains):
        # Irrelevant unpacking and conditional expression
        mode_flag = 'A' if (key >> idx) & 1 else 'B'
        adjustment = 1.5 if mode_flag == 'A' else 0.8
        
        # Fake recursive depth (non-recursive in practice)
        temp_buffer = []
        for item in chain:
            # Simulated multi-stage processing
n            stage1 = item * adjustment
            stage2 = stage1 ** 0.5 if stage1 > 0 else 0
            stage3 = math.floor(stage2 * 10) / 10  # quantize
            temp_buffer.append(stage3)
        
        # Real aggregation step
        if len(temp_buffer) >= 2:
            # Use min/max/average under distraction
            buffer_max = max(temp_buffer)
            buffer_min = min(temp_buffer)
            buffer_avg = sum(temp_buffer) / len(temp_buffer)
            
            # True contribution to result
            dynamic_offset = (buffer_max - buffer_min) * buffer_avg
            total += dynamic_offset * (idx + 1)
        
        # Dead code: modular arithmetic decoy
        cyclic_sum = 0
        for x in temp_buffer:
            cyclic_sum = (cyclic_sum + int(x * 10)) % 97
    
    # Final computation using only relevant accumulated value
    final_scale = scaling_factor / 100.0
    return total * final_scale

# Main execution context
sensor_readings = [0.88, 1.02, 0.95, 1.18, 0.72, 1.31, 0.65, 0.91]
calibration_sequence = [0.5, 0.7, 0.6, 0.8, 0.75]

# Irrelevant intermediate steps
integrity = analyze_signal_integrity(sensor_readings)
weight = compute_adaptive_weight(calibration_sequence)

# Fake data structure construction
processing_chain = [
    [integrity * 100],  # disguised input
    [weight * 200, 150],
    [80, 90, 100]
]

validation_key = 0xABCD  # Full 16-bit value; only low byte matters

# Critical statement
final_diagnostic = aggregate_metrics(processing_chain, validation_key)

print(f"Result: {final_diagnostic}")