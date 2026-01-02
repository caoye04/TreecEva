import math

# Simulated sensor calibration and diagnostic system
def collect_readings(base_value, iterations):
    readings = []
    temp_offset = 0.0
    for i in range(iterations):
        if i % 2 == 0:
            temp_offset += math.sin(i) * base_value / 10
        else:
            temp_offset -= math.cos(i) * base_value / 15
        raw = (base_value + i * 1.5) + temp_offset
        readings.append(round(raw, 3))
    return readings


def apply_correction(data_stream, factor):
    corrected = []
    noise_floor = 0.05
    for val in data_stream:
        adjusted = val * factor
        # Simulate noise suppression
        if abs(adjusted) > noise_floor:
            adjusted = math.copysign(max(abs(adjusted) - noise_floor, 0), adjusted)
        corrected.append(round(adjusted, 4))
    return corrected


def generate_threshold_map(levels):
    # Irrelevant red herring: builds a complex map not fully used
    thresholds = {}
    for i in range(1, levels + 1):
        key = f"level_{i}"
        thresholds[key] = {
            'upper': 100 * (1.2 ** i),
            'lower': 5 * (0.8 ** i),
            'weight': round(math.log(i + 1) / sum(1/j for j in range(1, i+2)), 3) if i % 2 == 0 else 0.1
        }
    # But only this scalar is actually used later
    magic_constant = sum(th['upper'] * th['weight'] for th in thresholds.values()) / levels
    return magic_constant


def encode_sequence(nums):
    # Unused decoy function - looks important but never called
    result = []
    for n in nums:
        hex_chunk = hex(int(n) ^ 0xFF)[2:].zfill(4)
        result.append(hex_chunk[::-1])
    return ''.join(result)


def validate_integrity(payload):
    # Dead code path - included to mislead
    checksum = 0
    for c in payload:
        if c.isdigit():
            checksum ^= int(c)
    return checksum % 7 == 0

# Critical processing function
def process_metrics(sequence, config_threshold):
    total = 0
    peak = max(sequence)
    valley = min(sequence)
    span = peak - valley
    
    # Real logic starts here — distractors above
    normalized = [x / span for x in sequence]
    
    # Conditional expression with bit manipulation
    adjustment = (config_threshold >> 2) if span > 50 else (config_threshold << 1)
    
    for idx, val in enumerate(normalized):
        # Mix modular arithmetic and trigonometry
        angle = (idx % 8) * math.pi / 4
        component = val * math.cos(angle)
        
        # Interleaved update with conditional override
        contribution = component * adjustment
        if idx % 3 == 0:
            contribution = contribution if contribution > 0 else -contribution
        elif idx % 5 == 0:
            # Decoy branch — condition never met due to loop length
            contribution = math.tanh(contribution)
        
        total += contribution
    
    # Final transformation using string-based modulus trick
    str_key = ''.join(str(int(abs(total * (i+1))))[-1] for i in range(3))
    digit_sum = sum(int(d) for d in str_key)
    final_score = total * (digit_sum or 1)
    
    # Key assignment: this is the target variable
    final_diagnostic = int(round(final_score * 1000)) % 97843
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# --- Simulation Entry Point ---
if __name__ == "__main__":
    # Collect real data
    raw_data = collect_readings(base_value=42.5, iterations=12)
    calibrated_data = apply_correction(raw_data, factor=0.93)
    
    # Generate configuration (only magic_constant used)
    threshold_map = generate_threshold_map(levels=6)
    
    # Build composite input
    calibration_sequence = [int(x * 10) / 10 for x in calibrated_data]  # Round to 1 decimal
    
    # Introduce misleading secondary variables
    audit_trace = [calibration_sequence[i] for i in range(0, len(calibration_sequence), 2)]
    compression_ratio = len(raw_data) / len(audit_trace) if audit_trace else 0
    
    # Unused complex structure
    metadata_bundle = {
        'version': '3.7.1',
        'checksum': sum(int(b) for b in bin(hash(tuple(calibrated_data[:3])))[-8:]),
        'flags': (0b1010 ^ len(calibrated_data)) & 0xF,
        'payload': encode_sequence([int(x) for x in raw_data])
    }
    
    # Validate something irrelevant
    _ = validate_integrity(metadata_bundle['payload'])
    
    # --- KEY EXECUTION POINT ---
    final_diagnostic = process_metrics(calibration_sequence, threshold_map)
