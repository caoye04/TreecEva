import math

# Baker's proprietary bread proofing parameters
base_proofing_factor = 2.5
humidity_coefficient = 0.7

# Calculate exponential growth component
exponential_component = math.exp(base_proofing_factor)

# Calculate logarithmic humidity adjustment
log_humidity_adjustment = math.log(humidity_coefficient * 10)

# Combine components to determine optimal temperature
optimal_proofing_temperature = exponential_component + log_humidity_adjustment

# Apply final adjustment using set operations on temperature ranges
standard_ranges = {30, 35, 40, 45}
premium_ranges = frozenset([32, 37, 42, 47])
intersection_ranges = standard_ranges & premium_ranges

# Apply adjustment based on intersecting ranges
if len(intersection_ranges) > 0:
    optimal_proofing_temperature += max(intersection_ranges) * 0.1

print(f"Result: {optimal_proofing_temperature}")