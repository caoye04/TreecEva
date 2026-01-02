from collections import defaultdict
from itertools import combinations

# Simulate sensor data trends over time intervals
temperature_trends = [0.4, -0.2, 0.8, -1.1, 0.3]
humidity_trends = [0.1, 0.3, -0.4, 0.2, -0.1]

# Irrelevant distractor: unused variable (minimal interference)
noise_floor = [0.05, 0.07, 0.03]

# Aggregate trend magnitudes above threshold
def calculate_stability(trends):
    significant = [t for t in trends if abs(t) > 0.3]
    return len(significant) * 2

# Compute combined index from multiple sources
combined_trends = []
for i in range(len(temperature_trends)):
    combined_trends.append(temperature_trends[i] + humidity_trends[i] * 0.5)

# Apply stability calculation on derived signal
pressure_index = calculate_stability(combined_trends)

# Output result as required
print(f"Result: {pressure_index}")