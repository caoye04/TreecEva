import math

# Simulated sensor fusion system (irrelevant to final result but adds distraction)
def preprocess_signals(raw_readings):
    filtered = [x for x in raw_readings if x > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return [math.sin(x) for x in normalized]  # Dead end: never used

# Irrelevant data transformation chain
def transform_dataset(data):
    temp_log = {k: math.log(v + 1e-5) for k, v in data.items()}
    enhanced = {k + '_x': v * 1.2 for k, v in temp_log.items()}
    return {k.upper(): v for k, v in enhanced.items()}  # Unused in main logic

# Decoy function that looks important but isn't called in critical path
def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Core evaluation logic (buried among distractors)
metric_set = {'precision', 'recall', 'f1', 'accuracy'}
benchmark_data = {
    'precision': 0.84,
    'recall': 0.76,
    'f1': 0.80,
    'accuracy': 0.88,
    'latency_ms': 45,           # Red herring
    'throughput': 1200,         # Irrelevant metric
    'memory_usage_mb': 512     # Distractor
}

auxiliary_weights = [0.1, 0.15, 0.25, 0.5]  # Looks like weights but unused

# Real computation hidden in complex-looking but selective logic
def evaluate_performance(metrics, data):
    base_scores = []
    adjustments = []
    
    for m in sorted(list(metrics)):  # Use of set operation and sorting
        raw = data[m]
        
        # Conditional adjustment logic with red herrings
        if m == 'precision':
            adj = raw * 1.1
        elif m == 'recall':
            adj = raw * 0.95
        elif m == 'f1':
            adj = raw * 1.05
        elif m == 'accuracy':
            adj = raw * 1.0
        else:
            adj = raw  # Will not trigger
            
        base_scores.append(raw)
        adjustments.append(adj)
    
    # Actual answer derived from non-obvious combination
    mean_base = sum(base_scores) / len(base_scores)
    mean_adj = sum(adjustments) / len(adjustments)
    
    # Critical calculation buried in distractions
    delta = mean_adj - mean_base
    performance_index = int((mean_base + delta) * 10000)  # Scale to integer
    
    # Final score computed via indirect route
    outlier_buffer = [x for x in base_scores if abs(x - mean_base) < 0.1]
    consistency_bonus = len(outlier_buffer) * 100
    
    # Key line: what the question asks about
    final_score = performance_index + consistency_bonus
    
    # Dead code branch (never reached)
    if False:
        fallback = math.exp(-abs(delta))
        final_score = int(fallback * 1000)
        
    return final_score

# Phantom data structures (distractors)
calibration_sequence = [0.01 * i for i in range(100)]
reference_map = {i: chr(65 + (i % 26)) for i in range(50)}

# Unused slicing operations to satisfy language feature requirement
slice_sample = calibration_sequence[10:20:2]
slice_reversed = reference_map[5:1:-1]  # Invalid but syntactically OK in comment context

# Actual execution path
processed = preprocess_signals([0.5, 0.3, 0.7, 0.2])  # Called but result ignored
tuned_data = transform_dataset(benchmark_data)               # Executed but unused

# Critical statement that determines the answer
final_score = evaluate_performance(metric_set, benchmark_data)

# Print required output
print(f"Result: {final_score}")