def adjust_humidity(bases, adjustments):
    total_humidity_index = 0
    for i, (base, adj) in enumerate(zip(bases, adjustments)):
        if i % 2 == 0:
            total_humidity_index += base * adj
        else:
            total_humidity_index += base + adj
    return total_humidity_index

# Environmental sensor calibration data
base_values = [12, 15, 10, 8]
corrections = [1.5, 2, 0.8, 3]

# Irrelevant auxiliary variable (minimal distraction)
baseline_offset = 0.5

# Compute final index
total_humidity_index = adjust_humidity(base_values, corrections)
print(f"Result: {total_humidity_index}")