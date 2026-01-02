from collections import defaultdict
import math

def analyze_efficiency(metrics):
    efficiency = 0
    adjustments = [0.1, -0.2, 0.15, 0.05]
    temp_buffer = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            efficiency += val * (1 + adjustments[i // 2])
        else:
            efficiency -= val * 0.1
        temp_buffer.append(efficiency * (i + 1))
    return efficiency

def track_history(data_log):
    history_map = defaultdict(int)
    for entry in data_log:
        history_map[entry] += 1
    return dict(history_map)

def compute_stability(indices):
    base = sum([x ** 0.5 for x in indices if x > 0])
    penalty = 0
    for i in range(len(indices)):
        if i > 0 and indices[i] < indices[i-1]:
            penalty += 0.5
    return base - penalty

def evaluate_performance(output_levels, risk):
    scaling_factor = 1.5 if risk < 3 else 0.8
    boost = 1.2
    raw_value = sum(output_levels) * scaling_factor
    adjusted = raw_value * boost
    if adjusted > 100:
        adjusted = 95 + (adjusted - 100) * 0.5
    return int(adjusted)

def main():
    # Simulated productivity metrics over 5 days
    daily_output = [18, 22, 19, 25, 20]
    risk_assessment = [3, 1, 4, 2, 5]
    
    # Irrelevant string processing (distractor)
    status_messages = ["System nominal", "Minor lag", "All clear", "Caution", "Normal"]
    flagged_states = [msg.upper().count('C') for msg in status_messages]
    
    # Misleading use of set operations (semi-relevant)
    unique_risks = list(set(risk_assessment))
    risk_sorted = sorted(unique_risks, reverse=True)
    
    # Dummy counter for tracking (dead code path)
    count_tracker = defaultdict(int)
    for r in risk_assessment:
        count_tracker[r] += 1
    
    # Compute auxiliary values (some used, some not)
    productivity = analyze_efficiency(daily_output)
    stability_index = compute_stability(daily_output)
    risk_factor = len([r for r in risk_assessment if r >= 3])
    
    # Unused complex tuple unpacking (distractor)
    config_settings = ('high', 'auto', 3.14, True)
    mode, sync, threshold, active = config_settings
    
    # Core logic embedded among distractions
    final_score = evaluate_performance(productivity, risk_factor)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()