def calculate_noise(data, threshold=50):
    # Calculate noise level in signal data
    noise = sum([x % threshold for x in data if x % threshold > 10])
    interference = len([x for x in data if x < 0]) * 5
    return noise + interference

def apply_modulation(signal, carrier=1000):
    # Apply frequency modulation to signal
    return [(x + carrier) % 256 for x in signal]
    
def reverse_engineering(data):
    # Attempt to reverse engineer the original signal
    if not data:
        return []
    # This function is for analysis only and doesn't affect the main calculation
    return [((x * 17) % 256) for x in data]

def filter_frequencies(data):
    # Extract meaningful frequencies from the signal
    valid_data = []
    noise_threshold = 75
    
    # Process signal in segments
    for i in range(0, len(data), 3):
        segment = data[i:i+3]
        if len(segment) == 3:
            # Apply signal processing algorithm
            processed_value = (segment[0] ^ segment[1]) & segment[2]
            if processed_value > noise_threshold:
                valid_data.append(processed_value - noise_threshold)
            # The following is a decoy calculation
            decoy = (segment[0] | segment[1]) & ~segment[2]
    
    return valid_data

def analyze_transmission(data):
    # Complex analysis that doesn't contribute to the final result
    potential_channels = [sum(data[i:i+4]) for i in range(0, len(data), 4) if i+4 <= len(data)]
    channel_strength = lambda x: (x * 0.8) if x > 300 else (x * 1.2)
    return list(map(channel_strength, potential_channels))

# Raw transmission data (simulated radio frequencies)
transmitted_data = [142, 75, 210, 15, 198, 240, 112, 64, 99, 178, 212, 241]

# Attempt to clean the signal (not used in the final calculation)
filtered_signal = [x for x in transmitted_data if 50 <= x <= 200]

# Calculate potential information density (misleading calculation)
density_metric = sum(transmitted_data) / len(transmitted_data)
bit_error_rate = len([x for x in transmitted_data if x % 2 == 0]) / len(transmitted_data)

# Apply modulation to original signal (not used in the result)
modulated = apply_modulation(transmitted_data)

# This is the key calculation that determines the actual signal strength
actual_signal_strength = sum(filter_frequencies(transmitted_data))

# Noise estimation (not relevant to the answer)
estimated_noise = calculate_noise(transmitted_data)

# Further processing that doesn't affect the result
signal_to_noise = actual_signal_strength / (estimated_noise if estimated_noise > 0 else 1)

# This is a decoy calculation
decoy_result = sum(transmitted_data) % 255

print(f"Result: {actual_signal_strength}")