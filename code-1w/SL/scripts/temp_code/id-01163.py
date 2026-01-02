import math

# Simulated sensor data and configuration
def generate_signals():
    base_freq = 7
    time_points = [t * 0.1 for t in range(100)]
    signal_a = [math.sin(base_freq * t) + 0.5 * math.cos(3 * t) for t in time_points]
    signal_b = [math.cos(base_freq * t) - 0.3 * math.sin(5 * t) for t in time_points]
    return {'A': signal_a, 'B': signal_b}

# Irrelevant helper - looks important but unused in critical path
def compute_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy

# Signal conditioning with red herring transformations
def preprocess(signal_dict):
    enhanced = {}
    stats_log = []
    
    for key, sig in signal_dict.items():
        # Real preprocessing step
        filtered = [x * 0.8 + 0.1 for x in sig]  # damping and offset
        squared_energy = sum(x**2 for x in filtered[:50])  # distraction metric
        
        # Distractor: complex transformation not used later
        fft_approx = []
        for i in range(8):
            comp = sum(filtered[j] * (math.cos(2 * math.pi * i * j / 8) for j in range(8)))
            fft_approx.append(round(comp, 3))
        
        # Only this line matters
        enhanced[key] = [round(x, 4) for x in filtered]
        
        # Dead code - collected but never used
        stats_log.append({
            'chan': key,
            'energy': squared_energy,
            'peaks': len([x for x in filtered if x > 0.5]),
            'fft_peak': max(fft_approx, default=0)
        })
    
    return enhanced

# Threshold mapping with decoy logic
def build_thresholds(channels, mode='strict'):
    # Real threshold values
    thresholds = {ch: 0.45 + i * 0.05 for i, ch in enumerate(channels)}
    
    # Misleading dynamic adjustment (never invoked)
    def adaptive_tune(x):
        return x * math.exp(-0.1 * x)
    
    # Fake calibration sequence
    calibration_matrix = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i == j:
                calibration_matrix[i][j] = 1.1
            elif i == j + 1:
                calibration_matrix[i][j] = -0.05
    
    # Only this mutation affects outcome
    if 'C' not in channels:
        thresholds['B'] = 0.62  # critical override
    
    return thresholds

# Core analysis with distractor-heavy logic
def analyze_signal(data, thresholds):
    results = {}
    summary_report = []
    
    # Key variables
    active_segments = {k: [] for k in data.keys()}
    transient_count = 0
    
    for chan, readings in data.items():
        above_thresh = 0
        cross_events = 0
        last_state = False
        
        for val in readings:
            current = val > thresholds.get(chan, 0.5)
            
            # Edge detection - real logic
            if current and not last_state:
                cross_events += 1
            
            if val > thresholds.get(chan, 0.5):
                above_thresh += 1
                
            # Distraction counter
            if -0.1 < val < 0.1:
                transient_count += 1
            
            last_state = current
        
        # Only this derived metric is used downstream
        results[chan] = round(above_thresh / len(readings), 3)
        
        # Dead structure assembly
        summary_report.append({
            'channel': chan,
            'activation_ratio': results[chan],
            'transitions': cross_events,
            'zero_crossings': transient_count,
            'data_integrity': 'OK' if len(readings) == 100 else 'ERROR'
        })
    
    # Complex-looking but irrelevant final aggregation
    weights = {'A': 1.0, 'B': 1.2}
    weighted_sum = sum(results.get(k, 0) * weights.get(k, 1.0) for k in ['A', 'B'])
    penalty_factor = 0.9 if transient_count > 15 else 1.0
    
    # The actual answer is computed here through a list comprehension and lambda
    diagnostic_scores = [scores for scores in results.values()]
    score_mapper = lambda s: int(s * 1000)  # maps 0.xxx to integer
    mapped_diagnostics = list(map(score_mapper, diagnostic_scores))
    
    # Final computation - only this matters
    final_diagnostic = sum(mapped_diagnostics) * 2 - 50
    
    # Never-printed debug
    debug_snapshot = {
        'raw_scores': diagnostic_scores,
        'mapped': mapped_diagnostics,
        'weighted': weighted_sum,
        'penalty': penalty_factor,
        'final_raw': final_diagnostic
    }
    
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    # Step 1: Generate raw signals
    raw_data = generate_signals()
    
    # Step 2: Preprocess signals (distractions included)
    processed_data = preprocess(raw_data)
    
    # Step 3: Build threshold map with decoy calibration
    channel_list = list(processed_data.keys())
    threshold_map = build_thresholds(channel_list, mode='strict')
    
    # Step 4: Analyze signal - target execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")