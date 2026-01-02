def calculate_phase(a, b):
    magnitude = (a ** 2 + b ** 2) ** 0.5
    angle = (a + b) % 360
    return angle if magnitude > 0 else 0

signal_a = 17
signal_b = 23
phase_shift = calculate_phase(signal_a, signal_b)
print(f"Target result: {phase_shift}")