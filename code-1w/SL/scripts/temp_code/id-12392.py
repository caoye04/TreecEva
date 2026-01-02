import math

# Simulated sensor signal processing with embedded logic chain
def preprocess_signals(raw_readings):
    filtered = []
    noise_floor = 0.041
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(val * 1.07)
    return filtered

# Irrelevant helper - decoy function (dead path)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed  # never used

# Signal envelope detection (distraction)
def compute_envelope(signal):
    envelope = []
    for x in signal:
        envelope.append(math.sqrt(x**2 + 0.1))
    return envelope

# Core analysis: pattern matching with state transitions
def detect_oscillatory_bursts(series, threshold):
    bursts = 0
    state = 'idle'
    count_in_burst = 0
    for idx, x in enumerate(series):
        if state == 'idle' and x > threshold:
            state = 'active'
            count_in_burst = 1
        elif state == 'active':
            if x > threshold / 2:
                count_in_burst += 1
            else:
                if count_in_burst >= 3:
                    bursts += 1
                state = 'idle'
                count_in_burst = 0
    if state == 'active' and count_in_burst >= 3:
        bursts += 1
    return bursts

# Frequency domain approximation (red herring)
def estimate_dominant_frequency(signal):
    N = len(signal)
    if N == 0:
        return 0.0
    power_max = 0.0
    best_freq = 0.0
    for k in range(1, N//4):
        re = im = 0.0
        for n, s in enumerate(signal):
            angle = 2 * math.pi * k * n / N
            re += s * math.cos(angle)
            im += s * math.sin(angle)
        power = re*re + im*im
        if power > power_max:
            power_max = power
            best_freq = k / N
    return best_freq  # computed but not used in final result

# Secondary metric: zero-crossing rate (distractor)
def calculate_zcr(signal):
    crossings = 0
    for i in range(1, len(signal)):
        if (signal[i-1] < 0 <= signal[i]) or (signal[i-1] > 0 >= signal[i]):
            crossings += 1
    return crossings / max(len(signal), 1)

# Main diagnostic logic with tuple unpacking and zip usage
def analyze_signal_patterns(data_list, limits):
    processed_chains = []
    diagnostics = []
    
    # Multiple assignment and list transformation
    for raw_seq, (low_thresh, high_thresh) in zip(data_list, limits):
        cleaned = preprocess_signals(raw_seq)
        
        # Dead code branch - misleading control flow
        if len(cleaned) == 0:
            envelope_feature = 0.0
            dominant_freq = 0.0
        else:
            # Real computation buried in distractions
            burst_count = detect_oscillatory_bursts(cleaned, high_thresh)
            
            # Decoy computations with intermediate results
            _envelope = compute_envelope(cleaned)
            _zcr = calculate_zcr(cleaned)
            _dom_freq = estimate_dominant_frequency(cleaned)
            
            # Critical calculation path
            magnitude_score = sum(abs(x) for x in cleaned) / len(cleaned)
            stability_index = magnitude_score / (1 + burst_count)
            
            # Linear search for anomaly (relevant logic)
            has_anomaly = False
            for val in cleaned:
                if val > 5.0 or val < -5.0:
                    has_anomaly = True
                    break
            
            # Tuple unpacking in loop (required idiom)
            temp_chain = [(i, x*0.91) for i, x in enumerate(cleaned)]
            processed_chains.extend(temp_chain)
            
            # Build diagnostic vector with irrelevant components
            diag_vector = (
                magnitude_score * 100,       # scaled irrelevant
                burst_count * 5,             # weighted burst feature
                int(has_anomaly),            # binary flag
                len(temp_chain),             # size metric
                stability_index * 200        # key component for final answer
            )
            diagnostics.append(diag_vector)
    
    # Final aggregation using destructuring and complex reduction
    total_impact = 0.0
    for d in diagnostics:
        score_part, burst_weight, anomaly_flag, size_norm, stability_scaled = d
        # Only stability_scaled contributes to final_diagnostic
        total_impact += stability_scaled
    
    # Final nonlinear transformation (answer derivation)
    adjustment_factor = 1.87
    if total_impact > 300:
        adjustment_factor = 1.23
    elif total_impact > 200:
        adjustment_factor = 1.54
    else:
        adjustment_factor = 1.87
    
    final_diagnostic = int(total_impact * adjustment_factor) + 17
    
    # Red herring variable - looks important but unused
    overall_coherence = len(processed_chains) / (1 + abs(total_impact - 250))
    
    return final_diagnostic

# Simulated multi-channel input data
channel_A = [-0.32, 0.15, 0.67, 1.21, 0.94, 1.83, 2.01, 1.76, 0.89, 1.02, 0.75]
channel_B = [0.05, -0.11, 0.43, 0.88, 1.32, 1.15, 0.92, 1.01, 0.77, 0.65]
channel_C = [0.21, 0.54, 1.63, 2.05, 1.91, 1.77, 1.22, 0.81, 0.63]

signal_data = [channel_A, channel_B, channel_C]
thresholds = [(0.25, 0.8), (0.25, 0.75), (0.25, 0.85)]

# Execute main analysis
final_diagnostic = analyze_signal_patterns(signal_data, thresholds)
print(f"Result: {final_diagnostic}")