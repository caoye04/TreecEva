def calculate_performance(results):
    total = 0
    bonus = 10
    threshold = 85
    count_high = 0

    for score in results:
        if score >= threshold:
            count_high += 1
        total += score

    avg = total / len(results)
    extra = 5 if count_high >= 3 else 0
    final = avg + extra
    return final

# Irrelevant utility function (minimal distraction)
def format_report(value):
    return f'Performance: {value:.2f}%'

# Main data
benchmark_results = [88, 92, 76, 90, 85]
initial_total = sum(benchmark_results)  # Distractor: not used in logic
final_score = calculate_performance(benchmark_results)
print(f'Result: {final_score}')