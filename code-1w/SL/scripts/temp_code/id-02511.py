from itertools import combinations

# Simulate employee performance metrics across departments
def analyze_department_stats(base_metrics, threshold=0.75):
    high_performers = 0
    total_employees = len(base_metrics)
    cumulative_efficiency = 0.0
    efficiency_list = []

    for metric in base_metrics:
        raw_productivity = metric * 1.8 + 2
        adjusted = raw_productivity * 0.9 if raw_productivity > 10 else raw_productivity * 1.1
        capped = min(adjusted, 15)
        efficiency_list.append(capped)
        cumulative_efficiency += capped

    avg_efficiency = cumulative_efficiency / total_employees

    for e in efficiency_list:
        if e >= threshold * 12:
            high_performers += 1

    return avg_efficiency, high_performers, efficiency_list


def calculate_synergy_teams(employee_count):
    # Irrelevant combinatorial calculation (distractor)
    team_combinations = 0
    if employee_count > 3:
        for r in range(2, 5):
            team_combinations += len(list(combinations(range(employee_count), r)))
    return team_combinations  # Not used in final logic

def assess_risk_level(efficiencies):
    volatile_periods = 0
    baseline = sum(efficiencies) / len(efficiencies)
    
    for i in range(1, len(efficiencies)):
        diff = abs(efficiencies[i] - efficiencies[i-1])
        if diff > 0.5 * baseline:
            volatile_periods += 1
    
    penalty_rate = 0.15 if volatile_periods > 2 else 0.05
    return volatile_periods * penalty_rate

def evaluate_performance(prod, risk_adj):
    base = prod * 100
    adjusted = base * (1 - risk_adj)
    bonus = 10 if adjusted > 800 else 0
    return int(adjusted + bonus)

# Main execution flow
if __name__ == "__main__":
    department_data = [6.2, 7.1, 6.8, 7.5, 6.0, 8.0, 7.2]
    
    # Step 1: Analyze department statistics
    avg_prod, top_staff, all_scores = analyze_department_stats(department_data)
    
    # Step 2: Calculate irrelevant synergy combinations
    synergy_teams = calculate_synergy_teams(len(department_data))
    dummy_offset = len(list(combinations([1,2,3,4], 2))) * 0.5  # Minor red herring
    
    # Step 3: Assess operational risk from volatility
    risk_factor = assess_risk_level(all_scores)
    
    # Step 4: Evaluate final performance score
    final_score = evaluate_performance(avg_prod, risk_factor)
    
    # Step 5: Print result
    print(f"Result: {final_score}")