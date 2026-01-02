import math

def analyze_efficiency(ratio):
    if ratio > 0.8:
        return "Optimal"
    elif ratio > 0.5:
        return "Suboptimal"
    else:
        return "Inefficient"

# Irrelevant function - distractor
def simulate_failure_mode(loads):
    critical_count = 0
    for i, val in enumerate(loads):
        if val > 90:
            critical_count += 1
    return critical_count * 0.1  # Unused result

# Another red herring function
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

# Misleading transformation chain
def transform_sequence(seq):
    transformed = []
    for i, x in enumerate(seq):
        if i % 2 == 0:
            transformed.append(x ** 0.5)
        else:
            transformed.append(x + 10)
    return [t * 1.5 for t in transformed]  # Not used later

# Core logic disguised among noise
def evaluate_threshold(values, limit=75):
    count = 0
    for v in values:
        if v >= limit:
            count += 1
    return count

# Primary calculation buried in abstraction
def calculate_peak(load_profile):
    base = 0
    adjustments = []
    
    for idx, load in enumerate(load_profile):
        if idx == 0:
            base = load * 1.1
        elif idx % 3 == 0:
            adjustments.append(load * 0.05)
        elif idx % 2 == 0:
            adjustments.append(load * 0.03)
        else:
            adjustments.append(load * 0.07)
    
    # Real computation hidden in list comprehension and zip
    factors = [math.sin(i * 0.1) for i in range(len(adjustments))]
    weighted_adj = sum(a * f for a, f in zip(adjustments, factors))
    
    temp_result = base + weighted_adj  # Intermediate value
    
    # Final adjustment based on conditional expression
    peak_value = temp_result if temp_result > 100 else temp_result * 1.2
    
    # Dead code path - never executed due to logic
    if len(load_profile) < 0:  # Impossible condition
        fallback = sum(transform_sequence(load_profile))
        peak_value = fallback
    
    return int(round(peak_value))

# Initialization with multiple irrelevant variables
baseline_readings = [68, 72, 70, 88, 94, 63, 81, 77]
diagnostic_codes = [101, 203, 107, 305]
redundant_flags = [True, False, True]

# Key data structure
grid_loads = [70, 85, 90, 95, 80, 87, 93, 76, 89, 91]

# Distractor computations
entropy_score = compute_entropy([0.1, 0.2, 0.4, 0.3])
failure_risk = simulate_failure_mode(grid_loads)
efficiency_label = analyze_efficiency(0.76)

# Real computation buried among distractions
temp_capacity = evaluate_threshold(grid_loads, 85)
buffer_zone = [x for x in grid_loads if x > 80]  # Unused list comprehension
overlap_check = any(idx == val for idx, val in enumerate(buffer_zone))  # Decoy check

# Critical execution point
peak_capacity = calculate_peak(grid_loads)

# Print required output
print(f"Result: {peak_capacity}")