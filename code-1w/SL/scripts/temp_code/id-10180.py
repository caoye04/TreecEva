import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading transformation chain
def transform_value(val, mode='basic'):
    if mode == 'advanced':
        val = (val * 7) ^ 45
    elif mode == 'legacy':
        val = val | 256
    return val & 255  # Clamp to byte range

# Auxiliary function with red herring logic
def analyze_pattern(seq):
    histogram = [0] * 256
    for item in seq:
        histogram[item % 256] += 1
    # Distractor: unused statistical computation
    avg_freq = sum(histogram) / len([h for h in histogram if h > 0])
    unique_count = len(set(seq))
    return unique_count > 50  # Never actually used

# Core processing pipeline with relevant and irrelevant steps
def process_pipeline(data):
    # Initial filtering (relevant)
    filtered = [x for x in data if x % 3 != 0]
    
    # Irrelevant normalization
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    
    # Bit manipulation stage (partially relevant)
    processed_bits = []
    for num in filtered:
        shifted = (num << 2) & 0xFF
        flipped = shifted ^ 0xAA
        if flipped > 100:
            flipped = flipped >> 1
        processed_bits.append(flipped)
    
    # Set operations with distractors
    seen = set()
    duplicates = set()
    cleaned = []
    for val in processed_bits:
        if val in seen:
            duplicates.add(val)
        else:
            seen.add(val)
            cleaned.append(val)
    
    # String-based flag check (uses string method - conditionally relevant)
    control_flag = 'enable_final_shift'
    enable_shift = 'enable' in control_flag and control_flag.endswith('shift')
    
    # Conditional expression with actual impact
    shift_amount = 1 if enable_shift else 0
    
    # Critical arithmetic with modular adjustment
    total = 0
    for idx, val in enumerate(cleaned):
        contribution = val * (idx + 1)
        if idx % 2 == 0:
            total += contribution
        else:
            total -= contribution
    
    # Final transformation (key step)
    if total < 0:
        total = abs(total) ^ 0xFFFF
    final_output = (total + len(duplicates)) % 97
    
    # Dead code: complex but unused structure
    summary_stats = {
        'range': max(cleaned) - min(cleaned),
        'entropy': sum(v * math.log(v + 1e-8) for v in normalized),
        'mode': max(set(cleaned), key=cleaned.count)
    }
    
    return final_output

# Generate deterministic input (avoid randomness)
data_stream = list(range(10, 121, 7))  # [10, 17, 24, ..., 118]

# Execute main logic
intermediate_result = transform_value(sum(data_stream), mode='advanced')
flag_check = analyze_pattern(data_stream)
final_output = process_pipeline(data_stream)

print(f"Result: {final_output}")