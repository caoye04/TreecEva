import math

def analyze_component(x, threshold=0.5):
    return x > threshold and (x * 2) % 1 < 0.3

def compute_weighted_sum(data, weights):
    # Irrelevant normalization
    norm = sum(weights)
    normalized = [w / norm for w in weights]
    return sum(d * w for d, w in zip(data, normalized))

def filter_outliers(values, limit=3):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) <= limit * std_dev]

def dummy_transformation(seq):
    # Dead code path - never contributes to final result
    transform = lambda s: ''.join(chr((ord(c) - 96) % 26 + 97) for c in s.lower())
    return transform(seq)

def accumulate_metrics(raw_logs):
    counts = {}
    for log in raw_logs:
        key = log % 10
        counts[key] = counts.get(key, 0) + 1
    # Misleading intermediate: looks important but unused later
    temp_analysis = {k: v * k for k, v in counts.items()}
    return [counts.get(i, 0) for i in range(5)]

def generate_baseline_profile():
    # Complex but irrelevant structure generation
    base = [0.1 * i for i in range(1, 6)]
    shift = lambda a, b: [x + 0.05 for x in a] if sum(a) < b else [x - 0.05 for x in a]
    profile = shift(base, 1.5)
    # Decoy transformation
    profile = [math.sin(x) for x in profile]
    return [0.15] * 5  # Actual simplified return

def validate_stability(readings):
    if len(readings) < 2:
        return False
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return all(d < 0.2 for d in diffs)

def evaluate_performance(metrics, baseline):
    adjusted = [(m * 1.2) - b for m, b in zip(metrics, baseline)]
    capped = [min(max(val, 0.0), 1.0) for val in adjusted]
    
    # Core logic hidden among distractions
    scaling_factor = 1000
    penalty = 0
    if len(metrics) > 4:
        penalty += 5
    if sum(metrics) < 0.5:
        penalty += 10
    
    # Critical computation buried in noise
    raw_value = sum(capped) * scaling_factor - penalty
    
    # Distractor: complex-looking but unused calculation
    auxiliary_score = math.log(1 + sum(m * b for m, b in zip(metrics, baseline)))
    auxiliary_score *= 100
    
    # Another red herring
    outlier_check = filter_outliers([raw_value, auxiliary_score, 42.0])
    
    # Final assignment - the real answer source
    final_score = int(raw_value)  # Truncate to integer
    
    # Unused but misleading debug print
    # print(f'Debug - aux: {auxiliary_score}, cap: {capped}')
    
    return final_score

# Simulated input data
sensor_logs = [123, 456, 789, 101, 112, 131, 415, 161, 718, 192, 232]

# Generate metrics from logs
extraction = accumulate_metrics(sensor_logs)

# Real baseline
baseline_config = generate_baseline_profile()

# Validate system state - this affects nothing but looks important
status_ok = validate_stability([0.1, 0.15, 0.14, 0.16, 0.15])

# Key statement that produces the target variable
final_score = evaluate_performance(extraction, baseline_config)

# Print result as required
print(f"Result: {final_score}")