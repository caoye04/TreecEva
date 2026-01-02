import itertools

# Simulated sensor data processing with noise filtering and checksum generation
def process_sensor_readings(raw_data, threshold=0.5, noise_floor=0.1):
    filtered = []
    cumulative_power = 0
    temp_buffer = []
    
    for val in raw_data:
        adjusted = abs(val - noise_floor)
        if adjusted > threshold:
            filtered.append(adjusted)
            cumulative_power += adjusted ** 2
            
    # Irrelevant signal smoothing path (dead code due to condition)
    smoothing_factor = 0.8
    if len(filtered) > 100:
        temp_buffer = [filtered[0]]
        for i in range(1, len(filtered)):
            temp_buffer.append(smoothing_factor * temp_buffer[-1] + (1 - smoothing_factor) * filtered[i])
    
    # Real processing: normalize and prepare for bit analysis
    if cumulative_power == 0:
        normalized = [1.0 for _ in filtered]
    else:
        normalized = [x / (cumulative_power ** 0.5) for x in filtered]
    
    # Bit feature extraction
    bit_features = []
    for num in normalized:
        as_int = int(num * 1000) & 0xFF
        popcount = bin(as_int).count('1')
        parity = popcount % 2
        bit_features.append((as_int, parity))
    
    # Decoy entropy calculation (unused later)
    entropy = 0
    counts = {i: 0 for i in range(256)}
    for b, _ in bit_features:
        counts[b] += 1
    for count in counts.values():
        if count > 0:
            p = count / len(bit_features)
            entropy -= p * __import__('math').log2(p)
    
    # Core logic begins: group every 3 valid features using itertools
    grouped = list(itertools.batched(bit_features, 3))
    
    # Misleading transformation chain
    transformed = []
    shift_register = 0xABC
    for group in grouped:
        if len(group) == 3:
            key_val = (group[0][0] << 4) ^ (group[1][0] >> 4) ^ group[2][0]
            shifted = (key_val ^ shift_register) & 0xFFFF
            transformed.append(shifted)
            shift_register = (shift_register >> 1) | (shift_register << 15)  # rolling

    # Unused FFT-like simulation
    freq_domain = []
    for i in range(len(transformed)):
        comp = 0
        for j in range(len(transformed)):
            angle = 2 * __import__('math').pi * i * j / len(transformed)
            comp += transformed[j] * __import__('cmath').exp(-1j * angle)
        freq_domain.append(comp)

    # Final processing stage with critical assignment
    base_value = 0
    for idx, t in enumerate(transformed):
        if t % 2 == 1:  # only odd transformed values contribute
            base_value += t % 100
    
    # Key computation with distractors around
    index_map = {i: v for i, v in enumerate(transformed)}
    scale_factor = len([x for x in normalized if x > 0.5])
    scaled_index = (scale_factor * 7) % 256
    correction_factor = bin(scaled_index).count('1') * 13
    
    # CRITICAL STATEMENT: this is where the target variable is set
    checksum = (base_value ^ scaled_index) + correction_factor
    
    # Red herring: alternate checksum that is never used
    alt_checksum = 0
    for c in str(checksum):
        alt_checksum = alt_checksum * 10 + (int(c) + 1) % 10
    
    # Final output
    print(f"Result: {checksum}")

# Simulated input
if __name__ == "__main__":
    sensor_data = [
        0.12, 0.15, 0.88, 0.91, 0.33, 0.76, 0.89, 0.92, 0.41, 0.14,
        0.87, 0.22, 0.90, 0.95, 0.67, 0.71, 0.85, 0.93, 0.55, 0.56,
        0.82, 0.84, 0.77, 0.69, 0.73, 0.81, 0.94, 0.68, 0.70, 0.74
    ]
    process_sensor_readings(sensor_data)