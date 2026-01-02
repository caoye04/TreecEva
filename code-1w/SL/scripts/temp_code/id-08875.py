import math

# Simulated sensor data and configuration for environmental monitoring system
data_stream = [14, 72, 33, 51, 24, 88, 61, 45, 37, 77, 29, 63, 91, 55, 42]
raw_timestamps = [1623450000 + i*60 for i in range(len(data_stream))]
calibration_factors = {14: 1.05, 72: 0.98, 33: 1.02, 51: 0.99, 24: 1.01}

# Irrelevant auxiliary mappings (distractor)
day_night_map = {'day': 1, 'night': 0}
temperature_zone = {'cold': -1, 'moderate': 0, 'hot': 1}

# System thresholds (some are decoys)
thresholds = {
    'critical': 85,
    'warning': 70,
    'info': 50,
    'debug': 30,
    'trace': 10
}

# Misleading preprocessing (dead code path)
def legacy_filter(data):
    """Old algorithm, no longer used."""
    result = []
    for x in data:
        if x > 25 and x % 5 == 0:
            result.append(x * 1.1)
    return result

# Unused transformation function (red herring)
def transform_amplitude(signal, factor=1.5):
    return [math.sin(x / 10) * factor for x in signal]

# Auxiliary state tracker (partially relevant but mostly noise)
state_log = {}
for idx, val in enumerate(data_stream):
    state_log[idx] = {
        'raw': val,
        'is_anomaly': val > 85,
        'phase': 'A' if val % 3 == 0 else 'B' if val % 3 == 1 else 'C',
        'dummy_flag': (val ^ 7) & 1
    }

# Real-time filter mask (used later)
active_mask = [1 if t % 2 == 0 else 0 for t in raw_timestamps]

# Apply mask to get filtered indices (actual relevance begins here)
filtered_indices = [i for i, m in enumerate(active_mask) if m == 1]

# Extract subset using list comprehension and dictionary augmentation
filtered_data = []
for i in filtered_indices:
    entry = {
        'value': data_stream[i],
        'calibrated': data_stream[i] * calibration_factors.get(data_stream[i], 1.0),
        'index': i,
        'weight': 0.8 if data_stream[i] > 60 else 0.6
    }
    filtered_data.append(entry)

# Configuration with multiple red herrings
config = {
    'gain': 1.25,
    'offset': -5,
    'algorithm': 'adaptive_mean',
    'window_size': 7,  # unused
    'decay_factor': 0.9,  # unused
    'use_normalization': True,
    'mode': 'production',
    'buffer_limit': 1000,  # irrelevant
    'sampling_rate': 1.0  # irrelevant
}

# Decoy statistical summary (never called)
def compute_moving_stats(sequence, window=3):
    stats = []
    for i in range(len(sequence)):
        window_slice = sequence[max(0, i-window+1):i+1]
        mean_val = sum(window_slice) / len(window_slice)
        variance = sum((x - mean_val)**2 for x in window_slice) / len(window_slice)
        stats.append({'mean': mean_val, 'variance': variance})
    return stats

# Core processing function with embedded distractions
def process_signals(entries, settings):
    accumulated = 0
    adjustment = settings['gain']
    shift = settings['offset']
    total_weighted = 0.0
    count = 0
    
    # Spurious internal mapping (mostly irrelevant)
    category_map = {}
    for item in entries:
        cat = 'high' if item['value'] > 50 else 'low'
        category_map[item['index']] = {'category': cat, 'flag': (item['value'] << 2) & 6}
    
    # Actual computation loop
    for item in entries:
        raw_val = item['value']
        calibrated = item['calibrated']
        weight = item['weight']
        
        # Simulated signal fusion
        fused = (raw_val * 0.7) + (calibrated * 0.3)
        
        # Fake branch (misleading - looks important but doesn't affect output)
        if settings['use_normalization']:
            normalized = fused / (max(data_stream) / 100)
            adjusted_norm = (normalized * adjustment) + shift
        
        # Key calculation (only this affects final output)
        intermediate = (fused + shift) * adjustment * weight
        accumulated += intermediate
        total_weighted += weight
        count += 1
        
        # Early termination decoy (never triggered)
        if raw_val == 999:
            break
    
    # Final aggregation
    if total_weighted > 0:
        result = accumulated / total_weighted
    else:
        result = 0
    
    # Injecting phantom logic (unused)
    final_diagnostics = {
        'input_count': len(entries),
        'output_stability': math.cos(result % 10),
        'version': 'v2.1'
    }
    
    return result

# Critical execution point
final_output = process_signals(filtered_data, config)

# Print result as required
print(f"Result: {final_output}")