def calculate_harmony(pairs):
    harmony_score = 0
    weight_factor = 1.5

    # Irrelevant distraction: unused variable
    baseline_offset = 0.25

    for index, (freq_a, freq_b) in enumerate(pairs):
        ratio = freq_b / freq_a
        # Using lambda to compute weighted logarithmic interval
        log_interval = (lambda x: weight_factor * (x - 1) ** 2)(ratio)
        harmony_score += log_interval
    
    return int(harmony_score + 0.5)  # Round to nearest integer

# Real data: musical frequency pairs in just intonation
frequency_pairs = [(261.63, 392.00), (329.63, 493.88), (196.00, 293.66)]

# Unused but plausible distraction
amplitude_data = [0.8, 0.6, 0.9]

# Key computation
total_harmony = calculate_harmony(frequency_pairs)

print(f"Result: {total_harmony}")