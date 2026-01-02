def compute_integrity_score():
    # Simulated sensor data processing with embedded integrity check
    raw_readings = [23, 45, 67, 89, 12, 34, 56, 78]
    
    # Irrelevant transformation: frequency modulation emulation (dead path)
    freq_mod = [x * 1.05 for x in raw_readings if x > 30]
    normalized = list(map(lambda x: round(x + 0.25), raw_readings))
    
    # Core signal filtering (partially relevant)
    filtered = [x for x in normalized if x % 2 == 0]
    accumulation = 0
    for val in raw_readings:
        accumulation += val * 2
        if accumulation > 200:
            accumulation -= 100  # artificial clamp

    # Dummy cryptographic hash attempt (distractor)
    secret_key = 0xDEADBEEF
    salted = accumulation ^ secret_key
    entropy_pool = (salted >> 16) & 0xFF

    # Data summarization (relevant)
    data_sum = sum(normalized) + (accumulation // 10)

    # Red herring: network latency simulation
    ping_samples = [120, 115, 130, 95, 140]
    avg_latency = sum(ping_samples) / len(ping_samples)
    jitter = max(ping_samples) - min(ping_samples)

    # Decoy calculation: packet loss estimation (irrelevant)
    expected_packets = 1000
    lost_packets = 12
    drop_rate = lost_packets / expected_packets

    # Spurious bit-twiddling (misleading intermediate)
    mask = 0
    for i in range(8):
        mask |= (1 << i)
    mask ^= 0xAA  # introduces alternating bit pattern

    # Core integrity computation — KEY EXECUTION POINT
    checksum = (data_sum ^ mask) & 0xFFFF

    # Unused alternate checksums (dead code paths)
    alt_checksum1 = (data_sum + mask) % 65537
    alt_checksum2 = (data_sum ^ (mask << 1)) & 0xFFFF

    # Fake validation logic
    is_valid = False
    threshold = 450
    if checksum > threshold and entropy_pool < 100:
        is_valid = True

    # Output final result
    print(f"Result: {checksum}")

compute_integrity_score()