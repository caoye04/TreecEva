def analyze_signal_patterns(signal_data):
    # Process noise levels (not relevant to main calculation)
    noise_levels = [x % 17 for x in range(8, 25)]
    filtered_noise = [n for n in noise_levels if n > 5]
    
    # Extract frequency components from signal
    frequencies = signal_data[:5]
    amplitudes = signal_data[5:10]
    phase_shifts = signal_data[10:15] if len(signal_data) > 14 else [0, 0, 0, 0, 0]
    
    # Calculate signal strength (misleading)
    signal_strength = sum(f * a for f, a in zip(frequencies, amplitudes))
    normalized_strength = signal_strength / max(amplitudes) if max(amplitudes) > 0 else 0
    
    # Calculate interference factor (distraction)
    interference = sum(p ** 2 for p in phase_shifts) / len(phase_shifts)
    
    # Return only the frequency components for actual use
    return frequencies

def decode_message(encrypted_data, key_sequence):
    # Apply various transformations to decode the message
    step1 = [x + y for x, y in zip(encrypted_data, key_sequence)]
    
    # Misleading operations
    potential_keys = [k ** 2 - 3 for k in key_sequence]
    alternative_decode = [e * 2 - k for e, k in zip(encrypted_data, potential_keys)]
    
    # Actual decoding logic
    step2 = [(x % 26) + 65 for x in step1]  # Convert to ASCII capital letters
    
    # Distraction: calculate checksum
    checksum = sum(step2) % 256
    verification_code = (checksum * 7) % 100
    
    # Create the decoded result
    decoded = [chr(c) for c in step2]
    return ''.join(decoded)

def analyze_frequency(message):
    # Create frequency map of characters
    freq_map = {}
    for char in message:
        if char.isalpha():
            char = char.upper()
            freq_map[char] = freq_map.get(char, 0) + 1
    
    # Calculate average frequency (distraction)
    avg_freq = sum(freq_map.values()) / len(freq_map) if freq_map else 0
    median_value = sorted(freq_map.values())[len(freq_map)//2] if freq_map else 0
    
    # Create misleading metrics
    frequency_score = sum(ord(c) * f for c, f in freq_map.items()) / 100
    
    return freq_map

def calculate_priority(message, freq_map):
    # Calculate letter positions in the alphabet (A=1, B=2, etc.)
    letter_positions = [ord(c) - 64 for c in message if c.isalpha()]
    
    # Misleading calculations
    vowel_count = sum(1 for c in message if c.upper() in 'AEIOU')
    consonant_value = sum(ord(c) for c in message if c.upper() not in 'AEIOU' and c.isalpha())
    
    # Extract most frequent letter
    if not freq_map:
        return 0
    most_frequent = max(freq_map.items(), key=lambda x: x[1])[0]
    
    # Calculate priority based on position of most frequent letter
    position_value = ord(most_frequent) - 64  # A=1, B=2, etc.
    
    # Misleading calculation that looks important
    complex_factor = (vowel_count * 5) + (sum(letter_positions) // 3)
    weighted_average = (position_value * 2 + complex_factor) / 3
    
    # The actual priority calculation
    return position_value * 5

# Main program
signal_data = [3, 7, 12, 8, 5, 10, 15, 8, 12, 7, 2, 3, 1, 4, 2]
frequencies = analyze_signal_patterns(signal_data)

# Define the encryption key (this is what matters)
key = [2, 4, 1, 3, 5, 2, 4]

# Create encrypted message (misleading longer sequence)
encrypted = [15, 4, 19, 19, 0, 6, 4]

# Apply some transformations to the data (distraction)
transformed_data = [f ** 2 % 20 for f in frequencies]
filtered_data = [d for d in transformed_data if d > 5]

# Decode the message using relevant parts
decoded_message = decode_message(encrypted, key)

# Analyze character frequencies
frequency_map = analyze_frequency(decoded_message)

# Calculate the final priority value
priority_value = calculate_priority(decoded_message, frequency_map)

# Some misleading final calculations to distract
final_score = sum(frequencies) * len(decoded_message)
weighted_result = (priority_value + final_score) / 2
normalized_output = weighted_result * 0.75 + priority_value * 0.25

print(f"Decoded message: {decoded_message}")
print(f"Priority value: {priority_value}")
