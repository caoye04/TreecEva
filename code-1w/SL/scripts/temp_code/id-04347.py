def calculate_performance(base, data):
    adjustment = 0
    total = base * 0.8
    for val in data:
        if not str(val).isdigit():
            continue
        adjusted_val = int(val) - base
        if adjusted_val > 0:
            adjustment += adjusted_val * 0.5
        else:
            adjustment -= abs(adjusted_val) * 0.2
    composite = total + adjustment
    return int(composite) if composite > 0 else 0

baseline = 50
inputs = ['55', '48', 'invalid', '60', '40']
initial_calc = baseline + len(inputs)
comment = "Processing complete."
final_score = calculate_performance(baseline, inputs)
print(f"Result: {final_score}")