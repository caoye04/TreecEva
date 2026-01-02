from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings and complex logic paths
def preprocess_sensors(raw_readings):
    processed = []
    noise_floor = 0.041
    for val in raw_readings:
        if abs(val) < noise_floor:
            processed.append(0)
        else:
            processed.append(round(val ** 2 + 0.1, 4))
    return processed

def generate_key(signal, mask):
    # Irrelevant transformation - decoy function
    return [s ^ mask for i, s in enumerate(signal)]

def evaluate_stability(readings):
    stability_score = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            stability_score += 1
        elif readings[i] < readings[i-1]:
            stability_score -= 0.5
    return round(stability_score, 3)

def build_logic_grid(timestamps, values):
    grid = defaultdict(lambda: 0)
    for t, v in zip(timestamps, values):
        if t % 3 == 0:
            grid['A'] += v
        elif t % 5 == 0:
            grid['B'] += v * 0.5
        else:
            grid['C'] += v // 2
    return grid

def activate_filters(grid, threshold=3.0):
    flags = []
    temp_vals = []
    for k, v in grid.items():
        if v > threshold:
            flags.append(True)
            temp_vals.append(v * 1.2)
        else:
            flags.append(False)
            temp_vals.append(v * 0.8)
    
    # Dead code path - never used
    if sum(temp_vals) > 100:
        adjustment = sum(temp_vals) / 10
    else:
        adjustment = 0
        
    return flags

def compute_entropy(seq):
    # Distractor function - looks important but unused in final result
    count = Counter(seq)
    total = len(seq)
    entropy = 0
    for c in count.values():
        p = c / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just mimicry
    return round(entropy, 4)

def analyze_pattern(grid, act_seq):
    base = 0
    modifier = 1.5
    
    # Real computation begins
    if grid['A'] > 10:
        base += grid['A'] * 2
    if grid['B'] > 5:
        base += grid['B'] * 3
    
    # Critical logic step
    for i, flag in enumerate(act_seq):
        if flag and i % 2 == 0:
            base += 7
        elif not flag and i % 3 == 0:
            base -= 2
    
    # Final adjustment based on hidden rule
    if grid['C'] != 0 and len(act_seq) >= 4:
        base = int(base * modifier) + 5
    else:
        base = int(base)
        
    return base

# Main execution flow with distractions
if __name__ == '__main__':
    timestamps = [1, 3, 5, 6, 9, 10]
    raw_sensor_data = [2.1, -0.03, 4.5, 1.8, -0.02, 3.3]
    
    # Step 1: Process sensor data (some relevant, some ignored)
    cleaned = preprocess_sensors(raw_sensor_data)
    
    # Step 2: Generate irrelevant key
    encryption_key = generate_key([1, 0, 1], 255)
    
    # Step 3: Evaluate stability (decoy metric)
    stability_metric = evaluate_stability(cleaned)
    
    # Step 4: Build the real logic grid (core component)
    logic_grid = build_logic_grid(timestamps, cleaned)
    
    # Step 5: Activate filters to get activation sequence (partially relevant)
    activation_flags = activate_filters(logic_grid, threshold=4.0)
    
    # Step 6: Compute fake entropy (red herring)
    dummy_entropy = compute_entropy([1, 0, 1, 1, 0])
    
    # Step 7: Perform final diagnostic analysis (this uses logic_grid and activation_flags)
    final_diagnostic = analyze_pattern(logic_grid, activation_flags)
    
    # Print final answer as required
    print(f"Result: {final_diagnostic}")