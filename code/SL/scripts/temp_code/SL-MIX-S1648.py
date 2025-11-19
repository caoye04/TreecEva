from functools import reduce
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

def process_symbol(symbol_value, position):
    adjusted_value = symbol_value if symbol_value % 2 == 0 else symbol_value * 3 + 1
    return adjusted_value + position

def binary_search_closest(arr, target):
    low, high = 0, len(arr) - 1
    closest = arr[0]
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return arr[mid]
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return closest

# Encoded signal sequence
signal_sequence = [13, 7, 24, 19, 36, 8, 15]
processed_values = []
checksum_components = []

for idx, symbol in enumerate(signal_sequence):
    processed_val = process_symbol(symbol, idx)
    processed_values.append(processed_val)
    # Ternary operator to determine component inclusion
    component = processed_val if processed_val > 20 else (processed_val * 2 if processed_val > 10 else 0)
    if component > 0:
        checksum_components.append(component)

# Sort for binary search
processed_values.sort()
search_targets = [25, 30, 35]
search_results = [binary_search_closest(processed_values, t) for t in search_targets]

# Calculate LCM of search results
lcm_of_results = reduce(lcm, search_results, 1)

# Number theory: GCD of checksum components
component_gcd = reduce(gcd, checksum_components, 0) if checksum_components else 0

# Final checksum using ternary operator
checksum_result = lcm_of_results if component_gcd > 1 else sum(checksum_components)

print(f"Result: {checksum_result}")