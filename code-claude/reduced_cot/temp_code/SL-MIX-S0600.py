def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def find_prime_factors(num):
    # Find all prime factors of a number
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def analyze_harmonic_pattern(values):
    # Analyze harmonic patterns in the data
    pattern_sum = sum(values)
    pattern_product = 1
    for v in values:
        pattern_product *= (v % 10 + 1)
    
    harmonic_value = pattern_sum / pattern_product if pattern_product != 0 else 0
    return harmonic_value * 1.5

def calculate_signal_strength(data, position):
    # Calculate signal strength at a specific position
    if position >= len(data) or position < 0:
        return -1
    
    noise_factor = fibonacci(4) # Always equals 3
    interference = sum(find_prime_factors(position + 10))
    
    # Main calculation
    base_value = data[position] * (noise_factor - 1)
    secondary_value = data[position-1] if position > 0 else 0
    
    # Apply modulation
    return (base_value + secondary_value) % 100

def calculate_optimal_frequency(signal_data, target_index):
    # Process the signal data to find optimal transmission frequency
    if not signal_data or target_index >= len(signal_data):
        return -1
    
    # Misleading calculations that won't be used
    harmonic_value = analyze_harmonic_pattern(signal_data)
    max_signal = max(signal_data) if signal_data else 0
    min_signal = min(signal_data) if signal_data else 0
    
    # Calculate potential frequencies
    potential_freqs = []
    for i in range(len(signal_data)):
        # More misleading calculations
        temp = calculate_signal_strength(signal_data, i)
        modulated_value = (temp * 3) % 50
        potential_freqs.append(modulated_value)
    
    # The key calculation
    target_value = signal_data[target_index]
    base_freq = 100 - (target_value % 37) * 2
    
    # Apply modifiers based on signal characteristics
    freq_modifier = sum(d % 5 for d in signal_data) / 10
    noise_adjustment = fibonacci(3) # Always equals 2
    
    # Final calculation using conditional expression
    optimal_frequency = base_freq + freq_modifier if target_value > 50 else base_freq - freq_modifier
    optimal_frequency = optimal_frequency + noise_adjustment
    
    # These calculations don't affect the result
    for _ in range(2):
        if sum(potential_freqs) > 100:
            potential_freqs = [p/2 for p in potential_freqs]
    
    return optimal_frequency

# Signal data represents amplitude readings from a communication system
signal_data = [75, 42, 63, 18, 91]

# Calculate the signal quality metrics
quality_metrics = {
    'snr': sum(signal_data) / len(signal_data),
    'variance': sum((x - (sum(signal_data) / len(signal_data)))**2 for x in signal_data) / len(signal_data),
    'peak': max(signal_data),
    'floor': min(signal_data)
}

# Process some data that won't be used in the final answer
processed_data = []
for i, value in enumerate(signal_data):
    if i % 2 == 0:
        processed_data.append(value * 1.5)
    else:
        processed_data.append(value * 0.8)

# Find the optimal frequency for our target index
optimal_frequency = calculate_optimal_frequency(signal_data, 3)

# Some more misleading calculations
frequency_band = 'UHF' if optimal_frequency > 300 else 'VHF' if optimal_frequency > 30 else 'HF'
modulation_type = 'FM' if optimal_frequency % 2 == 0 else 'AM'

print(f"Result: {optimal_frequency}")