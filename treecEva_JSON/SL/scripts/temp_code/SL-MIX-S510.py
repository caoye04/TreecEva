from collections import defaultdict
import math

def calculate_optimal_conversions(exchange_log):
    cumulative_gains = defaultdict(float)
    running_sum = 0.0
    peak_conversion_gain = -math.inf
    
    for idx, fluctuation in enumerate(exchange_log):
        running_sum += fluctuation
        if running_sum > 0:
            cumulative_gains[idx] = round(running_sum, 4)
            if cumulative_gains[idx] > peak_conversion_gain:
                peak_conversion_gain = cumulative_gains[idx]
        else:
            running_sum = 0.0
    
    return peak_conversion_gain

# Simulated exchange rate fluctuations over 12 periods
fluctuations = [0.02, -0.01, 0.03, 0.05, -0.08, 0.04, 0.01, -0.02, 0.06, 0.03, -0.04, 0.02]
peak_conversion_gain = calculate_optimal_conversions(fluctuations)
print(f"Result: {peak_conversion_gain}")