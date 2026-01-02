import math

# Irrelevant helper function (decoy)
def analyze_sentiment(text):
    return sum(ord(c) for c in text) % 7

# Unused transformation map (red herring)
symbol_map = {
    'A': lambda x: x + 10,
    'B': lambda x: x * 2,
    'C': lambda x: x - 5
}

# Misleading intermediate computation (distractor)
baseline_adjustment = sum([i**2 for i in range(6)]) // 3
offset_cache = {i: baseline_adjustment * (i+1) for i in range(4)}

# Core data with mixed relevance
raw_input = [12, 15, 20, 8, 22]

# Weighting system involving dictionary and lambda
weights = {
    'base': 0.8,
    'bonus': lambda x: 0.1 if x > 15 else 0.05,
    'penalty': lambda x: 0.05 if x < 10 else 0.02
}

# Auxiliary state tracker (partly irrelevant)
status_flags = {'processed': 0, 'flagged': [], 'ignored': set()}

# Data preprocessing with red herrings
processed = []
for val in raw_input:
    temp = val
    if temp % 2 == 0:
        temp = (temp // 2) * 3  # Distraction: not used in final logic
    processed.append(temp + 1)

# Actual signal data extraction (critical path)
effective_values = [x for x in raw_input if x >= 12]

# Complex accumulator with multiple concepts
accumulator = 0
for i, v in enumerate(effective_values):
    w_base = weights['base']
    w_bonus = weights['bonus'](v)
    w_penalty = weights['penalty'](v)
    contribution = v * (w_base + w_bonus - w_penalty)
    accumulator += contribution

# Dummy aggregation using dictionary operations (misleading)
summary_stats = {
    'count': len(raw_input),
    'max': max(raw_input),
    'min': min(raw_input),
    'extra': sum(offset_cache.values()) / 4  # Irrelevant
}

# Simulated logging (dead code path)
log_entries = []
for item in raw_input:
    entry = f"Item:{item}"
    if item > 20:
        log_entries.append(entry + "|HIGH")
    # No further use of log_entries

# Key data structure for final processing
data = {
    'values': effective_values,
    'meta': {'version': '2.1', 'active': True}
}

# Main processing function with nested logic
def process_results(dataset, weight_config):
    values = dataset['values']
    total = 0.0
    scaling_factor = 1.1
    
    # Nested loop simulating multi-step reasoning
    for idx, num in enumerate(values):
        stage1 = num * weight_config['base']
        stage2 = stage1 + (num * weight_config['bonus'](num))
        stage3 = stage2 - (num * weight_config['penalty'](num))
        
        # Apply lambda-based adjustment
        adjust = (lambda x: x * 1.05 if x > 18 else x * 0.98)(stage3)
        total += adjust
    
    # Final nonlinear transformation
    result = math.floor(total * scaling_factor)
    
    # Dead branch with misleading comment
    if dataset['meta']['version'] == '9.9':
        result = result * 2  # Never executed
        
    return result

# Execute critical statement
final_score = process_results(data, weights)

# Output result as required
print(f"Target result: {final_score}")