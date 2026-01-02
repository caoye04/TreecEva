def analyze_harmonic_sequence():
    frequencies = [2, 4, 8, 16, 32]
    damping = [0.5, 0.25, 0.125, 0.0625, 0.03125]
    total_harmonic = 0
    temp_sum = 0

    for index, (freq, damp) in enumerate(zip(frequencies, damping)):
        ratio = freq * damp
        if ratio > 1.0:
            temp_sum += ratio
        total_harmonic += ratio * index

    adjustment = sum(damping)
    total_harmonic -= adjustment

    return total_harmonic

result = analyze_harmonic_sequence()
print(f"Result: {result}")