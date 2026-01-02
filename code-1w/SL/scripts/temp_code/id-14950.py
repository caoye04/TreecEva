from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_quantum_state(state):
    return sum([abs(s)**2 for s in state])

# Unused transformation function
def transform_coordinates(coords):
    return [c * math.pi for c in coords]

# Misleading data structure
class DataProfile:
    def __init__(self, name):
        self.name = name
        self.metrics = defaultdict(int)
        self.flags = [False] * 10

# Real processing begins here
def compute_baseline(x):
    if x < 10:
        return x ** 2
    else:
        return int(math.sqrt(x))

def extract_features(raw_data):
    features = []
    for item in raw_data:
        if item % 3 == 0 and item > 0:
            features.append(item)
    # Slice only relevant portion
    return features[::2]  # Every other qualifying element

def calculate_entropy(values):
    count = Counter(values)
    total = len(values)
    entropy = 0.0
    for v in count.values():
        p = v / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)

def normalize_weights(ws):
    total = sum(ws)
    return [w / total for w in ws]

def filter_outliers(arr):
    # Simple outlier removal using IQR concept
    sorted_vals = sorted(arr)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [x for x in arr if lower <= x <= upper]

def validate_integrity(trace_log):
    # Dummy validation with side effect
    cumulative = 0
    for entry in trace_log:
        if isinstance(entry, dict) and 'code' in entry:
            cumulative ^= entry['code']
    return cumulative == 0

def process_metrics(data, weights):
    # Step 1: Extract qualifying features
    extracted = extract_features(data)
    
    # Step 2: Compute baselines for each
    baselines = [compute_baseline(e) for e in extracted]
    
    # Step 3: Normalize weights
    norm_weights = normalize_weights(weights)
    
    # Step 4: Filter outliers from baselines
    clean_baselines = filter_outliers(baselines)
    
    # Step 5: Calculate interaction score
    interaction = 0
    for i in range(len(clean_baselines) - 1):
        interaction += clean_baselines[i] * clean_baselines[i+1]
    
    # Step 6: Add entropy bonus
    entropy_bonus = calculate_entropy(clean_baselines)
    
    # Step 7: Apply weight modulation
    modulated = 0
    for i, val in enumerate(clean_baselines):
        modulated += val * norm_weights[i % len(norm_weights)]
    
    # Step 8: Final score computation
    final_score = int(modulated + interaction + entropy_bonus * 100)
    
    # Dead code path - never executed but looks relevant
    if False:
        profile = DataProfile('debug')
        for v in clean_baselines:
            profile.metrics[v] += 1
        validate_integrity([{'code': 42}, {'code': 17}])
    
    return final_score

# Irrelevant global variables
global_offset = 37
tracking_id = "TK-9912"
quantum_signature = [0.5+0.3j, 0.1-0.7j]

# Input data (meaningful values)
data = [24, -5, 18, 0, 12, 9, 36, 7, 3]
weights = [5, 3, 8, 2]

# Execution point of interest
final_score = process_metrics(data, weights)

# Output result as required
print(f"Result: {final_score}")