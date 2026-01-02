from itertools import combinations

# System resource simulation with filtering logic
def analyze_workloads(servers, load_threshold):
    critical = []
    for s in servers:
        if sum(s['load']) > load_threshold:
            critical.append(s['id'])
    return critical

# Irrelevant helper: computes pairwise load variances (not used in final result)
def compute_variance_pairs(servers):
    vars = []
    for a, b in combinations(servers, 2):
        mean_a = sum(a['load']) / len(a['load'])
        mean_b = sum(b['load']) / len(b['load'])
        var = (mean_a - mean_b) ** 2
        vars.append(var)
    return sum(vars)  # Dead-end computation

# Core capacity calculation
def calculate_density_score(elements):
    total = 0
    for e in elements:
        if isinstance(e, tuple) and len(e) == 3:
            total += e[1] * e[2]
    return total

def calculate_remaining_capacity(units, constraints):
    base_score = calculate_density_score(units)
    
    # Simulate constraint filtering
    valid_units = []
    for u in units:
        if isinstance(u, tuple) and len(u) == 3:
            id, dim, qty = u
            if dim > constraints['min_dim'] and qty <= constraints['max_qty']:
                valid_units.append(u)
    
    # Actual answer derivation
    capacity = base_score
    for unit in valid_units:
        capacity -= (unit[1] // 2)  # Adjustment based on dimension
    
    # Distractor: unused transformation
    transformed = [((u[1]+u[2]) % 7) for u in units if u[0] % 2 == 0]
    _ = sum(transformed) * 0.5  # Computation with no effect
    
    return int(capacity)

# Data setup
units = [
    (101, 8, 4),
    (102, 12, 3),
    (103, 5, 6),
    (104, 15, 2),
    (105, 7, 5)
]

constraints = {
    'min_dim': 6,
    'max_qty': 5
}

# Simulated server monitoring (irrelevant to main logic)
servers = [
    {'id': 'A', 'load': [70, 82, 77]},
    {'id': 'B', 'load': [65, 78, 60]},
    {'id': 'C', 'load': [90, 88, 95]}
]

_ = analyze_workloads(servers, 200)  # Side analysis
_ = compute_variance_pairs(servers)  # More distraction

# Key execution point
final_capacity = calculate_remaining_capacity(units, constraints)
print(f"Target result: {final_capacity}")