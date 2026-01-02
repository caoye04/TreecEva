def calculate_efficiency(rate, cost):
    return round((rate / (cost + 1)) * 100, 2)

# System performance data: (processing_rate, resource_cost)
systems_data = [(89, 12), (95, 14), (78, 10), (92, 13)]
analyzed_metrics = []

# Irrelevant baseline placeholder (minimal distraction)
default_baseline = 75.0

# Analyze each system using lambda and enumerate
for idx, (rate, cost) in enumerate(systems_data):
    efficiency = calculate_efficiency(rate, cost)
    adjusted_efficiency = efficiency * (0.95 + idx * 0.01)  # Slight index-based adjustment
    analyzed_metrics.append(adjusted_efficiency)

# Use zip to pair with dummy labels (no functional impact)
names = ['Alpha', 'Beta', 'Gamma', 'Delta']
labeled_metrics = list(zip(names, analyzed_metrics))

# Final aggregation step
final_analysis = max(analyzed_metrics)
peak_efficiency = final_analysis

print(f"Result: {peak_efficiency}")