def calculate_performance(data):
    total = 0
    adjustments = {'latency': 0.95, 'throughput': 1.05, 'error_rate': 0.85}
    for key, value in data.items():
        if key in adjustments:
            total += value * adjustments[key]
    return round(total, 3)

# Irrelevant auxiliary data (mild distraction)
config_params = {"version": "2.1", "mode": "production", "debug": False}
temp_log = [f"Entry_{i}" for i in range(3)]

benchmark_data = {
    'latency': 420,
    'throughput': 380,
    'error_rate': 50,
    'retries': 15  # Not used in calculation
}

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")