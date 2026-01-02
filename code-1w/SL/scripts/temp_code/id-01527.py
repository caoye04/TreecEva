def calculate_performance(results):
    total = 0
    bonus = 0
    for i, (name, score) in enumerate(zip(['A', 'B', 'C', 'D'], results)):
        if score > 80:
            total += score
            if i % 2 == 0:
                bonus += 5
    return total + bonus

# Irrelevant auxiliary variable (minimal distraction)
baseline = [75, 82, 90, 60]

benchmark_results = [85, 78, 92, 88]
initial_total = sum(benchmark_results)

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")