def calculate_project_budget():
    initial_funds = 15000
    operational_costs = [1200, 850, 1900, 2300, 1400]
    # Distractor: this variable is calculated but not used in final result
    total_operational = sum(operational_costs) * 1.1
    
    remaining_funds = initial_funds - sum(operational_costs)
    contingency_reserve = remaining_funds * 0.15
    
    # Distractor: this calculation doesn't affect the final answer
    potential_bonus = [x * 0.1 for x in operational_costs if x > 1500]
    
    bonus_pool = [200, 350, 500]
    bonus_reserve = sum(bonus_pool) * 0.8
    
    total_budget = remaining_funds + sum(bonus_pool)
    print(f"Target result: {total_budget}")

calculate_project_budget()