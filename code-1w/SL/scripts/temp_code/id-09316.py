from collections import defaultdict

def analyze_department_metrics(raw_data):
    # Irrelevant aggregation for distraction
    stats = defaultdict(lambda: {"count": 0, "total": 0})
    totals = []
    temp_sum = 0

    for dept, records in raw_data.items():
        for val in records:
            stats[dept]["count"] += 1
            stats[dept]["total"] += val
            temp_sum += val % 7  # Distractor computation

    # Semi-relevant transformation
    normalized = {}
    for dept, data in stats.items():
        if data["count"] > 0:
            normalized[dept] = round(data["total"] / data["count"], 2)
            totals.append(data["total"])

    # Dead code path (never used later)
    if len(totals) > 100:
        outlier = max(totals)
        totals.remove(outlier)

    return totals


def calculate_net_flow(contribs, deducts):
    base_flow = sum(contribs)
    adjustments = 0
    
    # Real logic with some noise
    for i, deduction in enumerate(deducts):
        if i % 2 == 0:
            adjustments += deduction * 0.5
        else:
            adjustments -= deduction * 0.1

    # Core calculation
    net = base_flow - adjustments
    
    # Extra operations that don't affect result
    squared_residuals = [abs(net - x)**2 for x in contribs[:3]]
    avg_square = sum(squared_residuals) / len(squared_residuals) if squared_residuals else 0
    
    return int(round(net))

# Main execution
raw_input = {
    "engineering": [84, 92, 77, 88, 95],
    "marketing": [65, 70, 68],
    "sales": [72, 78, 80, 85]
}

# Distractor function call
interim_totals = analyze_department_metrics(raw_input)

# Key data for actual answer
contributions = [120, 200, 150, 300]
deductions = [40, 60, 25, 80]

# Critical statement
net_flow = calculate_net_flow(contributions, deductions)

print(f"Result: {net_flow}")