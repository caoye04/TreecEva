import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [127, 63, 191, 31, 255]
    processed = []
    for val in raw:
        if val & 32:  # Check bit presence
            processed.append(val ^ 15)
        else:
            processed.append(val | 48)
    return processed

def generate_checksum(data):
    chk = 0
    for d in data:
        chk ^= d * 3
    return chk % 256

def extract_flags(value):
    flags = {}
    flags['bit_0'] = bool(value & 1)
    flags['bit_4'] = bool(value & 16)
    flags['bit_7'] = bool(value & 128)
    return flags

def decode_sequence(raw_seq):
    decoded = []
    temp_sum = 0
    for item in raw_seq:
        temp_sum += (item >> 2) & 7
        decoded.append({
            'shifted': item >> 3,
            'masked': item & 63,
            'inverted': 255 - item
        })
    # Irrelevant aggregation
    stats = {
        'total_shifts': temp_sum,
        'count': len(decoded),
        'max_masked': max(x['masked'] for x in decoded)
    }
    return decoded, stats

def compute_entropy(values):
    # Dummy entropy calculation (not actually used in final result)
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def filter_outliers(data_list):
    avg = sum(data_list) / len(data_list)
    dev = [abs(x - avg) for x in data_list]
    threshold = avg * 0.5
    filtered = [x for x in data_list if abs(x - avg) <= threshold]
    return filtered  # Not used in main logic

def build_lookup_table(seeds):
    table = {}
    for i, seed in enumerate(seeds):
        key = f"entry_{i % 4}"
        if key not in table:
            table[key] = []
        transformed = ((seed ^ 92) + i) % 100
        table[key].append(transformed)
    # Dead-end transformation
    summary = {k: sum(v) // len(v) for k, v in table.items()}
    return table  # Unused in critical path

def analyze_pattern(log_entries, sensor_data):
    # Core logic begins
    accumulator = 0
    history = []
    
    for entry in log_entries:
        if entry['shifted'] > 15:
            accumulator += entry['masked']
        elif entry['masked'] < 30:
            accumulator -= entry['shifted']
        else:
            accumulator ^= entry['inverted'] % 23
        history.append(accumulator)
    
    # Secondary integration with sensor data
    signal_peak = max(sensor_data)
    base_offset = min(sensor_data)
    
    # Key computation branch
    if signal_peak > 100 and len(history) >= 4:
        trend = history[-1] - history[0]
        adjustment = (trend * (signal_peak & 7)) // 2
        accumulator += adjustment
    
    # Red herring: complex dictionary operation that doesn't affect outcome
    diagnostics_summary = {
        'stages': len(history),
        'peak_factor': signal_peak // 8,
        'adjust_log': [h % 10 for h in history if h > 0],
        'meta': {
            'version': '2.1',
            'valid': True,
            'checksum': generate_checksum(sensor_data)
        }
    }
    
    # Final transformation using only accumulator and base_offset
    final_value = (accumulator * 3) + base_offset
    return final_value

# Main execution flow
if __name__ == '__main__':
    # Primary data sources
    readings = collect_readings()
    
    # Distractor: unused filtering
    clean_readings = filter_outliers(readings)
    
    # Distractor: lookup table generation (dead code)
    lookup = build_lookup_table(readings)
    
    # Distractor: entropy calculation on irrelevant aspect
    entropy_metric = compute_entropy([r & 31 for r in readings])
    
    # Core diagnostic trace
    raw_diagnostics = [0b11001101, 0b01101110, 0b10011101, 0b00101111, 0b11110001]
    decoded_diagnostics, diag_stats = decode_sequence(raw_diagnostics)
    
    # Flag extraction - completely irrelevant
    all_flags = [extract_flags(x) for x in raw_diagnostics]
    
    # Critical function call
    final_diagnostic = analyze_pattern(decoded_diagnostics, readings)
    
    # Output result
    print(f"Result: {final_diagnostic}")