import math

# Simulated sensor array diagnostics with noise filtering and signal validation

def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 31, 88, 142]
    noise_floor = 30
    adjusted = [x - noise_floor for x in raw_readings if x > noise_floor]
    return adjusted


def validate_signal_quality(signal):
    if len(signal) == 0:
        return False
    peak = max(signal)
    avg = sum(signal) / len(signal)
    quality_index = (avg / peak) * 100
    return quality_index > 40


def apply_calibration(readings):
    calibrated = []
    for val in readings:
        if val < 100:
            calibrated.append(val * 1.2)
        elif val < 150:
            calibrated.append(val * 1.1)
        else:
            calibrated.append(val * 0.95)
    return [round(c, 2) for c in calibrated]


def generate_diagnostics_report(data):
    # Irrelevant diagnostic metrics (distractors)
    entropy_approx = 0.0
    total_energy = sum([x**2 for x in data])
    sample_count = len(data)
    fluctuation_index = max(data) - min(data)
    
    # Fake subsystem check (dead code path)
    if False:
        for i in range(len(data)):
            data[i] = int(math.sin(data[i]) * 100)
        
    # Unused transformation
    normalized = [x / max(data) for x in data] if data else [0]
    
    # Red herring calculation
    checksum = sum([data[i] * (i + 1) for i in range(len(data))]) % 97
    
    # Real metric used later
    median_val = sorted(data)[len(data)//2]
    
    return {
        'total_energy': total_energy,
        'fluctuation_index': fluctuation_index,
        'median_val': median_val,
        'checksum': checksum,
        'size': sample_count
    }


def analyze_readings(signals):
    if not signals:
        return -1
    
    # Misleading intermediate processing
    squared_sum = sum([s**2 for s in signals])
    inverse_sum = sum([1/s for s in signals if s != 0])
    harmonic_mean = len(signals) / inverse_sum if inverse_sum else 0
    
    # Distractor: unused statistical measures
    variance_proxy = sum([(s - harmonic_mean)**2 for s in signals]) / len(signals) if signals else 0
    skew_attempt = sum([(s - harmonic_mean)**3 for s in signals]) / (len(signals) * (variance_proxy**1.5)) if variance_proxy else 0
    
    # Critical path begins here
    report = generate_diagnostics_report(signals)
    med = report['median_val']
    energy = report['total_energy']
    size_factor = report['size']
    
    # Decoy logic with misleading variable names
    temp_score = med * 0.7 + (energy / 100) * 0.3
    adjustment_curve = [math.cos(i * 0.5) for i in range(5)]
    fake_threshold = sum(adjustment_curve) / 2
    
    # Actual computation chain
    base_rating = med * size_factor
    penalty = 0
    if energy < 5000:
        penalty += 15
    if size_factor < 5:
        penalty += 10
    
    # Final aggregation using non-obvious combination
    final_score = base_rating - penalty
    secondary_boost = int(math.sqrt(energy) // 10) if energy > 0 else 0
    final_diagnostic = final_score + secondary_boost
    
    # Dead assignment - no effect
    final_diagnostic = final_diagnostic  # redundant but confusing
    
    return int(final_diagnostic)

# Main execution flow
raw_signals = collect_sensor_data()
valid = validate_signal_quality(raw_signals)

# Spurious data transformation (not used in final path)
if valid:
    enhanced = [x * 1.05 for x in raw_signals]
    processed_signals = apply_calibration(raw_signals)
else:
    processed_signals = [0]

# More irrelevant pre-checks
consistency_check = all([x > y for x, y in zip(processed_signals, processed_signals[1:])]) or len(processed_signals) < 2

# Another decoy function call with side effects that don't matter
redundant_analysis = generate_diagnostics_report(enhanced if 'enhanced' in locals() else raw_signals)

# Key statement
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")