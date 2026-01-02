def calculate_efficiency(risk_levels):
    base_multiplier = 0.85
    penalties = [1.2 if level > 7 else 0.9 for level in risk_levels]
    adjusted = [base_multiplier * p for p in penalties]
    return round(sum(adjusted) * 100)

# Environmental monitoring system
risk_readings = (6, 8, 7, 9)
activation_threshold = 7
high_risk_count = len([r for r in risk_readings if r > activation_threshold])
energy_output = calculate_efficiency(risk_readings)
print(f"Result: {energy_output}")