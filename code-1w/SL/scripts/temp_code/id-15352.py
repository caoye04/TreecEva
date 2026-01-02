def calculate_final_score(values, deductions):
    adjusted = [v * 0.9 for v in values]
    total = sum(adjusted)
    penalty_sum = sum(map(lambda x: x ** 0.5, deductions))
    final_reduction = penalty_sum * 2
    result = total - final_reduction
    return result

# Simulate sensor readings and calibration penalties
temperature_readings = [72, 68, 75, 80, 65]
calibration_errors = [4, 9, 16]

result = calculate_final_score(temperature_readings, calibration_errors)
print(f"Result: {result}")