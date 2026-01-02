def analyze_temperatures(raw_data, threshold=25.0):
    """ Analyze temperature readings and extract anomalies """
    filtered = [t for t in raw_data if t > threshold]
    deviations = [(t - threshold) ** 2 for t in filtered]
    total_deviation = sum(deviations)
    count = len(filtered)
    
    # Irrelevant computation path - red herring
    baseline_avg = sum(raw_data) / len(raw_data) if raw_data else 0
    adjusted_scores = list(map(lambda x: x * 0.9 + 2.5, raw_data))
    aggregate_score = sum(adjusted_scores) % 1000

    # Unused transformation chain
    shadow_buffer = raw_data[::2]  # Every other reading
    inverted = [-x for x in shadow_buffer[::-1]]
    dummy_sum = sum(inverted) // (len(inverted) or 1)

    # Distractor: complex-looking but unused bitwise cascade
    key = 0xABC
    for val in raw_data:
        if val > 30:
            key ^= int(val) & 0xFF
            key = (key << 1) | (key >> 7)
            key &= 0xFFFF

    # Real processing begins here — non-obvious due to noise
    def classify(temp):
        return 'HIGH' if temp > threshold + 5 else 'ELEVATED'

    categories = [classify(t) for t in filtered]
    grouped = {cat: categories.count(cat) for cat in set(categories)}

    # Another decoy function — looks important but unused
    def compute_entropy(data):
        from math import log
        freqs = {}
        for d in data:
            freqs[d] = freqs.get(d, 0) + 1
        return -sum((f / len(data)) * log(f / len(data)) for f in freqs.values())

    # Actual relevant logic embedded in noise
    sum_filtered = sum(t for t in filtered if t < 35.0)
    
    # Control sequence derived from data shape — used later
    control_sequence = [
        len(raw_data) % 7,
        len(filtered) % 5,
        grouped.get('HIGH', 0) % 3
    ]

    # Dead code path — never executed but looks like it might be
    if False:
        fallback = (sum_filtered * 2) ^ 0x1234
        return fallback

    # Critical function using lambda and slicing
    finalize = lambda x, seq: (x + seq[0] * 1000) ^ (seq[1] * 100) ^ (seq[2] * 10)
    
    # Key assignment — answer depends on this
    checksum = finalize(sum_filtered, control_sequence)
    
    # Print required result
    print(f"Target result: {checksum}")
    
    # Return unused values to add confusion
    return {
        'main_checksum': checksum,
        'aggregate': aggregate_score,
        'dummy': dummy_sum,
        'key_snapshot': key
    }

# Simulate sensor data — deterministic seed
import random
random.seed(42)
data_stream = [22.1, 26.3, 24.8, 29.5, 31.0, 23.7, 27.4, 33.2, 25.9, 28.1, 30.6]

# Execute main logic
result_dict = analyze_temperatures(data_stream)