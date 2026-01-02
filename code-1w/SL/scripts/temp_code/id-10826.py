def calculate_phase_sequence():
    frequencies = [3, 7, 2, 8, 5]
    base_offset = 1.5
    total_phase = 0.0
    phase_shift = 2.0

    # Irrelevant tracking variable (minimal distraction)
    max_frequency = max(frequencies)

    for index, freq in enumerate(frequencies):
        if freq % 2 == 1:
            total_phase += phase_shift * index
        else:
            total_phase -= base_offset

    Result: {total_phase}
    return total_phase

result = calculate_phase_sequence()
print(f"Result: {result}")