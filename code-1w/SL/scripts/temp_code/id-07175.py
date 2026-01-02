def collect_diagnostics():
    # Simulated sensor data with noise and redundant metrics
    raw_readings = [127, 255, 193, 64, 128, 96, 224, 31, 7, 48, 112, 240]
    calibration_map = {i: (i * 1.05) for i in range(256)}
    processed = [int(calibration_map[x]) for x in raw_readings if x > 50]

    # Irrelevant transformation: color space conversion (distractor)
    rgb_values = [(x >> 5, (x >> 2) & 0x07, x & 0x03) for x in raw_readings]
    luminance = [0.299*r + 0.587*g + 0.114*b for r, g, b in rgb_values]

    # Real signal filtering begins here
    valid_range = set(range(100, 256))
    filtered_data = [x for x in processed if x in valid_range]

    # Decoy statistical analysis (dead path)
    mean_val = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    variance = sum((x - mean_val)**2 for x in filtered_data) / len(filtered_data) if filtered_data else 0
    outlier_threshold = mean_val + 1.5 * (variance ** 0.5)

    # Actual logic uses bit patterns and thresholds
    def bit_population(n):
        return bin(n).count('1')

    population_scores = [bit_population(x) for x in filtered_data]
    high_density = {i for i, s in enumerate(population_scores) if s >= 5}

    # Threshold set based on prime-aligned values (key concept)
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True

    prime_offsets = {x for x in range(50, 100) if is_prime(x)}
    base_shift = sum(1 for x in population_scores if x % 2 == 0)
    threshold_set = {p + base_shift for p in prime_offsets}

    # Red herring: unused recursive smoothing
    def smooth_sequence(seq, depth=2):
        if depth == 0 or len(seq) < 3:
            return seq
        new_seq = [seq[0]]
        for i in range(1, len(seq)-1):
            new_seq.append((seq[i-1] + seq[i] + seq[i+1]) // 3)
        new_seq.append(seq[-1])
        return smooth_sequence(new_seq, depth-1)

    # Core diagnostic logic (non-obvious due to distractions)
    def analyze_readings(data, thresholds):
        accumulated = 0
        for val in data:
            matched = any(abs(val - t) < 10 for t in thresholds)
            parity_bit = bin(val).count('1') % 2
            if matched:
                if parity_bit == 1:
                    accumulated += val // 4
                else:
                    accumulated -= val % 15
        return accumulated + len(data)

    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused complex structure (distractor)
    class DataNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    return final_diagnostic

# Execute function
collect_diagnostics()