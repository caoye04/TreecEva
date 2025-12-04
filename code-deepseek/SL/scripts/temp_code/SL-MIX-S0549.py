base_value = 4
multiplier = 3
temp_calc = base_value * multiplier
threshold_check = temp_calc > 10
final_score = (lambda x, y: (x**2 + y**3) if x > y else (y**2 - x**3))(base_value, multiplier)
print(f"Result: {final_score}")