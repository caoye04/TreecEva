import itertools

# Simulated network telemetry data from 5G edge nodes
def collect_telemetry(slice_id, timestamp):
    base = (slice_id * 97 + timestamp % 13) % 100
    return [base + i * 3 for i in range(8)]

# Misleading decoy function - appears relevant but unused in critical path
def legacy_checksum(data):
    acc = 0
    for x in data:
        acc = (acc << 1) ^ x & 0xFFFF
    return acc % 7 == 0

# Data transformation pipeline stage 1: normalize signal amplitudes
def normalize_amplitudes(raw_readings):
    min_val, max_val = min(raw_readings), max(raw_readings)
    if max_val == min_val:
        return [0.5] * len(raw_readings)
    return [(x - min_val) / (max_val - min_val) for x in raw_readings]

# Unused auxiliary function - red herring for code analysis
def phase_shift_correction(signal, shift=3):
    return signal[-shift:] + signal[:-shift]

# Critical aggregation logic across network slices
def aggregate_metrics(slices, log_entry):
    cumulative_score = 0
    
    # Irrelevant preprocessing on log metadata
    tokens = log_entry.split('\n')
    debug_tags = [t for t in tokens if t.startswith('DBG')]
    priority_flag = len(debug_tags) > 2
    
    # Core processing with distractor variables
    slice_contributions = []
    noise_floor = 0
    for idx, sid in enumerate(slices):
        raw_data = collect_telemetry(sid, 16923456 + idx)
        
        # Distractor: irrelevant noise simulation
        if idx % 4 == 0:
            noise_floor += sum(x % 7 for x in raw_data[:4])
        
        normalized = normalize_amplitudes(raw_data)
        
        # Extract key pattern using slicing and transformation
        mid_window = normalized[2:6]
        pattern_energy = sum(mid_window) * 100
        
        # Bit manipulation red herring
        encoded = int(pattern_energy) ^ 0xAA55
        if encoded & 0xFF == 0x55:
            pattern_energy += 1.5
        
        slice_contributions.append(round(pattern_energy))
    
    # Real computation hidden among distractions
    filtered = [x for x in slice_contributions if x % 2 == 1]  # Only odd contributions count
    
    # Decoy accumulation with unused variables
    avg_noise = noise_floor / max(len(slice_contributions), 1)
    temp_buffer = list(itertools.accumulate(slice_contributions))
    checkpoint_hash = sum(temp_buffer[i] * (i+1) for i in range(len(temp_buffer))) % 1000
    
    # Actual answer derivation
    valid_count = len(filtered)
    total_power = sum(filtered)
    
    # Final diagnostic computed from meaningful subset
    final_diagnostic = total_power * valid_count
    
    # Dead code branch - never executed due to above logic
    if priority_flag and checkpoint_hash < 0:
        final_diagnostic = int(avg_noise)
        
    return final_diagnostic

# Setup realistic input data
network_slices = [12, 15, 18, 21, 24]
system_log = "LOG:INIT\nDBG:SYNC_OK\nDBG:FLOW_12A\nINFO:RX_READY"

# Execute critical statement
target_result = aggregate_metrics(network_slices, system_log)
print(f"Target result: {target_result}")