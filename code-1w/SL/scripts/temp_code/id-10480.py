def calculate_phase(data, limit):
    filtered = [x for x in data if abs(x) > limit]
    indices = [i for i, _ in enumerate(filtered)]
    products = [a * b for a, b in zip(filtered, indices)]
    return sum(products) // len(products) if products else 0

signal_data = [1, -3, 5, -2, 8, -7, 0, 4]
baseline = 2.5
threshold = int(baseline)

# Irrelevant auxiliary variable (minimal distraction)
counter_weights = [1, 1, 1, 1]

phase_shift = calculate_phase(signal_data, threshold)
print(f"Target result: {phase_shift}")