def sensor_diagnostic_protocol():
    raw_readings = [127, 255, 64, 192, 31, 88, 144, 201]
    calibration_key = {'offset': 12, 'gain': 0.75, 'noise_floor': 5}
    
    # Irrelevant signal smoothing (dead path)
    smoothed = []
    for i in range(len(raw_readings)):
        val = raw_readings[i] * 0.9 + (raw_readings[i-1] if i > 0 else 0) * 0.1
        smoothed.append(int(val))
    
    # Actual processing begins: filter out saturated sensors
    valid_range = (30, 200)
    filtered_data = [x for x in raw_readings if valid_range[0] <= x <= valid_range[1]]
    
    # Decoy checksum calculation (misleading)
    checksum = 0
    for b in raw_readings:
        checksum = (checksum + b) % 256
    checksum ^= 0xFF
    
    # Sensor health map (distraction with unused logic)
    health_flags = {}
    for idx, val in enumerate(raw_readings):
        if val < 40:
            health_flags[idx] = 'CRITICAL'
        elif val > 200:
            health_flags[idx] = 'SATURATED'
        else:
            health_flags[idx] = 'STABLE'
    
    # Real configuration: threshold per surviving sensor
    base_thresholds = {i: (v // 16) * 2 for i, v in enumerate(filtered_data)}
    
    # Red herring: bit rotation function never used
    def rotate_bits(n, bits=8):
        return ((n << 3) | (n >> (bits-3))) & ((1 << bits) - 1)
    
    # Create dynamic threshold map using enumerate and conditional expression
    threshold_map = {
        f'sensor_{i}': base_thresholds[i] + (10 if i % 2 == 0 else 5)
        for i in range(len(filtered_data))
    }
    
    # Phantom transformation (distractor list comprehension)
    inverted_pairs = [
        (filtered_data[i], filtered_data[-(i+1)]) 
        for i in range(len(filtered_data))
    ]
    xor_fused = [a ^ b for a, b in inverted_pairs]
    
    # Core diagnostic logic
    def process_readings(data, thresholds):
        result = 0
        for i, val in enumerate(data):
            key = f'sensor_{i}'
            if key in thresholds:
                # Apply bitwise mask based on threshold
                masked = val & (~thresholds[key])
                # Accumulate using modular arithmetic
                result += (masked * 3) % 97
        # Secondary transformation: add entropy from XOR chain
        entropy_seed = 0
        for x in xor_fused:
            entropy_seed ^= x
        result += entropy_seed % 23
        return result
    
    # Dummy machine state simulation (unused class)
    class MachineState:
        def __init__(self, code):
            self.code = code
            self.active = True if code > 0 else False
    
    status_nodes = [MachineState(code=i+10) for i in range(8)]
    
    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    print(f"Result: {final_diagnostic}")

sensor_diagnostic_protocol()