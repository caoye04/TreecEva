def fibonacci_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

# Generate first 12 Fibonacci weights
package_weights = fibonacci_sequence(12)
truck_capacity = 144

# Dynamic programming setup
max_weight = 0
loaded_weights = []

# Greedy selection within DP constraints
for weight in sorted(package_weights, reverse=True):
    if max_weight + weight <= truck_capacity:
        max_weight += weight
        loaded_weights.append(weight)

# Calculate mean of loaded weights for secondary optimization check
import statistics
mean_loaded_weight = statistics.mean(loaded_weights) if loaded_weights else 0

# Final adjustment using stack to simulate last-in-first-out reevaluation
stack = loaded_weights[::-1]
while stack:
    top = stack.pop()
    if max_weight > truck_capacity:
        max_weight -= top
    else:
        break

print(f"Result: {max_weight}")