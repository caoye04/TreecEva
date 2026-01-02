import math

# Simulated sensor fusion system for environmental monitoring

def collect_readings():
    raw_signals = [127, 255, 192, 64, 80]
    noise_floor = 12.5
    adjusted = [sig - 32 for sig in raw_signals]
    return adjusted

# Irrelevant signal smoothing (dead path)
def smooth_signal(data):
    smoothed = []
    for i in range(len(data)):
        left = data[i-1] if i > 0 else data[i]
        right = data[i+1] if i < len(data)-1 else data[i]
        avg = (left + data[i] + right) / 3
        smoothed.append(avg)
    return smoothed

# Distraction: unused calibration function
def calibrate_sensors(baseline):
    factors = {}
    for i, val in enumerate(baseline):
        factors[f'sensor_{i}'] = round(math.log(val + 1) / (i + 0.5), 3) if val > 0 else 0.0
    return factors

# Real processing begins here
def preprocess(readings):
    scaled = [r * 1.25 for r in readings]
    clipped = [min(max(r, 50), 200) for r in scaled]
    return clipped

# Conditional transformation based on thresholds
def classify_reading(value, low, high):
    if value < low:
        return 'LOW'
    elif value > high:
        return 'HIGH'
    else:
        return 'NORMAL'

# Distractor: complex but unused frequency analysis
def spectral_analysis(signal_seq):
    magnitude = 0
    for i in range(len(signal_seq)):
        angle = signal_seq[i] * math.pi / 180
        harmonic = math.sin(angle) + 0.5 * math.cos(2*angle)
        magnitude += abs(harmonic)
    spectral_index = magnitude / len(signal_seq)
    categories = ['STABLE', 'MODERATE', 'VOLATILE']
    return categories[int(min(magnitude // 10, 2))]

# Main processing with list comprehension and nesting
def process_diagnostics(data):
    status_map = {}
    levels = [(50, 75), (75, 100), (100, 150), (150, 200)]
    
    for i, val in enumerate(data):
        # Nested logic with red herring computations
        temp_flag = False
        debug_score = 0
        for j, (low, high) in enumerate(levels):
            if val == low:
                debug_score += 1
            if val == high:
                debug_score += 2
            if low <= val < high:
                category = f'BAND_{j}'
                if val > 80 and j != 0:
                    temp_flag = True
                break
        else:
            category = 'BAND_4'
        
        # Real assignment path
        status_map[f'node_{i}'] = {
            'value': val,
            'class': category,
            'flagged': temp_flag
        }
        
        # Dead computation with decoy accumulation
        accumulator = 0
        for x in range(1, int(val // 10)):
            if x % 3 == 0:
                accumulator += x * 0.75

    return status_map

# Core analysis function with recursion and dictionary reduction
def recursive_evaluate(nodes, index=0, acc=None):
    if acc is None:
        acc = {'total': 0, 'alerts': 0}
    
    if index >= len(nodes):
        return acc
    
    node_key = f'node_{index}'
    if node_key not in nodes:
        return recursive_evaluate(nodes, index + 1, acc)
    
    value = nodes[node_key]['value']
    flagged = nodes[node_key]['flagged']
    
    # Relevant scoring logic
    base_score = math.sqrt(value) * 1.5
    if flagged:
        base_score *= 1.8
    
    acc['total'] += base_score
    if value > 140 or flagged:
        acc['alerts'] += 1
    
    return recursive_evaluate(nodes, index + 1, acc)

# Final decision logic with conditional expressions
def analyze_readings(diag_map, thresholds):
    result_set = []
    for k, v in diag_map.items():
        val = v['value']
        # Complex condition with misleading intermediate
        surrogate = val * 0.87 if val < thresholds['mid'] else val * 0.92
        adjustment = 1.1 if v['flagged'] else 0.95
        adjusted_val = surrogate * adjustment
        result_set.append(adjusted_val)
    
    # Critical distractor: elaborate but unused clustering
    clusters = {'A': [], 'B': [], 'C': []}
    for res in result_set:
        if res < 80:
            clusters['A'].append(res)
        elif res < 120:
            clusters['B'].append(res)
        else:
            clusters['C'].append(res)
    
    # Actual final calculation
    primary_metric = sum(result_set) / len(result_set)
    secondary_metric = len([x for x in result_set if x > 100])
    
    # Final diagnostic computed from multiple steps
    final_score = primary_metric * (1 + 0.1 * secondary_metric)
    
    # Decoy normalization (unused)
    normalized = final_score
    for _ in range(3):
        normalized = normalized / (1 + math.exp(-normalized * 0.01))
    
    return int(round(final_score))

# Orchestration with irrelevant setup
if __name__ == '__main__':
    # Unused baseline references
    reference_grid = [[1,2],[3,4]]
    metadata_log = {'version': '2.1', 'nodes': 5}
    
    # Real execution path
    raw = collect_readings()
    processed_data = preprocess(raw)
    
    # Build threshold map (used later)
    threshold_map = {
        'low': 60,
        'mid': 100,
        'high': 180
    }
    
    # Generate detailed diagnostics
    diagnostic_nodes = process_diagnostics(processed_data)
    
    # Perform recursive evaluation (intermediate result)
    summary_stats = recursive_evaluate(diagnostic_nodes)
    
    # Final analysis
    final_diagnostic = analyze_readings(diagnostic_nodes, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")