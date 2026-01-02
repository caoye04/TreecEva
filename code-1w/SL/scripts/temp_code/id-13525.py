import itertools

# Simulated sensor data processing with noise filtering and checksum calculation
def main():
    raw_signal = [183, 24, 72, 91, 15, 66, 22, 88, 37, 50, 104, 33]
    baseline = 20
    threshold = 70
    scale_factor = 1.75
    offset = 3

    # Irrelevant transformation: frequency analysis (dead path)
    frequencies = {i: raw_signal.count(i) for i in set(raw_signal)}
    dominant_freq = max(frequencies, key=frequencies.get)

    # Real signal conditioning
    filtered = [x for x in raw_signal if x > baseline]
    scaled = [(x * scale_factor) + offset for x in filtered]
    rounded = [int(x) for x in scaled]  # Convert to integers

    # Decoy checksum using sum (misleading)
    decoy_checksum = sum(rounded) % 97

    # Mask generation with bit manipulation (relevant)
    prime_mask = 0
    for i in range(8):
        if (i * 5 + 3) % 7 < 5:
            prime_mask |= (1 << i)

    # Unused recursive function (red herring)
    def recursive_transform(n, depth=0):
        if depth >= 3 or n <= 1:
            return n
        return recursive_transform(n // 2, depth + 1) + recursive_transform(n // 3, depth + 1)

    # Linear search for first outlier (distraction)
    first_outlier = -1
    for i, val in enumerate(rounded):
        if val > threshold * scale_factor:
            first_outlier = i
            break

    # Core processing segment (key section)
    segment_a = rounded[2:7]
    segment_b = list(itertools.accumulate(segment_a, lambda a, b: (a + b) & 0xFF))
    segment_c = [x ^ (x >> 1) for x in segment_b]  # Bitwise diffusion

    # Actual checksum calculation function (closure with lambda)
    def process_segment(data, mask):
        temp = 0
        for i, val in enumerate(data):
            rotated = ((val << (i % 5)) | (val >> (8 - (i % 5)))) & 0xFF
            masked_val = rotated ^ mask
            temp ^= (masked_val * (i + 1))
        return temp % 10000

    # Spurious statistical computation (distractor)
    mean_val = sum(rounded) / len(rounded)
    variance = sum((x - mean_val) ** 2 for x in rounded) / len(rounded)
    entropy_proxy = -(sum((f / len(raw_signal)) * ((f / len(raw_signal))).__log__ for f in frequencies.values()) if frequencies else 0)

    # Unused XOR chain (dead code)
    accumulator = 0
    for x in raw_signal:
        accumulator ^= x ^ 0xAA

    # Key execution point
    checksum = process_segment(segment_c, prime_mask)

    # Print final result as required
    print(f"Result: {checksum}")

    # Additional red herring: unused tuple unpacking
    config = (baseline, threshold, 0xDEADBEEF)
    base_config, _, _ = config

    return checksum

if __name__ == "__main__":
    main()