def calculate_noise_factor(signal_data):
    # Calculate noise factor based on signal variance
    if len(signal_data) == 0:
        return 0
    
    # Extract signal strengths for noise calculation
    strengths = [s[1] for s in signal_data if isinstance(s, tuple) and len(s) > 1]
    if not strengths:
        return 0
        
    # Calculate variance as noise indicator
    mean = sum(strengths) / len(strengths)
    variance = sum((x - mean) ** 2 for x in strengths) / len(strengths)
    return variance ** 0.5  # Standard deviation as noise factor

def filter_by_frequency(signals, min_freq, max_freq):
    # Filter signals by frequency range
    return [s for s in signals if min_freq <= s[0] <= max_freq]

def calculate_priority(signals):
    # Complex priority calculation for signal processing
    if not signals:
        return 0
    
    # Extract valid signals with proper format (frequency, strength, type)
    valid_signals = [s for s in signals if isinstance(s, tuple) and len(s) >= 3]
    
    # Calculate baseline from strongest signals
    baseline_signals = sorted(valid_signals, key=lambda x: x[1], reverse=True)[:3]
    baseline = sum(s[1] for s in baseline_signals) / len(baseline_signals) if baseline_signals else 0
    
    # Calculate priority based on signal types
    priority = 0
    type_weights = {'A': 5, 'B': 3, 'C': 1, 'D': 0, 'E': -1}
    
    for i, signal in enumerate(valid_signals):
        freq, strength, sig_type = signal[0], signal[1], signal[2]
        
        # Apply type weight
        weight = type_weights.get(sig_type, 0)
        
        # Priority calculation formula
        if i % 2 == 0:  # Even indices get positive adjustment
            priority += (strength / 100) * weight * (freq / 10)
        else:  # Odd indices get negative adjustment
            priority -= (strength / 200) * (weight / 2) * (freq / 20)
    
    # Apply baseline adjustment
    priority = priority * (1 + baseline / 1000)
    
    # Round to 2 decimal places for stability
    return round(priority, 2)

# Simulate signal data collection
raw_signals = [
    (150, 720, 'A'),  # High frequency, strong A-type signal
    (80, 450, 'B'),    # Mid frequency, medium B-type signal
    (210, 380, 'A'),   # Very high frequency, medium A-type signal
    (95, 620, 'C'),    # Mid frequency, strong C-type signal
    (30, 810, 'B'),    # Low frequency, very strong B-type signal
    (175, 530, 'D'),   # High frequency, medium D-type signal
    (60, 340, 'E'),    # Low frequency, weak E-type signal
    (120, 490, 'B'),   # Mid-high frequency, medium B-type signal
    (200, 280, 'C'),   # Very high frequency, weak C-type signal
    (45, 710, 'A')     # Low frequency, strong A-type signal
]

# Process signals with various filters
low_band = filter_by_frequency(raw_signals, 0, 70)
medium_band = filter_by_frequency(raw_signals, 70, 150)
high_band = filter_by_frequency(raw_signals, 150, 250)

# Calculate noise factors for different bands
low_noise = calculate_noise_factor(low_band)
med_noise = calculate_noise_factor(medium_band)
high_noise = calculate_noise_factor(high_band)

# Generate interference metrics (not used in final calculation)
interference_score = (low_noise * 2 + med_noise * 1.5 + high_noise) / 3
quality_index = 100 - interference_score * 10

# Create distraction list with enumeration
distraction_list = [s[1] * (i+1) for i, s in enumerate(raw_signals) if s[1] > 500]

# More distracting operations
distraction_matrix = [[i * j for j in range(3)] for i in range(4)]
transposed = list(zip(*distraction_matrix))

# Extract signal data for processing
signal_types = {signal[2] for signal in raw_signals if len(signal) > 2}
type_counts = {sig_type: sum(1 for s in raw_signals if len(s) > 2 and s[2] == sig_type) for sig_type in signal_types}

# Filter signals for priority calculation
strength_threshold = sum(s[1] for s in raw_signals) / len(raw_signals) * 0.8
frequency_range = (60, 180)
filtered_signals = [s for s in raw_signals if s[1] >= strength_threshold or 
                   (frequency_range[0] <= s[0] <= frequency_range[1] and s[2] in ['A', 'B'])]

# Calculate priority from filtered signals
priority_value = calculate_priority(filtered_signals)

# Generate additional metrics for reporting (not used in result)
cover_ratio = len(filtered_signals) / len(raw_signals)
efficiency_score = priority_value / (sum(s[1] for s in filtered_signals) / 1000) if filtered_signals else 0

# Print results
print(f"Noise factors - Low: {low_noise:.2f}, Med: {med_noise:.2f}, High: {high_noise:.2f}")
print(f"Quality index: {quality_index:.2f}")
print(f"Signal coverage: {cover_ratio:.2f}")
print(f"Result: {priority_value}")