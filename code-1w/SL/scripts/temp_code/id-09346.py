def compute_neural_activity(baseline, inputs):
    activation_levels = [(baseline + inp) ** 0.5 for inp in inputs]
    system_active = any(x > 7 for x in activation_levels)
    scaling_factor = 1.75 if len(inputs) > 3 else 1.2
    
    # Irrelevant diagnostic variable (minor distraction)
    diagnostic_code = "OK" if system_active else "IDLE"
    
    energy_threshold = max(activation_levels) * scaling_factor if system_active else 0
    
    return energy_threshold

# Input data
input_signals = [4.0, 6.2, 8.1, 5.3]
base_level = 2.0

result = compute_neural_activity(base_level, input_signals)
print(f"Target result: {result}")