from itertools import compress, cycle

def analyze_growth_cycles(data):
    # Irrelevant analysis - distractor
    moving_avg = []
    for i in range(2, len(data)):
        avg = (data[i-2] + data[i-1] + data[i]) / 3
        moving_avg.append(avg > 15)
    
    # Semi-relevant transformation
    filtered = [x for x in data if x > 10]
    return filtered

def calculate_optimal_yield(raw):
    # Core logic begins
    processed = [x * 1.5 for x in raw if x % 2 == 1]  # Only odd values scaled
    
    # Distractor: complex lambda with limited impact
    adjuster = lambda val, idx: val * 0.9 if idx % 3 == 0 else val
    adjusted = [adjuster(v, i) for i, v in enumerate(processed)]
    
    # Secondary filter that actually matters
    valid_yields = [y for y in adjusted if y < 30]
    
    # Accumulate using linear logic
    accumulator = 0
    for i, yield_val in enumerate(valid_yields):
        if i % 2 == 0:
            accumulator += yield_val
        else:
            accumulator -= yield_val // 2
    
    # Dummy state tracking (distraction)
    state_log = []
    for step in range(3):
        state_log.append(f'Stage {step}: idle')
    
    final_yield = int(accumulator)  # Key assignment point
    return final_yield

# Simulated sensor input - realistic domain context (agricultural yield prediction)
base_input = [12, 17, 22, 19, 14, 25, 8, 11]
mask_pattern = [True, False, True, True, False]

# Irrelevant pre-processing using itertools
extended_mask = list(compress(cycle(mask_pattern), range(len(base_input))))
dummy_filtered = [x for x, m in zip(base_input, extended_mask) if m]

# Actual data pipeline
harvest_data = analyze_growth_cycles(base_input)
final_yield = calculate_optimal_yield(harvest_data)
print(f"Result: {final_yield}")