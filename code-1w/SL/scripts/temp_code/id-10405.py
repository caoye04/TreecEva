from collections import defaultdict, Counter

# Simulated sensor data stream with metadata tags
data_stream = [
    (1024, 'temp', 'sensor_A'), (2048, 'pressure', 'sensor_B'),
    (512, 'temp', 'sensor_A'), (4096, 'humidity', 'sensor_C'),
    (1024, 'pressure', 'sensor_B'), (256, 'temp', 'sensor_D')
]

# Irrelevant auxiliary mapping (distractor)
unit_conversion = {
    'temp': lambda x: (x * 9/5) + 32,
    'pressure': lambda x: x * 0.1,
    'humidity': lambda x: x / 10
}

# Misleading precomputation with unused result (red herring)
aggregated_stats = defaultdict(lambda: {'count': 0, 'total': 0})
for val, typ, src in data_stream:
    aggregated_stats[typ]['count'] += 1
    aggregated_stats[typ]['total'] += val

unused_checksum = sum(v['total'] for v in aggregated_stats.values()) % 1024

# Core transformation pipeline
transformation_chain = [
    lambda x: x << 2,           # Multiply by 4 via bit shift
    lambda x: x ^ 0xFF,         # XOR mask (bit manipulation)
    lambda x: x % 8192          # Bound within range
]

# Dead function - never called (dead code path)
def legacy_calibrate(data):
    return [d * 0.95 for d in data]

# Buffer preprocessing with slicing and filtering
stream_buffer = [
    item[0] for item in data_stream 
    if item[1] in ['temp', 'pressure']
][:10]

# Secondary buffer that looks important but isn't used later (distractor)
analysis_buffer = [item for item in data_stream if item[2].endswith('_B')]
buffer_summary = Counter([item[2] for item in analysis_buffer])

# Real processing function with nested logic
def process_value(x):
    temp = x
    for func in transformation_chain:
        temp = func(temp)
    return temp + 1

# Higher-order function combining map and reduce patterns
def process_data(buffer):
    mapped = list(map(process_value, buffer))
    
    # Conditional reduction logic with red herring condition
    reduction_key = len(mapped) > 3
    if reduction_key:
        acc = 0
        for i, val in enumerate(mapped):
            if i % 2 == 0:
                acc += val * 2
            else:
                acc -= val // 3
        final = acc
    else:
        final = sum(mapped) // len(mapped)
    
    # Additional transformation with tuple unpacking distraction
    meta_tuple = (final, final % 1000)
    result, _ = meta_tuple  # Unused second element
    
    # Final adjustment based on modular arithmetic
    return (result + (result & 511)) ^ 0xAAA

# Critical execution point
final_output = process_data(stream_buffer)

print(f"Result: {final_output}")