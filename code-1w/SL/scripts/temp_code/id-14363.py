def calculate_performance(data):
    normalize = lambda x: (x - min(data)) / (max(data) - min(data)) if max(data) != min(data) else 0
    normalized = [normalize(x) for x in data]
    avg_normalized = sum(normalized) / len(normalized)
    threshold = 0.5
    above_threshold = [val for val in normalized if val >= threshold]
    performance_bonus = len(above_threshold) * 0.1
    return round(avg_normalized + performance_bonus, 3)

# Irrelevant auxiliary variable (minimal distraction)
startup_phase = True

benchmark_data = [23, 45, 31, 57, 41, 55, 39]
initial_weight = 1.0  # Unused in final computation

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")