import math

# Simulated biomedical signal processing pipeline
def analyze_waveform(signal):
    if not signal:
        return 0
    peak = max(signal)
    baseline = sum(signal) / len(signal)
    amplitude = peak - baseline
    # Irrelevant transformation (distractor)
    normalized = [math.sin(x / 10) for x in signal]
    return amplitude

# Red herring function - looks important but unused in final calculation
def compute_envelope(data):
    envelope = []
    for i in range(1, len(data)-1):
        env_val = (data[i-1] + data[i] + data[i+1]) / 3
        envelope.append(math.log(env_val + 1))
    return envelope

# Auxiliary diagnostic filter (partially used)
def apply_filter(values, mode='lowpass'):
    if mode == 'lowpass':
        return [v * 0.9 for v in values]
    elif mode == 'highpass':
        return [v * 1.1 for v in values]
    else:
        return values

# Core metric processor with conditional logic and list comprehension
def evaluate_stability(readings):
    filtered = apply_filter(readings)
    deviations = [abs(r - 70) for r in filtered]  # Assume nominal level is 70
    # Early return red herring
    if len(deviations) < 5:
        temp_score = sum(deviations) * 0.5
        adjustment = math.tanh(temp_score / 100)
        return adjustment  # Dead end in this context
    avg_dev = sum(deviations) / len(deviations)
    # Complex conditional expression (required feature)
    risk_factor = 2.5 if avg_dev > 15 else (1.8 if avg_dev > 10 else (1.0 if avg_dev > 5 else 0.5))
    return avg_dev * risk_factor

# Main processing function combining multiple concepts
def process_metrics(data, limits):
    # Destructuring assignment (required concept)
    heart_rate, oxygen_levels, neural_activity = data
    
    # Bit manipulation decoy (irrelevant to final result)
    status_flag = 0b1010
    debug_mode = status_flag & 0b0100
    if debug_mode:
        mask_result = status_flag ^ 0b1111
    
    # Real computation begins
    hr_diagnostic = analyze_waveform(heart_rate)
    
    # Conditional branch with misleading intermediate
    if hr_diagnostic > 25:
        severity = 3
        # Unused nested block (dead code path)
        calibration = [x >> 2 for x in oxygen_levels]  # Bit shift distractor
    else:
        severity = 1
    
    # List comprehension with filtering (required feature)
    critical_o2 = [val for val in oxygen_levels if val < limits['o2_min']]
    o2_penalty = len(critical_o2) * 2.5
    
    # Boolean logic chain with short-circuit evaluation
    is_critical = len(critical_o2) > 3 or (severity == 3 and hr_diagnostic > 30)
    override_safety = False and is_critical  # Deliberately false, distractor
    
    # Neural feedback loop simulation (complex data transformation)
    feedback_gain = 1.0
    for step in range(3):
        feedback_gain *= 0.85
        # Decoy mutation
        neural_snapshot = [n ^ int(feedback_gain * 10) for n in neural_activity]  # XOR distractor
    
    # Primary stability evaluation (contributes to answer)
    stability_metric = evaluate_stability(neural_activity)
    
    # Final fusion formula (answer depends on this)
    base_score = hr_diagnostic * 1.2
    penalty_adjusted = o2_penalty * severity
    final_diagnostic = base_score - penalty_adjusted + (stability_metric / 2)
    
    # Multiple assignments that don't affect outcome
    summary_stats = (base_score, penalty_adjusted)
    report_status, validation_code = 'final', 200
    
    return final_diagnostic

# Simulated input data
health_data = (
    [68, 72, 65, 80, 70, 60, 85],           # heart rate waveform
    [96, 94, 92, 98, 90, 89, 95, 91, 88],    # oxygen levels
    [70, 71, 69, 72, 68, 73, 70, 71, 69]     # neural readings
)

# Threshold configuration
thresholds = {
    'o2_min': 90,
    'hr_max': 100,
    'neural_baseline': 70
}

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")