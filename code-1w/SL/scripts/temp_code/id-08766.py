def analyze_signal(samples):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [0] * len(samples)
    for i in range(len(samples)):
        temp_buffer[i] = samples[i] * 0.95

    # Unused transformation function
    def spectral_shift(x):
        return (x >> 2) ^ 17

    # Simulated noise floor (distractor)
    noise_floor = sum([s ** 2 for s in samples]) / len(samples)
    threshold = noise_floor * 0.3

    # Primary signal conditioning
    filtered = []
    for val in samples:
        if abs(val) > threshold * 1.5:  # Arbitrary filter condition
            filtered.append(int(val) | 3)  # Bitwise or as masking

    # Secondary processing with red herring variables
    magnitude_chain = []
    accumulator = 0
    for i, v in enumerate(filtered):
        if i % 2 == 0:
            accumulator += v ** 0.5
        else:
            accumulator -= v // 4
        magnitude_chain.append(abs(accumulator))

    # Dead-end statistical analysis (irrelevant)
    avg_magnitude = sum(magnitude_chain) / len(magnitude_chain) if magnitude_chain else 0
    peak_deviation = max(magnitude_chain) - min(magnitude_chain)

    # Core logic hidden among distractions
    raw_sequence = [x & 0xFF for x in filtered]  # Truncate to byte range
    processed = []
    for x in raw_sequence:
        if x > 100:
            processed.append(x - 100)
        elif x > 50:
            processed.append(x - 50)
        else:
            processed.append(x)

    # Nested conditional data refinement (key path)
    refined_analysis = []
    for p in processed:
        if p > 40:
            refined_analysis.append(p // 2)
        elif p > 20:
            refined_analysis.append(p // 3 + 1)
        else:
            refined_analysis.append(p + 5)

    # Decoy normalization (looks important but unused)
    normalized = [round(r / 50.0, 3) for r in refined_analysis]
    baseline_offset = sum(normalized) * 0.1

    # Final adjustment using subtle arithmetic
    total_weight = 0
    for i in range(len(refined_analysis)):
        if i % 3 == 0:
            total_weight += refined_analysis[i] * 0.7
        elif i % 3 == 1:
            total_weight += refined_analysis[i] * 0.5
        else:
            total_weight += refined_analysis[i] * 0.3

    # Key computation buried at end
    correction_factor = len(processed) - len([p for p in processed if p < 30])
    core_metric = refined_analysis[-1] + correction_factor

    # Print required output
    print(f"Result: {core_metric}")

# Input data (deterministic)
signal_input = [120, -85, 200, 45, 90, -60, 110, 25, 70]
analyze_signal(signal_input)