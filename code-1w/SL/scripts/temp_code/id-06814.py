from collections import defaultdict, Counter
import math

def analyze_signal_strength(raw_samples):
    # Irrelevant transformation (dead path)
    temp_adjusted = [x * 1.05 for x in raw_samples if x > 0]
    
    # Real processing begins: filter anomalies using threshold logic
    threshold = sum(raw_samples) / len(raw_samples)
    filtered_samples = [x for x in raw_samples if abs(x - threshold) < 15]

    # Distractor: complex but unused frequency map
    freq_map = defaultdict(int)
    for val in raw_samples:
        freq_map[val] += 1
    
    # Decoy statistical computation (not used later)
    mean_val = sum(filtered_samples) / len(filtered_samples)
    variance = sum((x - mean_val) ** 2 for x in filtered_samples) / len(filtered_samples)
    std_dev = math.sqrt(variance)
    
    # Bit manipulation red herring
    magic_key = 0
    for i, val in enumerate(filtered_samples):
        if i % 3 == 0:
            magic_key ^= int(val) & 0xFF
    
    # Unused recursive smoothing function (decoy)
    def smooth_recursively(data, depth=0):
        if depth >= 2 or len(data) < 2:
            return data
        return smooth_recursively([(data[i] + data[i+1]) / 2 for i in range(len(data)-1)], depth + 1)
    
    # Real signal: categorize by band
    bands = defaultdict(list)
    for val in filtered_samples:
        if val < 40:
            bands['low'].append(val)
        elif val < 70:
            bands['medium'].append(val)
        else:
            bands['high'].append(val)
    
    # Only this part matters: count valid peaks above 50 after filtering
    peak_candidates = [x for x in filtered_samples if x > 50]
    
    # String-based distractor: simulate metadata parsing
    header_info = "AX7-PRIME|VER:3.1|MODE:AUTO"
    tokens = header_info.split('|')
    mode_flag = tokens[2].split(':')[1] if len(tokens) > 2 else 'MANUAL'
    
    # Fake checksum from string IDs (irrelevant)
    checksum = 0
    for char in mode_flag:
        checksum += ord(char) ^ 0x55
    
    # Another decoy structure
    stats_summary = {
        'count': len(filtered_samples),
        'peaks': len(peak_candidates),
        'checksum': checksum,
        'band_distribution': {k: len(v) for k, v in bands.items()}
    }
    
    # This is discarded — just misdirection
    _ = json.dumps(stats_summary) if 'json' in globals() else str(stats_summary)

    return peak_candidates

def process_readings(data_chunk):
    # Secondary distraction: character frequency analysis on dummy ID
    device_id = "SENSOR-GAMMA-9X"
    char_freq = Counter(device_id.replace('-', ''))
    offset = sum(v ** 2 for v in char_freq.values()) % 7
    
    # Real logic: apply XOR folding on data_chunk
    accumulator = 0
    for i, val in enumerate(data_chunk):
        rotated = (val << 1) | (val >> 7)  # 8-bit rotate left simulation
        masked = rotated & 0xFF
        accumulator ^= masked
    
    # Add offset from string analysis (this actually affects result)
    accumulator += offset
    
    # Red herring: floating point conversion chain
    temp_float = float(accumulator)
    adjusted_float = math.sin(temp_float) * 1000
    rounded_int = int(round(adjusted_float))
    
    # Final trap: only use integer before float conversion
    return accumulator  # final answer comes from here

# Simulate diagnostic pipeline
raw_diagnostics = [12, 45, 55, 67, 34, 78, 23, 56, 61, 88, -5, 54, 72, 18, 91, 47]

# Misleading pre-processing step (partially relevant)
cleaned_data = [x for x in raw_diagnostics if x >= 0]

# Key data flow
filtered_data = analyze_signal_strength(cleaned_data)

# Critical statement: what is the value of final_diagnostic after this?
final_diagnostic = process_readings(filtered_data)

print(f"Target result: {final_diagnostic}")