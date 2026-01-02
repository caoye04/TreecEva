def calculate_final_score(data, limits):
    exceeded = [val for val in data if any(val > limit for limit in limits)]
    adjustment = sum(exceeded) // len(exceeded) if exceeded else 0
    base = len(data) > len(limits)
    score = adjustment + (10 if base else 5)
    result = score * 2 - len(limits)
    return result

# Sensor readings in degrees Celsius
temperatures = [23, 45, 12, 67, 34]
thresholds = [30, 50]

# Irrelevant auxiliary variable (minimal distraction)
status_flags = (True, False, True)

result = calculate_final_score(temperatures, thresholds)
print(f"Target result: {result}")