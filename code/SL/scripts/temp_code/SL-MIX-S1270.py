import math

# Initialize simulation parameters
zones = 3
iterations = 5
base_temp = 20.0

# Dictionary comprehension for zone factors
zone_modifiers = {f'zone_{i}': 1.0 + i * 0.1 for i in range(zones)}

# Nested loop for simulation
aggregated_impact_score = 0.0
for iteration in range(iterations):
    for zone_id, modifier in zone_modifiers.items():
        # Floating point operations with trigonometric and exponential functions
        temp_adjustment = math.sin(iteration * 0.5) * math.exp(-iteration * 0.1) * modifier
        aggregated_impact_score += temp_adjustment

print(f"Result: {round(aggregated_impact_score, 6)}")