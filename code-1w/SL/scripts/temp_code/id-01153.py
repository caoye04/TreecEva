def analyze_data_stream(raw_packets, threshold_multiplier=1.75):
    import math

    # Simulated packet metadata (irrelevant fields included)
    packet_ids = [i for i in range(len(raw_packets))]  # Distractor: not used later
    timestamps = [t * 1.03 for t in range(len(raw_packets))]  # Dead data path

    # Core processing variables
    signal_strengths = []
    for pkt in raw_packets:
        base_val = sum(ord(c) for c in pkt) % 100
        adjusted = math.floor(base_val * threshold_multiplier)
        signal_strengths.append(adjusted)

    # Irrelevant transformation chain (red herring)
    def transform_noise(data):
        return [d ^ 7 for d in data]  # Unused function

    noise_floor = [s % 10 for s in signal_strengths]
    enhanced_noise = list(map(lambda x: (x + 5) ** 2, noise_floor))  # Computationally dead end

    # Begin relevant logic: filter strong signals
    strong_signals = [s for s in signal_strengths if s > 42]

    # Generate frequency map (partially relevant)
    freq_map = {}
    for val in strong_signals:
        freq_map[val] = freq_map.get(val, 0) + 1

    # Extract unique high-frequency values
    frequent_values = {k for k, v in freq_map.items() if v >= 2}  # Set operation (required feature)

    # Secondary filter based on bit properties (bit manipulation red herring)
    def has_sparse_bits(n):
        return bin(n).count('1') <= 3

    sparse_set = {x for x in strong_signals if has_sparse_bits(x)}  # Distractor set

    # Actual key logic: intersection with descending sort and truncation
    candidate_pool = frequent_values & set(strong_signals)  # Meaningful set intersection
    sorted_candidates = sorted(candidate_pool, reverse=True)  # Sorting (suggested paradigm)

    # Apply artificial cap (real constraint)
    capped_candidates = sorted_candidates[:3]

    # Decoy statistical computation
    avg_decoy = sum(enhanced_noise) / len(enhanced_noise) if enhanced_noise else 0  # Misleading float
    normalized_ghost = math.log(avg_decoy + 1) if avg_decoy > 0 else 0  # Dead calculation

    # Final selection via character entropy side-channel (distraction)
    entropy_shadow = 0
    for pkt in raw_packets:
        chars = set(pkt)
        entropy_shadow += len(chars) * 0.1

    # Critical assignment point
    optimal_set = set(capped_candidates)  # Transition to set for final logic
    filtration_score = len(optimal_set)

    # Final irrelevant print (never reached in reasoning)
    debug_trace = [f"{i}: {v}" for i, v in enumerate(sparse_set)]  # Unused trace

    return filtration_score

# Input generation (deterministic)
data_packets = [
    "sensor_01", "logger_A7", "sensor_02", "status_X",
    "sensor_01", "sensor_03", "logger_A7", "sensor_02",
    "sensor_04", "status_X", "sensor_03", "logger_A7"
]

result = analyze_data_stream(data_packets)
print(f"Result: {result}")