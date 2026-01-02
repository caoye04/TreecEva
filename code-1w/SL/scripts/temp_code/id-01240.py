def analyze_efficiency(values):
    if not values:
        return 0
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return avg - variance * 0.5

# Irrelevant helper function (decoy)
def compute_bandwidth_utilization(rate, limit=100):
    utilization = (rate / limit) * 100
    penalty = 10 if utilization > 90 else 0
    return utilization - penalty

# Unused data structure (red herring)
benchmark_templates = {
    'cpu': {'base': 80, 'overclock': 120},
    'gpu': {'base': 60, 'overclock': 150}
}

# Distractor variables
temp_cache = [i ** 2 for i in range(10)]
scaling_factor = 1.75
offset_correction = -3

# Core logic disguised among distractions
def process_metrics(raw):
    adjusted = [x * 1.1 + 2 for x in raw]
    filtered = [x for x in adjusted if x > 25]
    return filtered if len(filtered) > 3 else [0]

def validate_stability(indices):
    total = 0
    for idx in indices:
        if idx < 0:
            continue
        total += idx % 7
    return total > 15

thresholds = {
    'efficiency': 40,
    'stability': 15,
    'density': 3
}

metric_data = [20, 15, 30, 45, 28, 33]

# Misleading intermediate calculation (dead path)
baseline_rank = sum(x // 5 for x in metric_data) * 0.8

processed = process_metrics(metric_data)
efficiency_rating = analyze_efficiency(processed)

# Conditional expression used as required
is_operational = 'yes' if efficiency_rating > thresholds['efficiency'] else 'no'

stability_flags = [1 if x % 2 == 0 else 0 for x in metric_data]
valid_stability = validate_stability(stability_flags)

def calculate_density(data):
    unique_count = len(set(data))
    return unique_count / len(data) if data else 0

density_score = calculate_density(metric_data)

# Key branching logic with nesting depth 4
if efficiency_rating > thresholds['efficiency']:
    if valid_stability:
        if density_score >= thresholds['density']:
            base_score = 95
        else:
            base_score = 70
    else:
        if all(x > 20 for x in processed):
            base_score = 60
        else:
            base_score = 40
else:
    temp_val = sum(temp_cache[:5]) / scaling_factor
    if temp_val > 100:
        base_score = 50
    else:
        base_score = 30

# Final computation chain
adjustment = (efficiency_rating * 0.3) + (density_score * 5)

# Critical statement
final_score = base_score + adjustment

# Output requirement
print(f"Result: {final_score}")