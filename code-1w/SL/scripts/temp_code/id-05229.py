import math

# Irrelevant helper function (dead code path)
def unused_utility(data):
    return [x ** 0.5 for x in data if x > 0]

# Misleading preprocessing with decoy transformations
def preprocess_signals(raw_data):
    filtered = [x for x in raw_data if x % 2 == 0]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return [round(x, 3) for x in normalized]

# Distractor: complex but unused signal analysis
def analyze_trend(sequence):
    trend_scores = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_scores.append(1.1)
        elif sequence[i] < sequence[i-1]:
            trend_scores.append(-0.9)
        else:
            trend_scores.append(0.05)
    return sum(trend_scores)

# Real logic starts here — subtle and buried among noise
def compute_stability_index(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return math.exp(-variance / (mean_val + 1e-8))

# Bit manipulation red herring
def encode_flags(mode, debug=False):
    base = mode << 4
    if debug:
        base |= 1
    return base ^ 255  # irrelevant obfuscation

# Core evaluation logic — depends on multiple concepts
def evaluate_performance(weights, outcomes):
    # Step 1: Apply weighted transformation using lambda and slicing
    trimmed_outcomes = outcomes[1:-1]  # remove outliers?
    weighted_components = list(map(lambda w, o: w * (o ** 0.7), weights, trimmed_outcomes))
    
    # Step 2: Conditional adjustment based on parity pattern (red herring check)
    parity_sum = sum(1 for x in trimmed_outcomes if x % 2 == 0)
    adjustment = 1.0
    if parity_sum > 2:
        adjustment = 0.9  # misleading penalty
    
    # Step 3: Stability analysis (actual key step)
    stability = compute_stability_index(weighted_components)
    
    # Step 4: Combinatoric factor from index permutations (fake complexity)
    combo_factor = 1
    for i in range(1, min(len(weighted_components), 4)):
        combo_factor *= i  # 3! = 6, not actually needed
    
    # Step 5: Actual determinant — hidden in middle
    base_score = sum(weighted_components) * stability * adjustment
    
    # Step 6: Decoy final normalization
    capped_score = min(base_score, 100.0)
    encoded = encode_flags(int(capped_score) % 16)
    final = capped_score + (encoded * 0.01)  # tiny perturbation — looks important
    
    # Step 7: Final correction based on initial condition (hidden dependency)
    first_weight = weights[0]
    if first_weight > 0.3:
        final *= 1.1  # critical multiplier
    
    return round(final, 4)

# Irrelevant global constants
data_buffer = [0] * 16
system_mode = 7
active_channels = (1, 0, 1, 1)

# Input data — realistic domain-specific values
metric_weights = [0.45, 0.35, 0.20, 0.50, 0.10]
raw_outcomes = [88, 76, 92, 81, 79, 85]

# Unused intermediate variables (distractors)
processed_metrics = preprocess_signals(raw_outcomes)
trend_analysis = analyze_trend(raw_outcomes)
baseline_ref = sum(raw_outcomes) / len(raw_outcomes)

# Key execution point
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Output result as required
print(f"Result: {final_score}")