def analyze_metrics(data, threshold=0.5):
    # Irrelevant preprocessing: normalize data (not actually used in final logic)
    normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
    outliers = [x for x in data if x > threshold * 2]

    # Semi-relevant transformation
    filtered = [x for x in data if x >= threshold]
    squared_residuals = [(x - sum(filtered)/len(filtered))**2 for x in filtered]
    variance = sum(sliced_devs[:len(squared_residuals)//2]) if (sliced_devs := squared_residuals[::2]) else 0

    return len(filtered), variance > 0.1


def evaluate_strategy(pattern):
    score = 0
    history = []
    for i, p in enumerate(pattern):
        if i % 3 == 0:
            score += p * 2
        elif p > 0:
            score += p // 2
        history.append(score)
    
    # Distractor: complex history analysis that isn't used
    trend = 'rising' if all(history[i] <= history[i+1] for i in range(len(history)-1)) else 'volatile'
    avg_change = sum(history[i+1] - history[i] for i in range(len(history)-1)) / len(history) if len(history) > 1 else 0
    
    # Key decision based on modular pattern
    mod_penalty = sum(1 for x in pattern if x % 4 == 3)
    return score - mod_penalty

# Main execution
raw_inputs = [0.3, 0.6, 0.4, 0.9, 0.2, 0.7]
data_active = [int(x * 10) for x in raw_inputs]  # Scale to integers

# Unused but misleading variable
processed_snapshot = data_active[::-1][:len(data_active)//2]

# Conditional expression with slicing and comparison
is_stable = len([x for x in data_active if x > 5]) >= 3 else False

# Dummy tracking variables
iteration_log = {}
consistency_flags = []

# Simulate multi-phase evaluation
phase_scores = []
for idx, val in enumerate(data_active):
    temp_adjust = val + (idx % 4) if val % 2 == 0 else val - (idx % 3)
    phase_scores.append(temp_adjust * 0.1)

# Key branching logic with distractors
if is_stable:
    base_metric = sum(data_active[i] for i in range(0, len(data_active), 2))
else:
    base_metric = sum(data_active[i] for i in range(1, len(data_active), 2))

# Red herring: unused statistical check
mean_val = sum(data_active) / len(data_active)
deviation_flag = any(abs(x - mean_val) > 2 for x in data_active)

# Actual core logic hidden among distractions
count_high = len([x for x in data_active if x >= 6])
effective_input = [x for x in data_active if x > 0]

# Nested conditional with slicing and arithmetic
secondary_weight = sum(effective_input[:3]) if len(effective_input) > 2 else sum(effective_input)

# Boolean logic with short-circuiting and comparisons
bonus_applied = count_high > 2 and (secondary_weight > 10 or base_metric < 20)
penalty_factor = 2 if not bonus_applied and deviation_flag else 1

# Core strategy evaluation (uses prior function)
strategy_result = evaluate_strategy(data_active)

# Final performance calculation — this is where 'final_score' is set
validity_check = analyze_metrics(raw_inputs, threshold=0.4)
final_score = strategy_result + base_metric

# Irrelevant post-processing
final_score *= 1.0  # Neutral operation
if final_score > 0:
    final_score += 0  # Dead code

print(f"Result: {final_score}")