def analyze_sequence(data):
    """Irrelevant helper function for sequence analysis."""
    if len(data) < 5:
        return sum(x ** 2 for x in data if x % 2 == 0)
    else:
        temp = [x for x in data if x > 0]
        return sum(temp[i] * i for i in range(len(temp)) if i % 3 == 0)


def preprocess_metrics(raw):
    """Applies normalization but is not used in final computation."""
    mean_val = sum(raw) / len(raw)
    normalized = [(x - mean_val) / mean_val for x in raw]
    return [round(x, 3) for x in normalized]

# Decoy weight sets (only one will be used)
WEIGHT_SET_A = [0.1, 0.3, 0.4, 0.2]
WEIGHT_SET_B = [0.2, 0.2, 0.3, 0.3]  # Unused
WEIGHT_SET_C = [0.4, 0.1, 0.2, 0.3]  # Unused

# Historical metrics (distractor data)
historical_data = [
    [85, 78, 90, 88],
    [80, 82, 85, 87],
    [90, 88, 87, 92]
]

# Current performance metrics
metrics = [88, 85, 92, 89]

# Weighting scheme (critical)
weights = WEIGHT_SET_A  # Only this line matters

# Red herring: complex preprocessing that isn't used
tempting_features = preprocess_metrics(metrics)

# Misleading intermediate calculation
drift_score = sum(abs(metrics[i] - historical_data[-1][i]) for i in range(4))

# Dummy function to create illusion of complexity
def calculate_stability(seq):
    diffs = [abs(seq[i+1] - seq[i]) for i in range(len(seq)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

stability = calculate_stability([metrics[0], metrics[2], metrics[1]])

# Simulated trend analysis (dead code path)
current_trend = None
if metrics[3] > metrics[2] > metrics[1]:
    current_trend = 'upward'
elif metrics[3] < metrics[2] < metrics[1]:
    current_trend = 'downward'
else:
    current_trend = 'stable'

# Core logic hidden among distractions
def evaluate_performance(m, w):
    base_score = sum(m[i] * w[i] for i in range(len(m)))
    
    # Conditional bonus based on slice properties
    recent = m[-2:]  # last two metrics
    if all(score >= 85 for score in recent):
        bonus = 7.5
    else:
        bonus = 2.5
    
    # Penalty for inconsistency in middle metrics (slice)
    mid_range = m[1:3]
    variation = max(mid_range) - min(mid_range)
    penalty = 3.0 if variation > 8 else 0.0
    
    # Bit manipulation check: count set bits in rounded base
    base_int = int(round(base_score))
    bit_count = bin(base_int).count('1')
    bit_bonus = 1.0 if bit_count % 2 == 1 else 0.0
    
    # Final composition
    result = base_score + bonus - penalty + bit_bonus
    
    # Additional red herring: unused transformation
    transformed = [round(result * (1 + w[i]), 2) for i in range(len(w))]
    
    return result

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Irrelevant post-processing
def generate_report(score, data_slice):
    category = 'Excellent' if score > 90 else 'Good' if score > 80 else 'Average'
    details = {
        'classification': category,
        'anomalies': [x for x in data_slice if x < 80],
        'peak': max(data_slice),
        'consistency': 'high' if max(data_slice) - min(data_slice) < 10 else 'medium'
    }
    return details

report_summary = generate_report(final_score, metrics)

# Debugging leftovers (unused)
DEBUG_MODE = False
temp_result = None
if DEBUG_MODE:
    temp_result = analyze_sequence(metrics)

# Output the target result
print(f"Target result: {final_score}")