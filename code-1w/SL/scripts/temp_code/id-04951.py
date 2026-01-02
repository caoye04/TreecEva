from collections import defaultdict, Counter
import math

# Irrelevant helper function (dead code path)
def analyze_traffic(patterns):
    frequency = defaultdict(int)
    for p in patterns:
        frequency[p] += 1
    return dict(frequency)

# Misleading performance scorer (not used in final calculation)
def legacy_scorer(values):
    base = sum(v ** 0.5 for v in values if v > 0)
    penalty = len([v for v in values if v < 5])
    return round(base - penalty * 1.5, 2)

# Core logic disguised among distractors
def normalize_vector(vec):
    magnitude = math.sqrt(sum(x ** 2 for x in vec))
    return [round(x / magnitude, 6) for x in vec] if magnitude else vec

def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

# Decoy data structure (looks important but unused)
system_logs = [
    {'event': 'init', 'time': 100, 'status': 1},
    {'event': 'ping', 'time': 105, 'status': 0},
    {'event': 'sync', 'time': 112, 'status': 1}
]

# Red herring variables
temp_buffer = [i * 1.5 for i in range(10)]
scaling_factor = 2.718
dummy_matrix = [[0 for _ in range(5)] for _ in range(3)]

# Actual relevant data
raw_metrics = [88, 92, 76, 94, 85, 90, 83]

# Simulated preprocessing with distraction
def preprocess(metrics):
    shifted = [m - 70 for m in metrics]  # Normalize base
    filtered = [s for s in shifted if s > 10]  # Remove low values
    
    # Distracting transformation
    transformed = list(map(lambda x: x + math.sin(math.pi * x / 10), filtered))
    
    # Real operation embedded
    return [int(t) for t in transformed]

# Key evaluation function
def evaluate_performance(data):
    # Step 1: Preprocess
    processed = preprocess(data)
    
    # Step 2: Compute weighted components
    avg = sum(processed) / len(processed)
    
    # Step 3: Apply conditional bonus
    bonus = 0
    if len(processed) >= 5:
        bonus += 10
    if avg > 20:
        bonus += 5
    
    # Step 4: Use entropy as diversity penalty
    rounded = [int(p) for p in processed]
    entropy = compute_entropy(rounded)
    penalty = int(entropy * 2)
    
    # Step 5: Assemble score
    base_score = int(avg * 1.3)
    adjusted = base_score + bonus - penalty
    
    # Step 6: Final nonlinear adjustment
    final = int(adjusted * (1 + 0.1 * math.log(len(data))))
    
    # Irrelevant side computation (misleads traceability)
    noise_level = sum(1 for r in rounded if r % 2 == 0)
    threshold_check = any(n > 25 for n in processed)
    
    return final

# Unused but plausible alternate pathway
def fallback_analysis(seq):
    rev = seq[::-1]
    return sum(rev[i] * (0.9 ** i) for i in range(len(rev)))

# Main execution flow
metric_data = raw_metrics.copy()

# Critical assignment point
final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")