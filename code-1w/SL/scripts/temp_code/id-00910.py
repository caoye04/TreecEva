def analyze_sensor_data():
    # Simulated sensor readings with calibration offsets
    raw_readings = [1024, 2048, 512, 4096, 3072, 1536]
    calibration_factor = 0.98
    temperature_bias = 23.5
    pressure_adjustment = 1.02

    # Irrelevant transformation: convert to string and back (distractor)
    str_values = [str(val) for val in raw_readings]
    parsed_back = [int(s.lstrip('0')) if s.startswith('0') else int(s) for s in str_values]

    # Real data processing begins
    filtered_data = [x for x in raw_readings if x > 1000]  # Only high-amplitude signals
    scaled_data = [int(x * calibration_factor) for x in filtered_data]

    # Decoy checksum using pressure (misleading path)
    decoy_sum = sum(scaled_data) * pressure_adjustment
    temp_checksum = int(decoy_sum) & 0xFFFF

    # Unused recursive function (dead code path)
    def recurse_nonsense(n):
        if n <= 1:
            return 1
        return n * recurse_nonsense(n - 2)

    # Another red herring: sorting and reversing for no reason
    sorted_scaled = sorted(scaled_data)
    reversed_scaled = sorted_scaled[::-1]
    shuffled_result = [reversed_scaled[i] + i*2 for i in range(len(reversed_scaled))]

    # Key computation chain starts here
    data_sum = sum(scaled_data)  # Core value
    
    # Complex adjustment derived from temperature and length
    base_adjustment = int(temperature_bias * 10)
    length_factor = len(filtered_data)
    adjustment = (base_adjustment << 2) | length_factor  # Bitwise mix

    # This is the critical line — answer depends on this
    checksum = (data_sum ^ adjustment) % 97

    # Final obfuscation: print unrelated intermediate
    debug_info = f"TempChecksum:{temp_checksum},Size:{len(shuffled_result)}"
    metadata_hash = sum([ord(c) % 7 for c in debug_info])

    # Output the actual target result
    print(f"Result: {checksum}")

analyze_sensor_data()