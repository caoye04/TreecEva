import math

# Simulated sensor data from a distributed environmental monitoring system
def generate_sensor_readings():
    base_values = [23.4, 19.8, 20.1, 25.5, 18.9, 22.0, 24.3]
    noise = [0.1 * math.sin(i) for i in range(7)]
    return [round(base_values[i] + noise[i], 2) for i in range(7)]

# Irrelevant helper: calculates dew point (not used in final result)
def calculate_dew_point(temp, humidity=60):
    return round(temp - ((100 - humidity) / 5), 2)

# Misleading transformation chain
def transform_readings(raw):
    shifted = [x + 5 for x in raw]
    scaled = [x * 1.1 for x in shifted]
    inverted = [100 - x for x in scaled]
    # Dead end: this list is never used
    normalized = [round((x - min(inverted)) / (max(inverted) - min(inverted)), 3) for x in inverted]
    return inverted

# Bit manipulation red herring
def flag_encoder(n):
    if n < 20:
        return n ^ 0b1010
    elif n < 25:
        return (n << 1) & 0b1111
    else:
        return (n >> 1) | 0b1100

# Unused diagnostic path
def legacy_diagnostic(seq):
    accum = 0
    for val in seq:
        accum = (accum + int(val)) % 97
    return accum * 2

# Core processing with embedded distractors
def sensor_array_processor(readings):
    # Step 1: Apply irrelevant bit flags to each reading (distractor)
    flagged = [flag_encoder(int(x)) for x in readings]
    
    # Step 2: Compute multiple parallel metrics (only one matters)
    avg_temp = sum(readings) / len(readings)
    temp_variance = sum((x - avg_temp) ** 2 for x in readings) / len(readings)
    median_temp = sorted(readings)[len(readings)//2]
    
    # Step 3: Create tuple-based metadata (partially relevant)
    meta_cluster = (round(avg_temp, 1), len(readings), 'STABLE')
    
    # Step 4: Spurious string manipulation (distraction)
    status_code = ''.join([chr(97 + int(x) % 26) for x in readings[:3]])
    health_flag = status_code.upper() if 'a' in status_code else 'UNKNOWN'
    
    # Step 5: Real computation hidden among others
    # Critical: only this line contributes to final answer
    critical_factor = sum(int(x) for x in readings if x > 20.0)
    
    # Step 6: Fake aggregation pipeline
    aggregator = lambda x, y: x + y * 0.5
    fake_aggregate = 0
    for val in readings:
        fake_aggregate = aggregator(fake_aggregate, val)
    
    # Step 7: Tuple unpacking distraction
    base, count, state = meta_cluster
    adjusted_base = base * (count / 10) if state == 'STABLE' else base * 1.2
    
    # Step 8: Final computation - only critical_factor is used
    final_diagnostic = critical_factor * 3  # Key transformation
    
    # Red herring print (never executed)
    # print(f'Debug: {adjusted_base}, {health_flag}, {fake_aggregate}')
    
    return final_diagnostic

# Orchestration with decoy function calls
if __name__ == '__main__':
    raw_data = generate_sensor_readings()
    processed = transform_readings(raw_data)  # Result discarded
    legacy_score = legacy_diagnostic(raw_data)  # Computed but unused
    
    # Actual key execution point
    final_diagnostic = sensor_array_processor(raw_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")