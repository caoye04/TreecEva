from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for length in range(2, len(sequence) + 1):
        for subset in combinations(sequence, length):
            if sum(subset) % 3 == 0:
                count += 1
    return count

def calculate_baseline(data):
    # Irrelevant helper: computes something not used in final result
    adjusted = [x * 1.5 for x in data if x > 5]
    return sum(adjusted) // len(adjusted) if adjusted else 0

def evaluate_performance(outcomes, factor):
    success_count = sum(1 for x in outcomes if x)
    total_tasks = len(outcomes)
    base_rate = success_count / total_tasks if total_tasks else 0
    
    # Intermediate metric with partial relevance
    bonus_points = 0
    streak = 0
    for outcome in outcomes:
        if outcome:
            streak += 1
            if streak == 3:
                bonus_points += 2
                streak = 0  # Reset after awarding
        else:
            streak = 0
    
    # Distractor computation: looks important but unused
    hypothetical = [i for i, val in enumerate(outcomes) if not val]
    phantom_risk = len(hypothetical) ** 2 if hypothetical else 0
    
    # Core calculation
    raw_score = base_rate * 100 + bonus_points * factor
    penalty = 0
    if len(outcomes) < 5:
        penalty = 10
    
    final_value = int(raw_score - penalty)
    
    # Extra distraction: set operation that isn't directly used
    unique_rewards = set(bonus_points * i for i in range(1, 4))
    reward_adjustment = len(unique_rewards.intersection({2, 4, 6}))
    
    # Final adjustment based on actual logic path
    final_value += reward_adjustment
    
    return final_value

# Main execution
if __name__ == '__main__':
    # Simulated task outcomes (True = success)
    task_outcomes = [True, True, False, True, True, False, True]
    
    # Efficiency determined via unrelated combinatorial analysis
    signal_data = [2, 3, 4, 6]
    pattern_complexity = analyze_patterns(signal_data)
    efficiency_factor = pattern_complexity % 7 or 1
    
    # Baseline calculation - dead end, not used
    baseline_metric = calculate_baseline([4, 7, 8, 5, 9])
    
    # Key state tracking
    audit_log = []
    for idx, outcome in enumerate(task_outcomes):
        audit_log.append(f"Task{idx+1}:{'PASS' if outcome else 'FAIL'}")
    
    # Critical assignment point
    final_score = evaluate_performance(task_outcomes, efficiency_factor)
    
    # Print required output
    print(f"Result: {final_score}")