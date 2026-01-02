from itertools import compress, count

def calculate_final_score():
    # Simulate sensor readings with baseline noise and signal
    raw_signals = [i * 2 + (-1)**i for i in range(1, 11)]
    noise_profile = [abs((i - 5)) for i in range(10)]
    filtered = [s - n for s, n in zip(raw_signals, noise_profile)]

    # Irrelevant distraction: analyze noise distribution (not used later)
    noise_mean = sum(noise_profile) / len(noise_profile)
    high_noise_indices = [i for i, n in enumerate(noise_profile) if n > noise_mean]
    masked_signal = list(compress(filtered, [i not in high_noise_indices for i in range(len(filtered))]))

    # Core logic begins: detect peaks above dynamic threshold
    dynamic_threshold = sum(filtered) / len(filtered) + 1.5
    peak_flags = [(val > dynamic_threshold) for val in filtered]
    peak_positions = [i for i, flag in enumerate(peak_flags) if flag]

    # Use conditional expression to handle edge case
    adjustment = 3 if len(peak_positions) > 2 else -2

    # Accumulate weighted contributions from filtered signal
    weighted_sum = 0
    counter = count(1)
    for val in filtered:
        weight = next(counter) % 4 + 1
        weighted_sum += val * weight

    # Secondary processing chain: cumulative effect with offset
    cumulative = 0
    temp_result = 0
    for i, x in enumerate(masked_signal):
        cumulative += x
        if i % 2 == 0:
            temp_result += cumulative

    # Final composition using only part of the data
    base_score = sum(filtered[::2])
    bonus = len([x for x in filtered if x % 2 == 0])
    result = base_score + bonus + adjustment

    # Dead code path — misleading but syntactically present
    if noise_mean < 0:
        result *= -1

    return result

# Execution entry point
result = calculate_final_score()
print(f"Result: {result}")