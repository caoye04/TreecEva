def calculate_performance(base, data):
    adjusted = [abs(float(x.strip('%')) - base) for x in data]
    correction_factor = sum(adjusted) / len(adjusted)
    if correction_factor > base:
        result = base * 0.75
    else:
        result = base + correction_factor
    return round(result, 3)

baseline = 8.5
readings = ['9.2%', '7.8%', '8.9%', '8.0%', '7.5%']
extra_data = ['temp', 'log', 'meta']
version = 'v2.1'
final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")