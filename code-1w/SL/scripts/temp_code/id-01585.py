from collections import defaultdict

# Simulate financial contribution tracking across departments
def main():
    departments = ['engineering', 'marketing', 'sales', 'hr']
    base_budget = 10000
    adjustment_factor = 0.05

    # Initialize contribution and deduction records
    contributions = defaultdict(float)
    deductions = defaultdict(float)

    # Populate contributions with realistic department data
    contributions['engineering'] = base_budget * (1 + adjustment_factor)
    contributions['marketing'] = base_budget * 0.9
    contributions['sales'] = base_budget * 1.2
    contributions['hr'] = base_budget * 0.7

    # Add some irrelevant intermediate calculations (distractors)
    projected_growth = sum(contributions.values()) * 0.03
    average_contribution = sum(contributions.values()) / len(contributions)
    growth_projection = projected_growth + average_contribution  # unused

    # Deductions based on overhead costs
    deductions['engineering'] = 1200
    deductions['marketing'] = 800
    deductions['sales'] = 1500
    deductions['hr'] = 400

    # Spurious loop: simulates review cycle but doesn't alter data
    review_cycles = 0
    for dept in departments:
        temp_review = 0
        for _ in range(2):
            temp_review += len(dept) % 3
        review_cycles += temp_review  # Dead computation

    # Auxiliary calculation: total_outlay (semi-relevant but not final)
    total_outlay = sum(deductions.values())
    total_inflow = sum(contributions.values())

    # Core logic: net flow calculation
    net_flow = calculate_net_flow(contributions, deductions)

    # Red herring: normalize values (never used)
    normalized = {}
    max_val = max(contributions.values())
    for k, v in contributions.items():
        normalized[k] = v / max_val

    # Final reporting
    print(f"Result: {net_flow}")


def calculate_net_flow(contribs, deducts):
    total_c = sum(contribs.values())
    total_d = sum(deducts.values())
    return total_c - total_d

if __name__ == "__main__":
    main()