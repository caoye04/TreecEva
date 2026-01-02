def analyze_signal_quality(buffer):
    base_level = sum(buffer) / len(buffer)
    peak = max(buffer)
    normalized_peak = peak / (base_level + 1e-5)
    
    # Conditional expression used here
    signal_class = 'strong' if normalized_peak > 1.5 else 'weak'
    
    # Simulate light recursive processing for quality score
    def dampen_noise(level, depth=2):
        if depth == 0:
            return level * 0.9
        return dampen_noise(level * 0.95, depth - 1)
    
    raw_quality = base_level * (1 + normalized_peak)
    refined_quality = dampen_noise(raw_quality)
    
    # Final threshold computation
    energy_threshold = int(refined_quality) if signal_class == 'strong' else int(refined_quality * 0.7)
    return energy_threshold

# Simulated sensor data buffer
signal_buffer = [12, 15, 10, 8, 23, 17, 14]

# Irrelevant auxiliary variable (minimal distraction - intervention level 4)
calibration_offset = 0.05

energy_threshold = analyze_signal_quality(signal_buffer)
print(f"Result: {energy_threshold}")