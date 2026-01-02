def calculate_performance(results):
    total = 0
    bonus = 10  # Irrelevant distractor
    for i, (success, cycles) in enumerate(zip(results['outcomes'], results['latency'])):
        if success and cycles < 100:
            total += 1
        elif not success and cycles >= 200:
            total -= 1
    return total * (i + 1)

# Simulated benchmark data
dummy_var = [1, 2, 3]  # Distractor variable
benchmark_results = {
    'outcomes': [True, False, True, True, False],
    'latency': [80, 150, 120, 90, 250]
}

initial_score = 0  # Unused variable (minor interference)
final_score = calculate_performance(benchmark_results)
print(f"Target result: {final_score}")