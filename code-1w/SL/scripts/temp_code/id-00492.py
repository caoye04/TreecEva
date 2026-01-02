from itertools import compress, count

# Domain-specific setup: sensor data validation with noise filtering
def analyze_sensor_stream(raw_readings):
    base_offset = 17
    threshold = 95
    scale_factor = 3
    decay_rate = 0.98  # Irrelevant in final calculation

    # Real-time calibration (distraction)
    calibrated = [int(x * decay_rate) for x in raw_readings]

    # Generate auxiliary sequences (mixed relevance)
    indices = list(count(1))
    flags = [x % 2 == 0 for x in indices[:len(raw_readings)]]
    
    # Filter valid high-signal readings (core logic step 1)
    filtered = list(compress(calibrated, (x > threshold for x in raw_readings)))

    # Secondary filter based on position parity (distraction)
    positional_filter = list(compress(filtered, (i % 3 == 0 for i in range(len(filtered)))))

    # Checksum pre-image computation (core logic step 2)
    accumulator = 0
    for val in filtered:
        if val % 2 == 0:
            accumulator ^= (val << 2)
        else:
            accumulator += (val >> 1)

    sum_filtered = accumulator + base_offset  # Core logic step 3

    # Mask generation with red herring bitwise chain
    magic_seed = 0xA3F7
    decoy_mask = (magic_seed >> 4) ^ 0xFF  # Unused path
    mask = (magic_seed & 0xFFFF) ^ 0x5A5A  # Core logic step 4

    # Decoy transformation tree (dead code path)
    def transform_x(x): return (x ^ 0xBEEF) & 0xFFFF
    def transform_y(x): return (x + 0xCAFE) ^ 0xDEAD
    def transform_z(x): return transform_y(transform_x(x))

    # Finalization function with lambda abstraction (core logic step 5)
    finalize = lambda x: ((x ^ mask) + scale_factor) & 0xFFFF

    # Critical execution point
    checksum = finalize(sum_filtered & mask)

    # Irrelevant telemetry output (distractor)
    telemetry = {'raw_count': len(raw_readings),
                 'filtered_count': len(filtered),
                 'decoy_hash': transform_z(checksum)}

    # Unused recursive trace (misleading complexity)
    def trace_depth(n):
        return 1 if n <= 1 else n + trace_depth(n - 2)

    # Only this matters
    print(f"Result: {checksum}")

    return checksum

# Input data (deterministic seed)
sensor_data = [88, 96, 92, 101, 87, 99, 103, 94, 110, 89, 107]

# Execute
analyze_sensor_stream(sensor_data)