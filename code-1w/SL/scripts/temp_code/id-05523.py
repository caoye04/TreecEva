def main():
    # Sensor data processing with noise filtering and integrity checks
    raw_samples = [127, 255, 64, 192, 32, 224, 16, 96]
    thresholds = {'low': 32, 'high': 192}
    scaling_factor = 0.75
    adjustment_offset = 5

    # Irrelevant transformation chain (distractor)
    temp_data = list(map(lambda x: (x + adjustment_offset) * scaling_factor, raw_samples))
    normalized = [int(x) for x in temp_data if x > 40]  # Partial use, misleading

    # Core logic: filter high-amplitude signals
    filtered = [x for x in raw_samples if x > thresholds['high']]

    # Secondary path: frequency pattern simulation (dead code path)
    def simulate_frequency(signal):
        return [signal[i] ^ signal[(i+1)%len(signal)] for i in range(len(signal))]
    
    freq_pattern = simulate_frequency(raw_samples)  # Computed but unused

    # Energy accumulation with bit manipulation
    energy_sum = 0
    for val in filtered:
        energy_sum += val >> 2  # Reduce by factor of 4 using bit shift

    # Masking sequence for transmission integrity (red herring variables)
    parity_track = 0
    for val in raw_samples:
        parity_track ^= val  # Overall XOR, looks important but not used in result

    metadata_flag = 0b101010
    mask = 0xFFFF & ~metadata_flag  # Effective mask used later

    sum_filtered = energy_sum << 3  # Amplify accumulated energy

    # Decoy checksum function
    def validate(arr):
        return sum(arr) % 256
    
    dummy_checksum = validate(normalized)  # Misleading intermediate result

    # Finalization via lambda (required language feature)
    finalize = lambda x: (x ^ 0xABCD) & 0xFFFF

    # Key statement
    checksum = finalize(sum_filtered & mask)

    # Spurious late-stage operation (distractor)
    if checksum < 30000:
        checksum |= 0x8000  # Not triggered due to prior logic

    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()