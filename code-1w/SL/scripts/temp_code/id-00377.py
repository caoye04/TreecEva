import math

# System health monitoring simulation with red herrings
def analyze_signal_strength(signal_data, noise_floor):
    peak = max(signal_data)
    avg = sum(signal_data) / len(signal_data)
    snr = (avg - noise_floor) * 1.5  # irrelevant calculation
    return peak > 75

# Irrelevant helper for thermal analysis
def compute_thermal_gradient(temps):
    gradient = 0
    for i in range(1, len(temps)):
        gradient += abs(temps[i] - temps[i-1])
    avg_grad = gradient / (len(temps) - 1) if len(temps) > 1 else 0
    threshold_breach = any(t > 82 for t in temps)
    return avg_grad, threshold_breach

# Core diagnostic engine
def generate_baseline_readings(count):
    readings = []
    for i in range(count):
        val = (i * i + 3 * i + 7) % 100
        readings.append(val)
    return readings

def filter_anomalies(logs, limit=50):
    clean_logs = [x for x in logs if x % 2 == 1]  # keep only odd
    excess_data = [x for x in logs if x > limit]   # distractor list
    return clean_logs

def aggregate_metrics(items):
    total = sum(items)
    mid_val = items[len(items)//2]
    product = 1
    for x in items:
        product *= (x % 7 + 1)  # misleading computation
    return total, mid_val

def apply_calibration(sequence, factor=0.93):
    calibrated = [int(x * factor) for x in sequence]
    return [x if x % 2 == 0 else x + 1 for x in calibrated]  # make even

# Set operations to determine compatibility flags
def compute_compatibility_layers(active_modules):
    required = {'sensor_hub', 'io_controller', 'power_manager'}
    optional = {'display_driver', 'audio_subsystem', 'network_stack', 'debug_interface'}
    available = set(active_modules)
    missing_req = required - available
    opt_count = len(available & optional)
    return len(missing_req) == 0, opt_count

# Main evaluation logic
def evaluate_thresholds(diagnostics, state):
    critical_failures = 0

    # Extract key metrics
    raw_total, median_val = aggregate_metrics(diagnostics)
    adjusted_diagnostics = apply_calibration(diagnostics)
    enhanced_total = sum(adjusted_diagnostics)

    # Boolean logic chain with short-circuiting
    base_condition = raw_total > 200
    adjustment_factor = 1.1 if base_condition and len(diagnostics) >= 8 else 0.9
    
    temp_sequence = [76, 79, 81, 77, 83]
    _, thermal_breach = compute_thermal_gradient(temp_sequence)

    # Irrelevant signal analysis
    signal_data = [68, 72, 78, 85, 91, 95]
    signal_ok = analyze_signal_strength(signal_data, noise_floor=20)

    # Bitwise manipulation for status encoding (distractor)
    status_word = 0
    for d in diagnostics[:4]:
        status_word ^= d
        status_word = (status_word << 1) & 0xFF

    # Real decision logic
    meets_power = state['voltage'] >= 3.3
    modules_active = state['modules']
    has_full_support, extra_features = compute_compatibility_layers(modules_active)

    # Lambda-based filtering (required Python feature)
    severity_filter = lambda x: x > 60
    high_severity_count = len(list(filter(severity_filter, diagnostics)))

    # Core logic path
    if meets_power and has_full_support:
        if high_severity_count >= 3:
            critical_failures += 2
        elif median_val < 40:
            critical_failures += 1
    else:
        critical_failures += 3

    # Final composite score (distraction)
    composite_score = (raw_total * adjustment_factor + extra_features * 10) / (critical_failures + 1)

    # Key logic step - this is the actual answer
    fallback_modes = state.get('redundancy', []).count('active')
    safe_margin = 10 if fallback_modes > 1 else 5
    final_diagnostic = int((enhanced_total // 10) % 100) + safe_margin

    return final_diagnostic

# Simulated system input
def main():
    # Generate baseline data
    diagnostics = generate_baseline_readings(10)
    
    # Add filtered anomalies (some data loss)
    raw_logs = [23, 84, 15, 76, 93, 44, 18, 89]
    cleaned = filter_anomalies(raw_logs)
    
    # Augment diagnostics with cleaned logs
    for x in cleaned:
        diagnostics.append(x)
    
    # System state with realistic structure
    system_state = {
        'voltage': 3.45,
        'modules': ['sensor_hub', 'io_controller', 'power_manager', 'display_driver', 'network_stack'],
        'redundancy': ['standby', 'active', 'active'],
        'firmware': 'v2.3.1'
    }
    
    # Unused intermediate computations (distractors)
    total_energy = sum(diagnostics) * system_state['voltage']
    entropy_approx = math.log(len(diagnostics)) * 2.3
    
    # Execute key statement
    final_diagnostic = evaluate_thresholds(diagnostics, system_state)
    
    # Output result
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()