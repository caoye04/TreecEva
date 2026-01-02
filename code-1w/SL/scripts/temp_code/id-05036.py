def calculate_performance(base, data):
    adjusted = [base * (1 + x / 100) for x in data if x > -10]
    valid_count = len(adjusted)
    avg_adjustment = sum(adjusted) / valid_count if valid_count > 0 else 0
    return round(avg_adjustment - base)

baseline = 50.0
readings = [12, -5, 20, -15, 8, -8]

# Filtering logic retains only values > -10: [12, -5, 20, 8, -8]
# Adjusted values: [50*(1+12/100)=56.0, 50*0.95=47.5, 60.0, 54.0, 46.0]
# Average of [56.0, 47.5, 60.0, 54.0, 46.0] = 52.7
# Final score = round(52.7 - 50.0) = round(2.7) = 3

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")