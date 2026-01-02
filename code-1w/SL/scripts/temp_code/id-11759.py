def calculate_performance(data):
    base_scores = [x * 0.8 for x, _ in enumerate(data, start=1)]
    weights = [1.2, 0.9, 1.1, 0.8, 1.0]
    adjusted = [score * weights[i] for i, score in enumerate(base_scores) if i < len(weights)]
    
    # Irrelevant distraction: unused variable
    temp_analysis = sum([x ** 0.5 for x in data if x > 5])
    
    total = sum(adjusted)
    bonus = 2.5 if len(data) >= 4 else 0
    final_score = total + bonus
    return final_score

# Main execution
data_set = [3, 7, 4, 9, 2]
run_mode = "diagnostic"
benchmark_data = [x + 1 for x in data_set]
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")