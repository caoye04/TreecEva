from itertools import groupby

# Simulate financial contribution and deduction flows across departments
def analyze_financial_stability(data):
    totals = {}
    for item in data:
        dept = item['department']
        if dept not in totals:
            totals[dept] = 0
        totals[dept] += item['amount']
    
    # Misleading aggregation: unused later
    peak_value = max(totals.values()) if totals else 0
    normalized = {k: round(v / (peak_value + 1e-5), 3) for k, v in totals.items()}

    return totals

# Calculate net flow after applying hierarchical adjustment rules
def calculate_net_flow(contribs, deducts):
    base_inflow = sum(contribs)
    base_outflow = sum(deducts)
    
    # Apply tiered reduction based on magnitude bands (distraction)
    inflow_tiers = []
    for amt in contribs:
        if amt > 500:
            inflow_tiers.append(('high', amt * 0.9))
        elif amt > 200:
            inflow_tiers.append(('medium', amt * 0.95))
        else:
            inflow_tiers.append(('low', amt))
    
    # Dummy grouping - no impact on result
    grouped_tiers = {k: list(g) for k, g in groupby(inflow_tiers, key=lambda x: x[0])}
    
    adjusted_inflow = sum(entry[1] for entry in inflow_tiers)
    
    # Outflow adjustments with conditional logic
    threshold_penalty = 0
    if len(deducts) > 3:
        sorted_deducts = sorted(deducts, reverse=True)
        top_three_avg = sum(sorted_deducts[:3]) / 3
        if top_three_avg > 400:
            threshold_penalty = 50

    # Spurious set operation - adds no value
    unique_contrib_rounded = set(int(round(c)) for c in contribs)
    unique_deduct_rounded = set(int(round(d)) for d in deducts)
    overlap_count = len(unique_contrib_rounded & unique_deduct_rounded)

    # Core logic: net flow depends only on total difference and penalty
    raw_diff = adjusted_inflow - base_outflow
    net_flow = raw_diff - threshold_penalty  # Final determination
    
    # Dead code branch - never executed under current logic
    if overlap_count > 10:
        net_flow *= 1.05
        
    return int(net_flow)

# Input data streams
department_data = [
    {'department': 'R&D', 'amount': 120},
    {'department': 'Sales', 'amount': 310},
    {'department': 'R&D', 'amount': 180},
    {'department': 'HR', 'amount': 95},
    {'department': 'Sales', 'amount': 420},
    {'department': 'Ops', 'amount': 270}
]

# Extract contributions and deductions from analysis
aggregated = analyze_financial_stability(department_data)
contributions = [v for v in aggregated.values()]  # [300, 730, 95, 270]
deductions = [200, 150, 300, 450, 100]  # Fixed outflows

# Key computation point
net_flow = calculate_net_flow(contributions, deductions)

print(f"Result: {net_flow}")