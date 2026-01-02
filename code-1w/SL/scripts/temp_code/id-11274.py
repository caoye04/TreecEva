def analyze_efficiency(data, threshold=0.75):
    """Irrelevant helper function analyzing efficiency (dead code path)."""
    return sum(1 for x in data if x > threshold) / len(data)


def compute_entropy(values):
    """Another decoy function not used in main logic."""
    from math import log
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total
        entropy -= p * log(p) if p > 0 else 0
    return entropy

# Unused global constants (distractors)
MAX_ITERATIONS = 10000
DEFAULT_TIMEOUT = 30
RETRY_DELAY = 0.5

# Simulated sensor readings (some relevant, some not)
sensor_data = [0.4, 0.7, 0.9, 0.3, 0.6]
event_flags = [True, False, True, True, False]

def preprocess(stream):
    """Apply gain and offset correction (partially irrelevant)."""
    corrected = []
    gain = 1.2
    offset = -0.1
    for val in stream:
        corrected.append(max(0.0, min(1.0, val * gain + offset)))
    return corrected

# Misleading intermediate transformation
calibrated = preprocess(sensor_data)
temporal_weight = len([x for x in calibrated if x >= 0.5])

# Real computation begins here
weights = [0.1, 0.3, 0.4, 0.2]
metrics = [0.85, 0.72, 0.93, 0.68]  # Accuracy, Recall, Precision, F1

# Distractor: unused list comprehension with side effects avoided
_ = [x * 2 for x in weights if x < 0.25]

status_codes = {1: 'OK', 2: 'WARN', 3: 'ERROR'}

# Key function containing red herrings and real logic
def evaluate_performance(m, w):
    if not m or not w:
        return 0.0
    
    # Irrelevant validation block (never triggers due to input)
    if any(x < 0 or x > 1 for x in m):
        raise ValueError("Metrics out of bounds")
    
    # Real weighted score calculation
    raw_score = sum(m[i] * w[i] for i in range(len(m)))
    
    # Apply nonlinear adjustment based on consistency
    differences = [abs(metrics[i] - metrics[i+1]) for i in range(len(metrics)-1)]
    consistency_penalty = sum(differences) * 0.05
    adjusted_score = raw_score - consistency_penalty
    
    # Artificial clamp that doesn't trigger (misleading)
    final = max(0.0, min(1.0, adjusted_score))
    
    # Extra distraction: enumerate and zip usage (partly irrelevant)
    labels = ['A', 'B', 'C', 'D']
    for i, (label, val) in enumerate(zip(labels, m)):
        if val > 0.9 and i % 2 == 0:
            final += 0.02  # Never reached since only index 2 has val>0.9 and it's even
    
    # Conditional expression red herring
    bonus = 0.03 if all(x > 0.7 for x in m[:3]) else 0.0
    final += bonus if 'Precision' in [x.upper() for x in labels] else 0.0  # bonus never added due to condition
    
    # Actual small bonus applied silently
    if len(m) == len(w):
        final += 0.01
    
    return final

# Dead code path: event processing loop (unused)
for idx, flag in enumerate(event_flags):
    if not flag:
        continue
    sensor_data[idx] *= 1.1

# Main execution point
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")