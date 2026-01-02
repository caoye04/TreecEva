from collections import defaultdict, Counter

# Simulated sensor data aggregation for a health monitoring system
def collect_readings():
    readings = []
    for i in range(50):
        if i % 7 == 0:
            readings.append((i, (36.5 + (i % 4)), (70 + (i * 1.5) % 30)))
    return readings

# Irrelevant auxiliary function - dead code path
def compute_strain_index(heart_rates):
    total = 0
    for hr in heart_rates:
        if hr > 100:
            total += (hr - 100) ** 0.8
    return total / len(heart_rates) if heart_rates else 0

# Data transformation with red herring operations
def transform_readings(raw):
    transformed = []
    temp_stats = defaultdict(float)
    count_log = Counter()
    
    for seq, temp, bpm in raw:
        adjusted_temp = round(temp + (0.1 * (seq % 3)), 2)
        risk_flag = False
        
        # Distractor logic block - looks important but unused
        if adjusted_temp > 38.0:
            risk_flag = True
            temp_stats['high'] += 1
        elif adjusted_temp < 36.0:
            temp_stats['low'] += 1
        else:
            temp_stats['normal'] += 1
        
        # Only this line matters: filtering relevant entries
        if seq % 5 == 0 and bpm > 85:
            transformed.append({'seq': seq, 'value': bpm * 0.9})
            
        count_log[seq % 4] += 1  # Red herring accumulation

    # Another decoy computation
    avg_deviation = sum(abs(v - 1) for v in temp_stats.values()) / len(temp_stats) if temp_stats else 0
    
    return transformed

# Core processing with conditional logic and modular arithmetic
def generate_thresholds(base):
    thresholds = {}
    for i in range(8):
        key = f"level_{i}"
        # Complex-looking but partially irrelevant calculation
        core_val = (base * (i + 1)) % (15 + i)
        extra_noise = (i ** 2) % 7
        thresholds[key] = core_val - (extra_noise // 2)
    return thresholds

# Main analysis function with misleading intermediate steps
def process_metrics(data, config):
    accumulator = 0
    sequence_sum = 0
    debug_flags = [False, True, False]
    
    # Real logic begins
    for entry in data:
        seq_id = entry['seq']
        raw_value = entry['value']
        
        # Key computation branch
        if seq_id % 3 == 0:
            mod_val = int(raw_value) % 11
            if mod_val in [3, 6, 9]:
                accumulator += mod_val * 2
            else:
                accumulator -= mod_val
        
        # Dead logic branch - looks like it does something
        flag_index = seq_id % 3
        if debug_flags[flag_index] and raw_value > 100:
            sequence_sum += seq_id % 7
    
    # Decoy normalization
    if accumulator > 50:
        normalized = accumulator * 0.95
    else:
        normalized = accumulator + (accumulator * 0.1)
    
    # Final mapping based on configuration keys
    offset = 0
    for k, v in config.items():
        if int(k.split('_')[1]) % 2 == 1:  # only odd levels contribute
            offset += v % 10
    
    final_diagnostic = accumulator + offset  # Actual answer depends on this
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    # Initialize with realistic context
    raw_sensor_data = collect_readings()
    processed_entries = transform_readings(raw_sensor_data)
    
    # Generate configuration map (only specific parts used)
    threshold_map = generate_thresholds(12)
    
    # Unused variables - red herrings
    baseline_risk = compute_strain_index([entry['value'] for entry in processed_entries])
    summary_counts = Counter([int(e['value']) // 10 for e in processed_entries])
    
    # Critical execution point
    final_diagnostic = process_metrics(processed_entries, threshold_map)