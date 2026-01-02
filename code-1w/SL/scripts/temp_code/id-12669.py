def calculate_system_state():
    # Simulate sensor readings over time (in arbitrary units)
    raw_readings = [14, 18, 22, 19, 25, 30, 28, 24, 20, 17]
    
    # Irrelevant transformation: normalized values (not used in final result)
    max_reading = max(raw_readings)
    normalized = [round(x / max_reading, 3) for x in raw_readings]
    
    # Extract every second reading starting from index 1 (slice operation)
    sparse_samples = raw_readings[1::2]  # [18, 19, 30, 24, 17]
    
    # Base pressure derived from median of sparse samples
    sorted_samples = sorted(sparse_samples)
    n = len(sorted_samples)
    median_pressure = (sorted_samples[n//2] + sorted_samples[(n-1)//2]) / 2  # 19.0
    
    # Adjust base using modulo pattern from original sequence
    offset_sum = sum(r % 4 for r in raw_readings)  # 1+2+2+3+1+2+0+0+0+1 = 12
    adjusted_base = median_pressure + (offset_sum % 7)  # 19.0 + 5 = 24.0
    
    # Scale factor determined by set intersection logic
    expected_peaks = {20, 25, 30}
    actual_peaks = {x for x in raw_readings if x > 23}
    common_peaks = expected_peaks & actual_peaks  # {25, 30}
    scale_factor = len(common_peaks) * 2  # 2 * 2 = 4
    
    # Cumulative delta from pairwise differences in a sliced window
    window = raw_readings[2:7]  # [22, 19, 25, 30, 28] -> slice used
    deltas = []
    for i in range(len(window) - 1):
        deltas.append(abs(window[i+1] - window[i]))
    cumulative_delta = sum(d for d in deltas if d > 3)  # [3,6,5,2] -> 6+5=11
    
    # Dead code: unused statistical calculation
    mean_window = sum(window) / len(window)
    variance = sum((x - mean_window) ** 2 for x in window) / len(window)
    std_dev = variance ** 0.5
    
    # Final computation
    final_pressure = adjusted_base + (scale_factor * cumulative_delta)
    return final_pressure

result = calculate_system_state()
print(f"Result: {result}")