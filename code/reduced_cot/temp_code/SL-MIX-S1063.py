import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2

def optimize_loading(weights, priorities, capacity):
    n = len(weights)
    items = [(priorities[i], weights[i], i) for i in range(n)]
    items.sort(key=lambda x: x[0]/x[1] if x[1] > 0 else float('inf'), reverse=True)
    
    total_weight = 0
    max_priority = 0
    selected = []
    
    for priority, weight, idx in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            max_priority += priority
            selected.append(idx)
    
    return max_priority, selected

# Package data: (weight, priority)
packages = [
    (12, 30),
    (7, 25),
    (5, 15),
    (9, 20),
    (4, 10),
    (8, 18),
    (6, 22),
    (3, 8)
]

weights = [pkg[0] for pkg in packages]
priorities = [pkg[1] for pkg in packages]
capacity = 25

# Calculate geometric properties for warehouse layout
warehouse_corners = [(0, 0), (10, 0), (10, 8), (0, 8)]
area = calculate_polygon_area(warehouse_corners)

# Apply number theory to adjust capacity based on prime factors
adjusted_capacity = capacity
if is_prime(capacity):
    adjusted_capacity = capacity + 1
else:
    factors = []
    temp = capacity
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            temp //= d
        else:
            d += 1
    if temp > 1:
        factors.append(temp)
    if len(factors) >= 2:
        adjusted_capacity = lcm(factors[0], factors[-1])

# Optimization using greedy algorithm
max_priority_loaded, selected_packages = optimize_loading(weights, priorities, adjusted_capacity)

# Short-circuit evaluation for final check
final_check = (len(selected_packages) > 0) and (max_priority_loaded > 0) and (adjusted_capacity >= 0)

if not final_check:
    max_priority_loaded = -1

print(f"Result: {max_priority_loaded}")