def analyze_load_pattern(samples):
    # Filter peaks using slicing and lambda
    peak_filter = lambda x: x > 75
    peaks = [x for x in samples[::2] if peak_filter(x)]
    
    # Baseline computation from subset
    baseline = sum(samples[:4]) / 4
    
    # Conditional adjustment based on peak density
    if len(peaks) >= 3:
        adjustment = 12.5
    else:
        adjustment = -7.3
    
    # Final threshold calculation
    energy_threshold = baseline + adjustment
    
    # Irrelevant auxiliary variable (minor distraction)
    status_code = "OK"
    
    return energy_threshold

# Sensor simulation data (realistic naming)
load_samples = [68, 82, 74, 90, 65, 88, 71, 94]

# Key execution point
energy_threshold = analyze_load_pattern(load_samples)

print(f"Result: {energy_threshold}")