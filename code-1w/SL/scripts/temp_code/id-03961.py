import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else x > 0

# Distractor: complex but unused data transformation
decoy_matrix = [[i * j + 2 for j in range(5)] for i in range(5)]
processed_noise = list(map(lambda row: [item ** 0.5 for item in row if item % 2 == 0], decoy_matrix))

# Real data pipeline begins
raw_signal = [1, -3, 4, -1, 5, -9, 2, -6]

# Step 1: Filter out negative values (distractor: absolute used later)
abs_values = [abs(x) for x in raw_signal]
enhanced_signal = [x for x in raw_signal if x > 0]

# Step 2: Apply exponential backoff scaling on enhanced signal
scaling_factor = 1.5
temp_scaled = []
for idx, val in enumerate(enhanced_signal):
    temp_scaled.append(val * (scaling_factor ** idx))

# Step 3: Misleading FFT-like operation (unused)
fft_simulated = [math.sin(x / 3.0) + math.cos(x / 4.0) for x in abs_values]
smoothed_fft = list(filter(lambda x: x > 0.5, fft_simulated))

# Step 4: Actual transformation using lambda and recursion
def recursive_weight(seq, n):
    if n <= 0:
        return 0
    return seq[n-1] + 0.5 * recursive_weight(seq, n-1)

transformed_data = []
for i in range(1, len(temp_scaled) + 1):
    segment = temp_scaled[:i]
    weight_fn = lambda s, k: k == 0 and 0 or s[k-1] + 0.25 * weight_fn(s, k-1)
    recursive_result = recursive_weight(segment, len(segment))
    transformed_data.append(round(recursive_result, 4))

# Step 5: Configuration with red herring parameters
config = {
    'threshold': 7.5,
    'mode': 'aggressive',
    'debug_trace': True,
    'history_cache': [recursive_weight([1,2],2), recursive_weight([3],1)], # irrelevant precomputations
    'version': '2.1-alpha'
}

# Step 6: Decoy sort operation (no effect on main logic)
sorted_decoy = sorted(transformed_data, key=lambda x: -x if x > 4 else x)

# Step 7: Main analysis function with early returns and branching
valid_count = 0
def analyze_pattern(data, cfg):
    global valid_count
    result = 0.0
    threshold = cfg['threshold']
    
    for idx, val in enumerate(data):
        # Simulated condition check with bit manipulation red herring
        flag = (idx + 1) & 3  # irrelevant bitwise
        
        if val < threshold:
            continue  # skip below-threshold values
            
        adjustment = 1.0
        if idx % 2 == 0:
            adjustment = 1.2
        elif idx > 2:
            adjustment = 0.8
            
        contribution = val * adjustment
        
        # Early termination red herring
        if contribution > 20:
            valid_count += 1  # counted but not used
            break
            
        result += contribution
    
    # Final nonlinear correction (key step)
    if result > 0:
        result = math.log(result + 10) * 2.5
    
    return round(result, 4)

# Step 8: Execute critical statement
final_diagnostic = analyze_pattern(transformed_data, config)

# Print result for evaluation
print(f"Target result: {final_diagnostic}")