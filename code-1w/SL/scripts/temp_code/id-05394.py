from itertools import combinations

def analyze_efficiency(tasks):
    # Irrelevant helper: calculates pairwise task overlaps (not used in final result)
    overlaps = []
    for pair in combinations(tasks, 2):
        overlap = len(set(pair[0]) & set(pair[1]))
        overlaps.append(overlap)
    return sum(overlaps)  # Dead-end computation

def calculate_baseline(workload):
    # Semi-relevant: computes average but only used to seed a distractor
    total_load = sum(workload)
    avg_load = total_load / len(workload)
    threshold = avg_load * 1.2
    high_load_count = sum(1 for w in workload if w > threshold)
    return high_load_count  # Used in red_herring_metric only

def compute_stability_index(milestones):
    # Computes variance-like metric; actually contributes to risk_factor
    mean_val = sum(milestones) / len(milestones)
    squared_diffs = [(m - mean_val)**2 for m in milestones]
    variance = sum(squared_diffs) / len(squared_diffs)
    stability = 1 / (1 + variance)  # Higher variance → lower stability
    return stability

def evaluate_performance(output_levels, risk):
    # Core logic: performance score based on output and adjusted risk
    base_performance = sum(output_levels)
    adjustment = 1 - risk
    final_score = base_performance * adjustment
    return int(final_score)

# Main execution block
if __name__ == "__main__":
    # Real input data
    productivity = [85, 90, 95, 87, 93]  # Weekly output units
    deadlines_met = [True, True, False, True, True]  # Distraction series
    team_size = 7  # Unused constant
    project_phases = ['planning', 'dev', 'testing', 'review', 'deployment']

    # Distractor computations
    complexity_scores = [2, 3, 4, 3, 2]
    analysis_result = analyze_efficiency([[1,2,3], [2,3,4], [1,3,5], [4,5,6], [2,4,6]])
    
    baseline_flag = calculate_baseline([50, 60, 55, 70, 65])
    red_herring_metric = baseline_flag * 10

    # Relevant data for risk
    milestone_delays = [0, 1, 3, 1, 0]  # Days delayed per milestone
    risk_factor = 1 - compute_stability_index(milestone_delays)

    # Key statement
    final_score = evaluate_performance(productivity, risk_factor)

    # Print result as required
    print(f"Target result: {final_score}")