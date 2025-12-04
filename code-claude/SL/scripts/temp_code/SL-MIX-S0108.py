def count_letter_frequencies(text):
    # Count frequency of each letter
    frequencies = {}
    for char in text.lower():
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def calculate_signal_noise_ratio(frequencies, threshold=3):
    # Calculate a signal-to-noise ratio based on letter frequencies
    if not frequencies:
        return 0
    
    total_chars = sum(frequencies.values())
    noise_chars = sum(count for char, count in frequencies.items() if count <= threshold)
    signal_chars = total_chars - noise_chars
    
    # Avoid division by zero
    if noise_chars == 0:
        return total_chars * 2
    
    return signal_chars / noise_chars

def apply_frequency_filter(frequencies, strength):
    # Apply a filter to the frequencies based on strength
    filtered = {}
    max_freq = max(frequencies.values()) if frequencies else 0
    
    # This is a distraction - we don't use modulation_factor
    modulation_factor = sum(ord(char) % 7 for char in frequencies.keys()) / 10
    
    for char, count in frequencies.items():
        # Apply the actual filter formula
        filtered[char] = count * (1 + (count / max_freq) * strength)
    
    return filtered

def calculate_optimal_frequency(text, filter_strength):
    # Process the text and calculate the optimal frequency
    raw_frequencies = count_letter_frequencies(text)
    
    # Distractor calculations
    potential_primes = [n for n in range(2, 20) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
    entropy_estimate = sum(ord(c) & 0x0F for c in text[:10])
    
    # More distractor variables
    redundancy_factor = len(text) / (len(set(text)) or 1)
    compression_ratio = redundancy_factor * 0.75
    
    # Apply filter to the frequencies
    filtered_frequencies = apply_frequency_filter(raw_frequencies, filter_strength)
    
    # Calculate signal-to-noise ratio
    snr = calculate_signal_noise_ratio(filtered_frequencies)
    
    # Dead code path - never executed due to the condition
    if entropy_estimate > 1000:
        return (snr * compression_ratio) / (redundancy_factor * 0.5)
    
    # The actual calculation for the target frequency
    vowels = 'aeiou'
    vowel_counts = sum(filtered_frequencies.get(v, 0) for v in vowels)
    consonant_counts = sum(filtered_frequencies.get(c, 0) for c in filtered_frequencies if c not in vowels)
    
    # More distractor calculations
    if len(potential_primes) > 5:
        harmonic_mean = len(potential_primes) / sum(1/p for p in potential_primes)
    else:
        harmonic_mean = 3.14159
    
    # The final calculation
    if consonant_counts == 0:
        return vowel_counts * 1.5
    
    base_frequency = (vowel_counts / consonant_counts) * (filter_strength + 1)
    target_frequency = round(base_frequency * 100) / 100
    
    return target_frequency

# Main code execution
text_sample = "The quick brown fox jumps over the lazy dog."
filter_strength = 2

# More distracting calculations
character_entropy = sum(ord(c) for c in text_sample) % 256
bit_operations = (character_entropy << 3) | (character_entropy >> 2)
reversed_text = text_sample[::-1]

# Distractor condition that's always false
if len(text_sample) > 100:
    adjusted_strength = filter_strength * (bit_operations % 5)
else:
    adjusted_strength = filter_strength

# The key calculation
target_frequency = calculate_optimal_frequency(text_sample, filter_strength)

# Some more distractions
alternative_result = len([c for c in text_sample if c.lower() in 'aeiou']) / len(text_sample)
weighted_score = (target_frequency + alternative_result) / 2

print(f"Target result: {target_frequency}")