def calculate_power(base, exp):
    # Helper function to calculate power with special cases
    if base == 0 and exp == 0:
        return 1  # Mathematical convention
    if exp < 0 and base == 0:
        return float('inf')  # Division by zero
    return base ** exp

def noise_analysis(signal_data, frequencies):
    # Signal processing function that analyzes noise patterns
    # and returns the optimal frequency for filtering
    
    # Initialize tracking variables
    max_amplitude = 0
    min_interference = float('inf')
    optimal_freq = 0
    noise_threshold = 75
    
    # Process metrics that aren't actually used
    baseline_metrics = {
        'snr': sum(signal_data) / len(signal_data),
        'peak': max(signal_data) if signal_data else 0,
        'valley': min(signal_data) if signal_data else 0
    }
    
    # Calculate signal strength for distraction
    signal_strength = 0
    for i, amplitude in enumerate(signal_data):
        if i % 3 == 0:
            signal_strength += amplitude * 0.8
        elif i % 3 == 1:
            signal_strength += amplitude * 1.2
        else:
            signal_strength += amplitude
    
    # This loop looks complex but most calculations are irrelevant
    for freq in frequencies:
        # Misleading calculation that isn't used
        harmonic_factor = freq / 10 if freq > 0 else 1
        resonance = sum(s * calculate_power(harmonic_factor, 0.5) for s in signal_data[:3])
        
        # The actual calculation that matters
        interference = sum(abs(s - freq) for s in signal_data)
        
        # More distracting calculations
        if freq > noise_threshold:
            normalized_freq = freq / 100
            weighted_interference = interference * (1 + normalized_freq)
        else:
            weighted_interference = interference * 0.95
            
        # This condition is never met due to the data
        if resonance > 1000 and interference < min_interference / 2:
            return freq + 10
        
        # The actual logic that determines the result
        if interference < min_interference:
            min_interference = interference
            optimal_freq = freq
    
    # These lines create confusion but don't affect the result
    adjusted_freq = optimal_freq
    if baseline_metrics['snr'] > 50:
        adjusted_freq += 5
    elif baseline_metrics['peak'] > 200:
        adjusted_freq -= 3
    
    # Early return that's never triggered
    if min_interference > 1000:
        return frequencies[0]
        
    return adjusted_freq if adjusted_freq > 0 else optimal_freq

# Main code execution
signal_data = [45, 67, 32, 89, 51]
true_frequencies = [20, 40, 60, 80, 100]
false_frequencies = [15, 35, 55, 75, 95]  # Unused distractor

# Calculate some metrics that aren't used
max_signal = max(signal_data)
min_signal = min(signal_data)
dynamic_range = max_signal - min_signal

# Misleading preprocessing
processed_signal = []
for s in signal_data:
    if s > 50:
        processed_signal.append(s * 1.1)
    else:
        processed_signal.append(s * 0.9)

# The key statement that computes the answer
optimal_frequency = noise_analysis(signal_data, true_frequencies)

# More distraction after the answer is already computed
filtered_signal = [s - (optimal_frequency * 0.1) for s in signal_data]
quality_score = sum(filtered_signal) / len(filtered_signal)

# This conditional creates a red herring - it's never executed
if quality_score > 100:
    optimal_frequency = optimal_frequency + 10

print(f"Result: {optimal_frequency}")