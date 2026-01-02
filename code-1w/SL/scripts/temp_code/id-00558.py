import math

# System reliability simulation: calculate combined entropy of component failure probabilities
def calculate_component_entropy(prob):
    if prob <= 0 or prob >= 1:
        return 0
    return -prob * math.log2(prob)

failure_rates = [0.1, 0.2, 0.05, 0.3, 0.15]

# Calculate individual entropies using list comprehension
temp_values = [x * 100 for x in failure_rates]  # Irrelevant scaling (distractor)
entropies = [calculate_component_entropy(p) for p in failure_rates]

total_entropy = sum(entropies)

# Additional unrelated computation (minor interference)
max_rate = max(failure_rates)
normalized = [r / max_rate for r in failure_rates]

print(f"Result: {total_entropy}")