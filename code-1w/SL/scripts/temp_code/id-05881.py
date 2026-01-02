def calculate_phase(data, limit):
    phase_shift = 0
    for i, (value, index) in enumerate(zip(data, range(len(data)))):
        if value > limit:
            phase_shift += (index ^ value) & 3
        else:
            phase_shift -= (index & value) | 1
    return phase_shift

signal_data = [5, 2, 8, 1, 9]
threshold = 4
temp_var_ignore = [x * 2 for x in signal_data]  # Irrelevant computation
phase_shift = calculate_phase(signal_data, threshold)
print(f"Result: {phase_shift}")