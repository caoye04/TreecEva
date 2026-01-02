from collections import defaultdict, Counter
import itertools

# Simulated system telemetry data
telemetry_streams = [
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
]

# Irrelevant helper (decoy)
def analyze_health(stream):
    return sum(s ** 2 for s in stream) / len(stream)

# Unused transformation (dead code path)
def transform_signal(data):
    result = []
    for x in data:
        if x > 0.5:
            result.append(x * 1.5)
        else:
            result.append(x * 0.5)
    return result

# Misleading metric calculation (red herring)
raw_energy = 0
for seq in telemetry_streams:
    energy = 0
    for val in seq:
        energy += val * val  # Redundant since val is 0 or 1
    raw_energy += energy  # This accumulates but isn't used later

# Distractor: frequency counting with no impact
event_counter = Counter()
for stream in telemetry_streams:
    for event in stream:
        event_counter[event] += 1

# Baseline thresholds (some irrelevant entries)
baseline = {
    'threshold_a': 0.65,
    'threshold_b': 0.75,
    'noise_floor': 0.1,
    'max_outlier': 999  # unused
}

# Core metrics extraction
metrics = defaultdict(float)
for i, stream in enumerate(telemetry_streams):
    # Compute active segments using bit patterns
    active_periods = 0
    for j in range(len(stream) - 1):
        if stream[j] == 1 and stream[j+1] == 1:
            active_periods += 1
    metrics[f'stability_{i}'] = active_periods

    # Compute isolated events (single 1s surrounded by 0s)
    isolated = 0
    padded = [0] + stream + [0]
    for j in range(1, len(padded) - 1):
        if padded[j] == 1 and padded[j-1] == 0 and padded[j+1] == 0:
            isolated += 1
    metrics[f'isolation_{i}'] = isolated

# Secondary derived features (mix of relevant and irrelevant)
metrics['total_stability'] = sum(metrics[f'stability_{i}'] for i in range(3))
metrics['total_isolation'] = sum(metrics[f'isolation_{i}'] for i in range(3))
metrics['phantom_metric'] = 42  # red herring

# Real computation begins here — nested logic with distractors

def compute_robustness(data_dict):
    stab = data_dict['total_stability']
    iso = data_dict['total_isolation']
    if stab > 10:
        return stab * 1.2 - iso * 0.8
    else:
        return stab * 0.9 + iso * 0.3

# Unused recursive function (decoy abstraction)
def recursive_dampen(x, depth=0):
    if depth >= 5 or x < 1:
        return x
    return 0.9 * recursive_dampen(x, depth + 1)

# Another distraction: pairwise combinations that go nowhere
useless_pairs = list(itertools.combinations([1, 2, 3, 4], 2))
expanded_grid = list(itertools.product([0, 1], repeat=3))

# Real evaluation logic hidden among noise
def evaluate_performance(metrs, base):
    # Extract relevant values
    stability = metrs['total_stability']
    isolation = metrs['total_isolation']

    # Simulated gain factors
    alpha = base['threshold_a'] * 100  # 65
    beta = base['threshold_b'] * 50    # 37.5

    # Core formula disguised in distractions
    temp_score = 0
    for i in range(2):
        if i == 0:
            temp_score += stability * alpha
        else:
            temp_score += isolation * beta * 2  # double weight on isolation component

    # Additional adjustment based on pattern density
    total_bits = sum(sum(s) for s in telemetry_streams)
    density_factor = total_bits / 30.0  # 24 / 30 = 0.8

    intermediate = temp_score * density_factor

    # Final nonlinear scaling
    final = int(intermediate - (isolation * 10))  # subtract penalty

    # Dead branch (never taken due to data)
    if metrs.get('phantom_metric') == 99:
        final = int(final * 0.5)

    return final

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output result as required
print(f"Result: {final_score}")