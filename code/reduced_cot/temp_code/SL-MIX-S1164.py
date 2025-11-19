def modular_filter(x, modulus):
    return x % modulus if x >= 0 else (x % modulus + modulus) % modulus

def apply_filter_chain(signal_data):
    # Initialize processing parameters
    filter_params = {
        'attenuation': 3,
        'amplification': 2,
        'modulus': 128
    }
    
    # Dictionary comprehension to create initial state mapping
    signal_states = {i: {'raw': val, 'processed': 0} for i, val in enumerate(signal_data)}
    
    # Merge with default processing rules
    default_rules = {'clipping_threshold': 100, 'enable_agc': True}
    processing_config = {**filter_params, **default_rules}
    
    total_energy = 0
    
    # Process each signal sample
    for idx, state in signal_states.items():
        raw_value = state['raw']
        
        # Apply attenuation with modular arithmetic
        attenuated = modular_filter(raw_value * processing_config['attenuation'], processing_config['modulus'])
        
        # Short-circuit evaluation for conditional amplification
        amplified = attenuated * processing_config['amplification'] if processing_config['enable_agc'] and attenuated < processing_config['clipping_threshold'] else attenuated
        
        # Update state with processed value
        signal_states[idx]['processed'] = amplified
        
        # Accumulate energy using modular addition
        total_energy = (total_energy + amplified) % processing_config['modulus']
    
    # Calculate final signal strength using context manager for precision control
    class PrecisionControl:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def compute_strength(self, states, energy):
            max_processed = max(s['processed'] for s in states.values())
            return (max_processed * energy) % 256
    
    with PrecisionControl() as pc:
        processed_signal_strength = pc.compute_strength(signal_states, total_energy)
    
    return processed_signal_strength

# Test data representing audio samples
audio_samples = [45, -23, 120, 67, -89, 34, 156]

# Execute the filter chain
final_result = apply_filter_chain(audio_samples)
print(f"Result: {final_result}")