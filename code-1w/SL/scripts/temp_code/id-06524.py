def calculate_score(data):
    avg = sum(data) / len(data)
    deviation = [abs(x - avg) for x in data]
    filtered = [x for x in deviation if x > 1.5]
    score = sum(filtered) * (0.9 if len(filtered) > 2 else 1.0)
    return round(score, 3)

# Irrelevant auxiliary variable (minimal distraction)
baseline = [20.1, 19.8, 21.0, 20.5, 19.9]

temperature_data = [2.3, 4.1, 6.7, 1.9, 5.2, 3.8]
result = calculate_score(temperature_data)
print(f"Result: {result}")