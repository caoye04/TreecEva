def calculate_phase_sequence():
    frequencies = [2, 3, 5, 7, 11]
    base_offset = 1.5
    total_phase = 0.0
    phase_shift = 0.5

    for index, freq in enumerate(frequencies):
        if freq % 2 == 1:
            total_phase += phase_shift * index
        else:
            total_phase -= base_offset

    Result: {total_phase}