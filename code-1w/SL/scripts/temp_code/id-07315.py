import math

# Irrelevant helper function (dead code path)
def useless_transform(data):
    return [x ** 2 + 1 for x in data if x % 3 == 0]

# Unused complex lambda (distractor)
stealth_op = lambda z: sum([math.sin(i) for i in range(len(z))])

# Real baseline constants
baseline = {
    'threshold': 42,
    'weight_a': 0.6,
    'weight_b': 0.4,
    'penalty_factor': 1.5
}

# Simulated metrics with red herring fields
metrics = {
    'accuracy': 89.2,
    'precision': 76.4,
    'recall': 82.1,
    'f1_score': 79.3,
    'complexity_index': 127,  # misleading metric
    'data_volume': 1500,
    'noise_ratio': 0.07,
    'execution_time_ms': 234,
    'deprecated_flag': True  # irrelevant flag
}

# Fake scoring function that looks important but isn't used
def legacy_scorer(x):
    temp = 0
    for i in range(1, int(x['accuracy']) + 1):
        if i % 7 == 0:
            temp += math.sqrt(i)
    return temp // 3

# Another decoy: unused list comprehension with side effects avoided
decoys = [math.log(abs(metrics['noise_ratio'] - 0.1) + 1e-5) for _ in range(5)]

# Core logic buried among distractions
def adjust_for_volume(volume):
    if volume < 100:
        return 0.8
    elif volume < 500:
        return 1.0
    else:
        return 1.1  # bonus for large data

# Bit manipulation distractor (no real impact)
cursed_value = 0b110101
for _ in range(3):
    cursed_value = ((cursed_value << 3) & 0xFF) | (cursed_value >> 5)

# Hidden key transformation using lambda and conditional expression
refinement = lambda f1: f1 * (1.05 if f1 > 75 else 1.0)

# Conditional adjustment based on multiple factors (real logic starts here)
base_performance = (metrics['accuracy'] * baseline['weight_a'] + 
                    metrics['f1_score'] * baseline['weight_b'])

adjusted_perf = base_performance * adjust_for_volume(metrics['data_volume'])

# Apply refinement only if recall is sufficient
if metrics['recall'] > baseline['threshold']:
    adjusted_perf = refinement(adjusted_perf)

# Penalty for high noise ratio
if metrics['noise_ratio'] > 0.05:
    adjusted_perf -= baseline['penalty_factor'] * 10

# Decoy calculation that mimics the real one
phantom_score = (metrics['precision'] * 0.5 + metrics['accuracy'] * 0.5) * 0.9
phantom_score = round(phantom_score, 2)  # looks meaningful but unused

# Real final computation buried after distractions
def evaluate_performance(m, b):
    score = adjusted_perf  # uses outer-scope computed value
    if m['execution_time_ms'] > 200:
        score *= 0.95
    if m['deprecated_flag']:
        # This looks like it should hurt, but doesn't due to context
        pass  
    return int(round(score))

# Key statement
final_score = evaluate_performance(metrics, baseline)

# Output result as required
print(f"Target result: {final_score}")