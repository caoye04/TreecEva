import math

def gcd_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])
        if result == 1:
            break
    return result

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def calculate_combinations(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Package data: (weight, priority)
packages = [
    (10, 25),
    (15, 30),
    (8, 20),
    (12, 35),
    (20, 40),
    (5, 15),
    (18, 45)
]

truck_capacity = 50

# Step 1: Calculate priority-to-weight ratios and sort packages
package_ratios = [(priority/weight, i, weight, priority) for i, (weight, priority) in enumerate(packages)]
package_ratios.sort(reverse=True)

# Step 2: Greedy selection of packages
loaded_weights = []
loaded_indices = []
loaded_priorities = []
current_weight = 0

for ratio, idx, weight, priority in package_ratios:
    if current_weight + weight <= truck_capacity:
        current_weight += weight
        loaded_weights.append(weight)
        loaded_indices.append(idx)
        loaded_priorities.append(priority)

# Step 3: Calculate checksum from selected indices
if not loaded_indices:
    final_checksum = 0
else:
    # Use a lambda to process indices
    index_transform = lambda x: x * 2 + 1
    transformed_indices = [index_transform(i) for i in loaded_indices]
    
    # Calculate GCD of transformed indices
    indices_gcd = gcd_list(transformed_indices)
    
    # Calculate LCM of first two transformed indices if possible
    indices_lcm = 0
    if len(transformed_indices) >= 2:
        indices_lcm = lcm(transformed_indices[0], transformed_indices[1])
    
    # Calculate combinations of selected packages taken 2 at a time
    combo_count = calculate_combinations(len(loaded_indices), 2)
    
    # Final checksum calculation
    final_checksum = indices_gcd * indices_lcm + combo_count

print(f"Result: {final_checksum}")