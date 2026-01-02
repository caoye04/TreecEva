def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function for distraction."""
    return [x * 1.5 for x in data if x > threshold]


def normalize_vector(vec):
    """Another decoy function that is never called."""
    norm = sum(x ** 2 for x in vec) ** 0.5
    return [x / norm for x in vec]

# Simulated system metrics (some are red herrings)
raw_metrics = [0.82, 0.71, 0.93, 0.64, 0.88, 0.79, 0.55, 0.91]
dummy_data = [12, 15, 23, 45, 67]  # Unused list for distraction

# Weight coefficients for evaluation (only first four are actually used)
weights = [0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05]

# Historical baselines — irrelevant to final computation
trend_baseline = {
    'Q1': 0.78,
    'Q2': 0.81,
    'Q3': 0.76,
    'Q4': 0.85
}

# Early preprocessing — looks important but only subset matters
cleaned_metrics = []
for i, val in enumerate(raw_metrics):
    if val >= 0.6:
        cleaned_metrics.append(val * 1.1)
    else:
        cleaned_metrics.append(val * 0.9)

# Introduce more noise with a misleading transformation
adjusted_metrics = [round(m * (1 + 0.05), 2) for m in cleaned_metrics]

# Bit manipulation segment to increase complexity and distract
def calculate_checksum(values):
    chk = 0
    for v in values:
        int_val = int(v * 100)
        chk ^= int_val
        chk = (chk << 1) & 0xFFFF
    return chk % 1000

checksum = calculate_checksum(adjusted_metrics)  # Computed but unused

# Real logic begins: filter top performers
selected_indices = []
for idx, met in enumerate(adjusted_metrics):
    if met > 0.75:
        selected_indices.append(idx)

# Use zip to pair adjusted metrics with weights only for relevant entries
paired_eval = []
for idx in selected_indices:
    if idx < len(weights):  # Safety check
        paired_eval.append((adjusted_metrics[idx], weights[idx]))

# Secondary filtering: exclude any weight below 0.12 (removes some entries)
filtered_pairs = [(m, w) for m, w in paired_eval if w >= 0.12]

# Compute weighted sum using logical conditions and arithmetic
weighted_sum = 0.0
weight_total = 0.0
for metric, weight in filtered_pairs:
    include = True
    if metric < 0.7:
        include = False
    if not include:
        continue
    weighted_sum += metric * weight
    weight_total += weight

# Normalize only if valid total weight
if weight_total > 0:
    normalized_result = weighted_sum / weight_total
else:
    normalized_result = 0

# Additional conditional scaling based on checksum parity (appears significant, minor effect)
scale_factor = 1.05 if checksum % 2 == 0 else 0.95
scaled_performance = normalized_result * scale_factor

# Final evaluation function
def evaluate_performance(metrics, weights):
    base = scaled_performance  # Captures outer scope value
    penalty = 0.0
    
    # Simulate robustness check (never triggers in this input)
    if len(metrics) < 5:
        penalty += 0.05
    if min(metrics) < 0.5:
        penalty += 0.03
    
    # Bonus for high average (this will trigger)
    avg = sum(metrics) / len(metrics)
    bonus = 0.02 if avg > 0.8 else 0.0

    # Apply bonus and cap result
    result = base + bonus - penalty
    if result > 1.0:
        result = 0.98  # Artificial cap

    # Final adjustment using enumerate and zip (core requirement)
    temp_vals = [0.1, 0.2, 0.15]
    for i, (tv, wv) in enumerate(zip(temp_vals, weights[:3])):
        result -= tv * 0.01  # Small reduction, distractor

    return round(result * 1000)  # Scale to integer output

# Execute main logic
final_score = evaluate_performance(raw_metrics, weights)

# Print final result as required
print(f"Result: {final_score}")