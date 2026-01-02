def calculate_performance(stability, throughput):
    base_metric = (stability + throughput) / 2
    adjust = lambda x: x * 1.5 if x > 75 else x * 0.8
    return adjust(base_metric)

# System diagnostics data
reliability = 80
efficiency = 70

# Irrelevant telemetry (minimal distraction)
cpu_temp = 68
disk_usage = 0.45

# Key computation
final_score = calculate_performance(reliability, efficiency)
print(f"Result: {final_score}")