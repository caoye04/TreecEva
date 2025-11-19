import math
import statistics

def execution_timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@execution_timer
def generate_fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

@execution_timer
def compute_variance_ratios(data):
    if len(data) < 2:
        return 0
    return statistics.variance(data) / (statistics.mean(data) or 1)

# Signal processing parameters
transmission_rates = [10, 15, 20, 25, 30]
fibonacci_length = 8

# Generate Fibonacci sequence for optimization
optimization_sequence = generate_fibonacci(fibonacci_length)

# Calculate statistical measures
variance_ratio = compute_variance_ratios(optimization_sequence)
mean_rate = statistics.mean(transmission_rates)

# Compute weighted efficiency score
raw_efficiency = (variance_ratio * mean_rate) if mean_rate > 0 else 0
normalized_efficiency = raw_efficiency / len(optimization_sequence) if len(optimization_sequence) > 0 else 0

# Apply conditional adjustments based on sequence analysis
final_efficiency_rating = normalized_efficiency if normalized_efficiency > 10 else normalized_efficiency * 2

# Additional adjustment based on transmission rate analysis
rate_deviation = statistics.stdev(transmission_rates)
final_efficiency_rating = final_efficiency_rating + (rate_deviation if rate_deviation > 5 else 0)

print(f"Result: {round(final_efficiency_rating, 2)}")