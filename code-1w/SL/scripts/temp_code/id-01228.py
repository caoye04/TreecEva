def calculate_threshold(signals, importance):
    base = len(signals & {x for x in range(10, 20)})
    modifier = sum(map(lambda x: x[0] ^ x[1], zip(importance, importance[1:])))
    adjustment = 0
    if base > 3:
        adjustment += 8
    else:
        adjustment -= 2
    
    # Irrelevant tracking variables (minimal distraction)
    log_entry_count = 0
    temp_buffer = []

    return base * modifier + adjustment

# Signal processing simulation
weights = [5, 3, 1, 7, 4]
signal_set = {8, 12, 14, 16, 18, 22}

# Extra unused variable (low interference)
baseline_reference = 0.75

activation_score = calculate_threshold(signal_set, weights)
print(f"Target result: {activation_score}")