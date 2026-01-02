def calculate_performance(base, data):
    adjusted = [val - base for val in data if val > base]
    bonuses = len(adjusted) * 2
    penalty = sum(1 for val in data if val < base / 2)
    return bonuses - penalty

baseline = 50
data_sequence = [60, 45, 55, 40, 70, 30, 80]
readings = [x for x in data_sequence if x >= 30]

# Key computation step
temp_result = sum(readings) // len(readings)
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")