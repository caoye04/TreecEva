from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_samples = [127, 64, 255, 32, 192, 16, 8, 0, 48, 96]
    scale_factor = 0.75
    processed = [x * scale_factor for x in raw_samples]
    return processed

# Irrelevant helper - distractor function (dead code path)
def legacy_checksum(data):
    acc = 0
    for val in data:
        acc = (acc + val) % 257
    return acc

# Misleading intermediate transformation (unused result)
def apply_noise_filter(signal):
    filtered = []
    for s in signal:
        if s > 50:
            filtered.append(s * 0.9)
        else:
            filtered.append(s * 1.1)
    temp_adjustment = sum(filtered) / len(filtered)  # Red herring
    return [f - temp_adjustment for f in filtered]

# Core logic: categorize signal bands
def categorize_amplitude_levels(readings):
    bands = defaultdict(int)
    for r in readings:
        if r < 30:
            bands['low'] += 1
        elif r < 75:
            bands['medium'] += 1
        else:
            bands['high'] += 1
    return bands

# Bit manipulation decoy - looks important but unused
def compute_bit_pattern(n):
    pattern = 0
    for i in range(8):
        if (n >> i) & 1:
            pattern ^= (i * 3)
    return pattern

# Main diagnostic engine
def generate_threshold_map(levels):
    base_map = {'low': 25, 'medium': 60, 'high': 100}
    adjusted = {}
    for k, v in levels.items():
        adjustment = (v % 7) * 2  # Non-linear tweak
        adjusted[k] = base_map[k] + adjustment
    # Decoy mutation
    adjusted['critical'] = 200
    return adjusted

# Signal quality analyzer - the actual key function
def analyze_signal_quality(buffer, thresholds):
    count_stats = Counter(buffer)
    scaled_values = [round(v * 1.25) for v in buffer if v > 0]
    
    # Real computation path
    total_weight = 0.0
    for val in scaled_values:
        if val < thresholds['low']:
            total_weight += 0.5
        elif val < thresholds['medium']:
            total_weight += 1.0
        elif val < thresholds['high']:
            total_weight += 1.75
        else:
            total_weight += 2.5
    
    # Introduce fake dependency
    dummy_offset = 0
    for k in thresholds.keys():
        dummy_offset += hash(k) % 10
    
    # Final calculation - answer derived here
    final_score = int(total_weight * 3) - 15  # Key formula
    
    # Unused complex structure - distraction
    diagnostics_report = {
        'version': '2.1',
        'metrics': {
            'entropy': 3.14159,
            'jitter': sum([abs(scaled_values[i] - scaled_values[i-1]) for i in range(1, len(scaled_values))]),
            'stability': 'nominal'
        }
    }
    
    return final_score

# Orchestration with red herrings
if __name__ == '__main__':
    # Step 1: Collect real data
    sensor_output = collect_sensor_readings()
    
    # Step 2: Generate level categories (used later)
    amplitude_profile = categorize_amplitude_levels(sensor_output)
    
    # Step 3: Create threshold map (actually used)
    threshold_config = generate_threshold_map(amplitude_profile)
    
    # Step 4: Apply fake filter (result discarded - distraction)
    noisy_copy = sensor_output.copy()
    _ = apply_noise_filter(noisy_copy)
    
    # Step 5: Compute irrelevant bit patterns over data (decoy loop)
    bit_sum = 0
    for sample in sensor_output[:3]:
        bit_sum += compute_bit_pattern(int(sample))
    
    # Step 6: Prepare buffer for analysis (key data)
    diagnostic_buffer = [int(x) for x in sensor_output if x > 10]
    
    # Step 7: Calculate legacy checksum (never used - red herring)
    verification_key = legacy_checksum(diagnostic_buffer)
    
    # Step 8: Actual critical computation
    final_diagnostic = analyze_signal_quality(diagnostic_buffer, threshold_config)
    
    # Output target result
    print(f"Result: {final_diagnostic}")