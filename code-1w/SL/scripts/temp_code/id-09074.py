def analyze_workload_efficiency():
    tasks_completed = [8, 12, 5, 17, 3]
    time_spent_hours = [2, 3, 1, 4, 1]
    
    # Irrelevant metric: total_entries
    total_entries = len(tasks_completed) + len(time_spent_hours)
    
    efficiency_ratios = []
    for i in range(len(tasks_completed)):
        if time_spent_hours[i] > 0:
            ratio = tasks_completed[i] / time_spent_hours[i]
            efficiency_ratios.append(round(ratio, 2))
    
    # Distractor computation: average_time (not used later)
    total_time = sum(time_spent_hours)
    average_time = total_time / len(time_spent_hours) if time_spent_hours else 0
    
    # Semi-relevant filtering
    high_performers = [r for r in efficiency_ratios if r >= 4.0]
    performance_flag = len(high_performers) >= 3
    
    # Conditional expression with slicing distraction
    base_score = 50 if performance_flag else 30
    bonus = sum(efficiency_ratios[:3]) * 2 if len(efficiency_ratios) >= 3 else 0
    
    # Additional red herring: unused function call simulation
    temp_diagnostic = (sum(tasks_completed) // len(tasks_completed)) * 1.5
    
    # Core logic hidden among distractions
    adjustment_factor = 1.2 if sum(bonus for _ in range(1)) > 40 else 0.8
    raw_score = base_score + bonus
    final_adjustment = raw_score * adjustment_factor
    
    # Final calculation point
    final_score = int(final_adjustment - 10)  # Key assignment
    
    # Print result as required
    print(f"Result: {final_score}")
    
    return final_score

# Helper function to trigger key statement
def calculate_performance_rating():
    return analyze_workload_efficiency()

# Execution point
final_score = calculate_performance_rating()