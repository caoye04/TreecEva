def analyze_frequency_profile(raw_spectrum):
    # Irrelevant signal preprocessing (dead path)
    normalized = [x / max(raw_spectrum) for x in raw_spectrum]
    filtered = [x for x in normalized if x > 0.1]
    peak_count = len([x for x in filtered if x > 0.8])

    # Distractor: complex but unused transformation
    shifted = [(x * 2 + 1) % 1 for x in normalized]
    entropy_approx = sum([abs(shifted[i] - shifted[i-1]) for i in range(1, len(shifted))])

    # Relevant path begins: extract key bands
    low_band = raw_spectrum[::3]
    mid_band = raw_spectrum[1::3]
    high_band = raw_spectrum[2::3]

    # Compute diagnostic metrics
    avg_low = sum(low_band) / len(low_band)
    avg_mid = sum(mid_band) / len(mid_band)
    avg_high = sum(high_band) / len(high_band)

    # Bit manipulation on averages (convert to fixed-point int for bit ops)
    fp_low = int(avg_low * 1000)
    fp_mid = int(avg_mid * 1000)
    fp_high = int(avg_high * 1000)

    # Key bitwise diagnostic signature
    signature = (fp_low ^ fp_mid) & fp_high | 0xABC  # Base interference

    return {'avgs': (avg_low, avg_mid, avg_high), 'signature': signature}


def encode_timestamp(tag, time_id):
    # String processing red herring
    encoded = ''.join(sorted(set(tag.lower())))
    shift_val = len(encoded) % 5
    # Unused result
    obfuscated = tag[::-1].upper() + str(time_id ^ (shift_val * 17))
    return obfuscated  # Not used later

# Simulated sensor input
sensor_log = [
    "ERR@214", "DBG@891", "INF@305", "WRN@776"
]

# Extract numeric codes using string methods (distraction)
timestamp_codes = [int(entry.split('@')[1]) for entry in sensor_log]
total_impulse = sum(timestamp_codes) // len(timestamp_codes)

# Real data source
base_sequence = [18, 24, 15, 30, 21, 36]

# Transform with multiple steps
squared = [x**2 for x in base_sequence]
doubled = [x*2 for x in squared]  # Dead path
modded = [x % 257 for x in doubled]  # Prime modulus distraction

# Core transformation chain
processed = []
for val in squared:
    temp = val
    temp = (temp + 13) * 7
    temp = temp ^ 0xFE  # Bit flip pattern
    temp = temp & 0xFF  # Clamp to 8-bit
    processed.append(temp)

data_checksum = sum(processed) & 0xFFFF

# Build frequency profile from processed data
profile = [processed[i] + processed[-i-1] for i in range(len(processed))]
result_set = analyze_frequency_profile(profile)

# Create threshold map with set operations (partially relevant)
signal_avgs = result_set['avgs']
high_performers = {i for i, x in enumerate(signal_avgs) if x > 50}
low_performers = {0, 1, 2} - high_performers
overlap_flag = len(high_performers & low_performers) > 0  # False, distraction

threshold_map = {
    'min_trigger': min(signal_avgs) * 1.5,
    'critical': max(signal_avgs) * 2.1,
    'base_offset': sum(signal_avgs) / 3
}

# String-based key generation (irrelevant)
config_key = "SysLog_2024"
key_parts = config_key.split('_')
crypto_tag = ''.join([p[0] for p in key_parts]).lower()
version_seed = int(key_parts[1]) % 100

# Actual signal transformation
transformed_data = []
for i, val in enumerate(processed):
    phase_shift = (val >> 2) ^ (i << 1)
    if i % 2 == 0:
        phase_shift = phase_shift ^ 0x1F
    transformed_data.append(phase_shift)

# Critical function with mixed logic
def process_signal(data, thresholds):
    # Initialize accumulators
    accumulator = 0
    history = []
    
    for step in range(len(data)):
        item = data[step]
        
        # Simulate conditional activation
        if step == 0:
            accumulator += item * 2
        elif step == 1:
            accumulator += item // 3
        else:
            # Complex condition with string comparison decoy
            mode_flag = "active" if item > 50 else "idle"
            adjustment = len(mode_flag)  # 5 or 4, irrelevant
            
            temp_val = item
            if temp_val % 2 == 0:
                temp_val = temp_val ^ 0x55
            else:
                temp_val = temp_val | 0x0F
            
            # Actual contribution
            scaled = (temp_val * (step + 1)) // 4
            accumulator += scaled
            
        # Update history (unused)
        snapshot = f"{accumulator:x}-{item:b}"
        history.append(snapshot)
    
    # Final computation
    base_score = accumulator
    
    # Apply threshold adjustments (only one matters)
    adj1 = base_score - thresholds['min_trigger']
    adj2 = base_score + thresholds['base_offset']
    final_adjustment = adj2  # This is the one actually used
    
    # Signature fusion
    sig = result_set['signature']
    fused = (int(final_adjustment) ^ sig) & 0xFFFFF
    
    # Final diagnostic code
    final_code = (fused * 3) // 7
    
    return final_code

# Execute critical statement
final_diagnostic = process_signal(transformed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")