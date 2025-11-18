def process_signal(data_stream):
    # Phase 1: Base transformation using modular exponentiation
    base_transform = {i: pow(i, 3, 17) for i in data_stream}
    
    # Phase 2: Frequency encoding with lambda-based mapping
    freq_encoder = lambda x: (x * 13 + 7) % 19
    encoded_freq = {k: freq_encoder(v) for k, v in base_transform.items()}
    
    # Phase 3: Signal amplification with selective filtering
    amplified = {k: v*2 if k % 2 == 0 else v*3 for k, v in encoded_freq.items()}
    
    # Phase 4: Interference correction using dictionary merging
    correction_map = {i: (i*5) % 11 for i in range(10)}
    corrected = {**amplified, **{k: v for k, v in correction_map.items() if k not in amplified}}
    
    # Phase 5: Final modulation calculation
    modulated_signal_strength = sum((k * v + 1) % 23 for k, v in corrected.items())
    return modulated_signal_strength

# Test sequence representing received signal data
received_data = [4, 7, 2, 9, 1, 8, 5]
signal_output = process_signal(received_data)
print(f"Result: {signal_output}")