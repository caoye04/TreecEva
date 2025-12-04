def calculate_broadcast_metrics(frequencies, channels, noise_levels):
    # Initialize signal processing variables
    primary_band = sum([f for f in frequencies if f % 2 == 0])
    secondary_band = sum([f for f in frequencies if f % 3 == 0])
    
    # Process noise reduction parameters
    noise_reduction = lambda x: x // 2 if x > 100 else x
    reduced_noise = [noise_reduction(n) for n in noise_levels]
    
    # Calculate channel metrics
    active_channels = set(channels) - {0, 7, 13}
    backup_channels = {ch + 1 for ch in channels if ch % 5 == 0}
    potential_channels = active_channels.union(backup_channels)
    
    # Signal integrity processing
    main_channel = 42
    for ch in potential_channels:
        if ch % 4 == 0 and ch in active_channels:
            main_channel = (main_channel * ch) % 256
    
    # Frequency filtering and modulation
    frequency_mask = 0xFF
    for f in frequencies:
        if f > 150:
            frequency_mask = (frequency_mask << 1) & 0xFF
        elif f < 50:
            frequency_mask = (frequency_mask >> 1) & 0xFF
    
    # Interference calculation (unused in final result)
    interference = sum(reduced_noise) % 100
    modulation_index = (primary_band - secondary_band) % 50
    
    # Error correction processing
    error_bits = sum([n & 0x0F for n in reduced_noise])
    error_correction = error_bits ^ (sum(channels) & 0xFF)
    
    # Filter frequencies based on modulation pattern
    filtered_frequencies = 0
    for i, f in enumerate(sorted(frequencies)):
        if i % 3 == 0 or f % 7 == 0:
            filtered_frequencies |= (1 << (f % 8))
    
    # Calculate transmission power (distractor)
    transmission_power = 0
    for ch in active_channels:
        for n in reduced_noise:
            if ch % n == 0 and n > 0:
                transmission_power += ch * 2
    
    # Signal strength calculation - this is the key operation
    signal_strength = (filtered_frequencies & main_channel) | error_correction
    
    # Calculate broadcast range (distractor)
    broadcast_range = ((primary_band * main_channel) // max(reduced_noise)) % 1000
    optimal_frequency = frequencies[len(frequencies) // 2] if frequencies else 0
    
    # Output processing results
    print(f"Noise levels: {reduced_noise}")
    print(f"Active channels: {active_channels}")
    print(f"Frequency mask: {frequency_mask}")
    print(f"Main channel: {main_channel}")
    print(f"Filtered frequencies: {filtered_frequencies}")
    print(f"Error correction: {error_correction}")
    print(f"Result: {signal_strength}")
    
    return signal_strength

# Input parameters
frequencies = [42, 78, 105, 121, 210, 36, 63]
channels = [4, 8, 15, 16, 23, 42]
noise_levels = [120, 84, 56, 72]

# Execute calculation
result = calculate_broadcast_metrics(frequencies, channels, noise_levels)