import math

# Simulated sensor data processing system for environmental monitoring
def collect_readings():
    raw_readings = [127, 255, 83, 191, 45]
    scale_factor = 0.75
    adjusted = [r * scale_factor for r in raw_readings]
    return adjusted

# Irrelevant transformation: color space conversion (red herring)
def rgb_to_hsv(r, g, b):
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val
    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360
    return (h, 0, max_val)

# Unused function: time series padding (dead code path)
def pad_sequence(seq, length, mode='zero'):
    while len(seq) < length:
        if mode == 'zero':
            seq.append(0)
        elif mode == 'repeat':
            seq.append(seq[-1])
    return seq

# Core signal processing with distractors embedded
def clean_signal(signal):
    filtered = []
    noise_floor = 50.0
    for x in signal:
        if x > noise_floor:
            # Apply logarithmic compression
            compressed = math.log(x) * 10
            filtered.append(round(compressed, 2))
        else:
            filtered.append(0)
    return filtered

# Data enrichment with string metadata (distractor usage)
def annotate_data(data_list):
    labels = [f"sensor_{i}_active" for i in range(len(data_list))]
    status_flags = [lbl.upper().replace('_', '-') for lbl in labels]  # Use of string methods
    annotated = {lbl: val for lbl, val in zip(status_flags, data_list)}
    return annotated

# Conditional transformation using lambda and modular arithmetic
def transform_data(entries):
    processor = lambda x: (x ** 2) % 19 if x > 0 else 0
    return [processor(e) for e in entries]

# Recursive filtering function based on bit count
def count_set_bits(n):
    return 1 if n <= 1 else (n & 1) + count_set_bits(n >> 1)

def filter_by_bit_density(values):
    densities = [count_set_bits(int(v)) / v.bit_length() if v > 0 else 0 for v in values]
    return [v for v, d in zip(values, densities) if d >= 0.5]

# Main processing pipeline
def process_metrics(data, cfg):
    stage1 = [math.sqrt(x) for x in data if x > 10]
    
    # Conditional expression mix
    threshold = cfg['mode'] if 'mode' in cfg and cfg['mode'] > 5 else 7
    stage2 = [x + threshold for x in stage1]
    
    # Bitwise interference
    mask = 0b1111
    stage3 = [(int(x) & mask) ^ 0b1010 for x in stage2]
    
    # Final aggregation
    total = sum(stage3)
    adjustment = math.sin(math.pi / total) if total != 0 else 0
    result = int(total - adjustment * 100)
    return result

# Execution flow with irrelevant side computations
def main():
    # Step 1: Collect and clean raw sensor readings
    raw_data = collect_readings()
    cleaned = clean_signal(raw_data)
    
    # Irrelevant color processing (red herring)
    dummy_color = rgb_to_hsv(255, 128, 0)
    
    # Transform data using modular arithmetic
    transformed_data = transform_data([int(c) for c in cleaned if c > 0])
    
    # Filter by binary density
    filtered_stream = filter_by_bit_density(transformed_data)
    
    # Annotate with string-based labels (distractor)
    annotated_output = annotate_data(filtered_stream)
    
    # Configuration with decoy fields
    config = {
        'mode': 6,
        'timeout': 30,
        'retries': 3,
        'debug_trace': True,
        'log_level': 'verbose'
    }
    
    # Critical statement
    final_diagnostic = process_metrics(transformed_data, config)
    
    # Dead-end computation (misleading intermediate)
    shadow_copy = [x * 2 for x in transformed_data]
    temp_result = sum(shadow_copy) // 2 if shadow_copy else 0
    
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Run and output result
main()