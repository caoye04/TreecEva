from itertools import combinations

# Simulate employee performance metrics across departments
def analyze_department_metrics(base_values):
    adjusted = [val * 1.1 for val in base_values if val > 50]
    outliers = [val for val in base_values if val < 30]
    # Irrelevant aggregation
    avg_outlier = sum(outliers) / len(outliers) if outliers else 0
    return adjusted

# Auxiliary function with red herring logic
def calculate_theoretical_limit(n):
    if n <= 1:
        return 1
    limit = 0
    for i in range(1, n + 1):
        limit += i * (i + 1) // 2
    return limit  # Never used in main logic

# Core evaluation pipeline
def evaluate_productivity_scores(raw_data):
    filtered = [x for x in raw_data if x >= 40]
    smoothed = [val * 0.95 for val in filtered]
    trend = sum(smoothed) / len(smoothed) if smoothed else 0
    return trend

# Risk assessment with dummy branches
def assess_risk_level(entries):
    critical = [e for e in entries if e > 80]
    warnings = [e for e in entries if 60 <= e <= 70]
    suppression_factor = 0.85 if len(warnings) > 2 else 1.0
    # Unused transformation
    masked_entries = [e ^ 7 for e in entries]  
    return len(critical) * suppression_factor

# Main logic path
base_input = [45, 60, 75, 85, 90, 25, 40, 55]
productivity = evaluate_productivity_scores(base_input)
risk_entries = [70, 85, 65, 90, 68, 88]
risk_factor = assess_risk_level(risk_entries)

# Generate irrelevant combinatorial features
pairwise_sums = [sum(pair) for pair in combinations(base_input, 2)]
theoretical_cap = calculate_theoretical_limit(5)

# Key computation: performance score adjusted by risk
def evaluate_performance(prod, risk):
    base_rating = prod * 1.2
    penalty = base_rating * (risk * 0.05)
    final_rating = base_rating - penalty
    return int(final_rating)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")