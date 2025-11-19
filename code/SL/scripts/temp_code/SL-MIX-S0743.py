import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Truck capacities and package data
truck_capacities = [1500, 2000, 1800, 2200]
packages = [
    {'weight': 120, 'volume': 80},
    {'weight': 200, 'volume': 100},
    {'weight': 150, 'volume': 90},
    {'weight': 300, 'volume': 120},
    {'weight': 180, 'volume': 110},
    {'weight': 250, 'volume': 130},
    {'weight': 90, 'volume': 60},
    {'weight': 160, 'volume': 85}
]

# Calculate weight density for each package
for pkg in packages:
    pkg['density'] = pkg['weight'] / pkg['volume']

# Sort packages by density descending using sorted()
sorted_packages = sorted(packages, key=lambda x: x['density'], reverse=True)

# Greedy loading for each truck
loading_efficiencies = []
remaining_packages = sorted_packages[:]

for capacity in truck_capacities:
    loaded_weight = 0
    i = 0
    while i < len(remaining_packages):
        pkg = remaining_packages[i]
        if loaded_weight + pkg['weight'] <= capacity:
            loaded_weight += pkg['weight']
            remaining_packages.pop(i)
        else:
            i += 1
    efficiency = loaded_weight / capacity
    loading_efficiencies.append(efficiency)

# Compute coefficient of variation (CV)
if len(loading_efficiencies) > 0:
    mean_efficiency = sum(loading_efficiencies) / len(loading_efficiencies)
    variance = sum((x - mean_efficiency) ** 2 for x in loading_efficiencies) / len(loading_efficiencies)
    std_dev = math.sqrt(variance)
    cv_result = std_dev / mean_efficiency if mean_efficiency != 0 else 0
else:
    cv_result = 0

# Adjust result using number theory
prime_factors_lcm = lcm(12, 18)
adjusted_result = cv_result * prime_factors_lcm

print(f"Result: {adjusted_result}")