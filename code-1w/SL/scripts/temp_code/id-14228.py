def analyze_efficiency(data, thresholds):
    """Irrelevant helper function for distraction."""
    return [x * 2 for x in data if x > thresholds[0]]


def preprocess_signal(signal, window_size=3):
    """Another decoy function that simulates signal processing but is unused."""
    smoothed = []
    for i in range(len(signal) - window_size + 1):
        smoothed.append(sum(signal[i:i+window_size]) / window_size)
    return smoothed

# Unused global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 5.7
RETRY_LIMIT = 3

# Simulated sensor metrics with meaningful names
metrics = [0.82, 0.91, 0.77, 0.65, 0.88]
weights = [3, 4, 2, 1, 5]

# Dead code path with misleading intermediate calculation
aggregate = 0
for val in metrics:
    if val > 0.8:
        aggregate += val * 100  # Looks important, but not used later

# Irrelevant transformation using enumerate and zip (adds interference)
decoded = []
for i, (m, w) in enumerate(zip(metrics, weights)):
    adjusted = m * w
    if i % 2 == 0:
        adjusted = round(adjusted, 1)  # Distracting rounding
    decoded.append(adjusted + 1.5)  # Adds noise, not used

# Simulate a bitmask analysis (bitwise red herring)
flag_register = 0b101010
mask = 0b111100
masked_value = flag_register & mask  # Used nowhere

# Unused list slicing operation for interference
subset = metrics[1:4:1]
subset_inverted = subset[::-1]  # Looks algorithmic, but irrelevant

# Conditional expression with dummy branching
mode = 'aggressive' if sum(weights) > 10 else 'conservative'

# Another decoy: set operations that don't affect outcome
unique_weights = set(weights)
weight_coverage = unique_weights.union({6, 7})  # Not used

# Core logic hidden among distractions
scaling_factor = 1.25

# Key computation disguised within conditional branches
def evaluate_performance(mets, wts):
    raw_score = 0
    bonus = 0
    penalty = 0

    for idx, (metric, weight) in enumerate(zip(mets, wts)):
        contribution = metric * weight * scaling_factor
        raw_score += contribution

        # Conditional logic with early impact
        if metric >= 0.8:
            bonus += weight // 2
        elif metric < 0.7:
            penalty += weight

        # Short-circuit evaluation pattern
        if idx > 2 and (metric > 0.9 or (metric > 0.85 and weight >= 4)):
            bonus += 1

    # Final adjustment using bitwise XOR on accumulated values
    adjusted_bonus = bonus ^ 2  # Manipulates bonus via bit logic
    net_deduction = penalty >> 1  # Right shift as obfuscation

    final = raw_score + adjusted_bonus - net_deduction

    # Additional red herring: tuple unpacking that does nothing
    temp_vals = (raw_score, adjusted_bonus, net_deduction)
    _, _, _ = temp_vals  # Useless unpacking

    return int(final)  # Ensure integer result

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Output required format
print(f"Target result: {final_score}")