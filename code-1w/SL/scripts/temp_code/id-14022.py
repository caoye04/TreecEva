def analyze_pattern(sequence):
    """Irrelevant helper that analyzes repeating patterns (dead code path)"""
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            count += 1
    return count

# Distractor: unused complex structure
task_ranks = {'alpha': 3, 'beta': 1, 'gamma': 4, 'delta': 1, 'epsilon': 5}
sorted_tasks = sorted(task_ranks.items(), key=lambda x: x[1])

# Real data pipeline starts here
def transform_entries(entries):
    result = []
    for idx, val in enumerate(entries):
        if idx % 2 == 0:
            result.append(val * 1.5)
        else:
            result.append(val * 0.8)
    return result

def compute_baseline(items):
    total = 0
    for item in items[:len(items)//2]:  # Only first half
        total += item ** 0.5
    return total / len(items)  # Smoothing factor

# Misleading intermediate function
def estimate_load(x):
    acc = 0
    for i in range(1, x + 1):
        acc += i % 7
    return acc // 3

# Core logic with slicing and zip
measurements = [16, 25, 36, 49, 64, 81]
bias_vector = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1]

scaled = [m ** 0.5 for m in measurements]  # Square roots: [4, 5, 6, 7, 8, 9]
adjusted = [s + b for s, b in zip(scaled, bias_vector)]

# Apply transformation on every other element using slicing
processed = transform_entries(adjusted[::2])  # Operate on indices 0,2,4

# Decoy list comprehension with no downstream use
dummy_grid = [[i*j for j in range(3)] for i in range(3)]

# Weight assignment with red herring keys
weights = {
    'base': 0.4,
    'trend': 0.35,
    'outlier_penalty': -0.1,  # Not used
    'normalization': 1.0
}

data = {
    'readings': processed,
    'baseline': compute_baseline(adjusted),
    'offset': sum(bias_vector) / len(bias_vector)
}

# Another distraction: recursive bit counting (unused)
def count_set_bits(n):
    return 1 + count_set_bits(n & (n-1)) if n else 0

# Main processing function
def process_metrics(d, w):
    readings = d['readings']
    base_contrib = sum(readings) * w['base']
    
    trend_line = 0
    for i in range(1, len(readings)):
        trend_line += readings[i] - readings[i-1]
    trend_contrib = trend_line * w['trend']
    
    norm_factor = w['normalization']
    offset_adj = d['offset'] * 0.2
    
    # Final computation
    raw_score = base_contrib + trend_contrib + offset_adj
    smoothing = d['baseline'] * 0.5
    final_score = (raw_score - smoothing) * norm_factor
    
    # Irrelevant conditional branch (does not affect final_score)
    if len(readings) > 10:
        extra = 0
        for _ in range(10):
            extra += estimate_load(5)
        final_score += extra
    
    return final_score

# Critical execution point
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")