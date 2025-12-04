class SignalProcessor:
    def __init__(self, base_frequency=42):
        self.base_frequency = base_frequency
        self.noise_filters = {
            'high': lambda x: x & 0xF0,
            'low': lambda x: x & 0x0F,
            'band': lambda x: x & 0x3C
        }
        self.calibration_factors = [1.5, 0.75, 2.25, 1.0]
        self.interference_map = {i: (i * 3) % 256 for i in range(16)}
        
    def apply_noise_reduction(self, signal_data):
        # Unused noise reduction that looks important
        reduced = []
        for val in signal_data:
            if val > 200:
                reduced.append(val - 50)
            elif val < 50:
                reduced.append(val + 25)
            else:
                reduced.append(val)
        return reduced
    
    def calculate_distortion(self, frequency):
        # Misleading distortion calculation
        distortion = 0
        for i in range(1, 6):
            distortion += (frequency * i) % 17
        return distortion / 10.0
    
    def compute_final_strength(self):
        # This is where the actual calculation happens
        raw_signal = [self.base_frequency]
        
        # Generate misleading signal values
        for i in range(5):
            next_val = (raw_signal[-1] * 1.5) % 100
            raw_signal.append(next_val)
        
        # Apply a filter that looks important but isn't used
        filtered_high = self.noise_filters['high'](self.base_frequency)
        filtered_low = self.noise_filters['low'](self.base_frequency)
        
        # The key calculation - uses bitwise XOR and dictionary lookup
        key_value = filtered_high ^ filtered_low
        
        # More misleading calculations
        harmonic_series = sum(1/n for n in range(1, self.base_frequency % 10 + 2))
        distortion_factor = self.calculate_distortion(self.base_frequency)
        
        # Actual signal strength calculation using the key_value
        interference = self.interference_map.get(key_value, 0)
        strength_factor = min(self.calibration_factors) + max(self.calibration_factors)
        
        # Final calculation combines key elements
        return (key_value * strength_factor) - interference

# Setup and execution
signal_data = [65, 120, 210, 45, 90]
signal_processor = SignalProcessor()

# More distractions
harmonics = [signal_processor.base_frequency * (i/2) for i in range(1, 5)]
resonance = sum(harmonics) / len(harmonics)
modulation_index = lambda f: (f % 10) / 10.0
modulated = list(map(modulation_index, signal_data))

# Calculate the final result
final_signal_strength = signal_processor.compute_final_strength()
print(f"Target result: {final_signal_strength}")