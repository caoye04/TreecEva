from collections import defaultdict
import math

def apply_transform(freq_band, amplitude):
    transforms = {
        0: lambda x: x * 2,
        1: lambda x: x ** 2,
        2: lambda x: math.sqrt(x) if x >= 0 else 0,
        3: lambda x: abs(x),
        4: lambda x: x + 10
    }
    return transforms.get(freq_band, lambda x: x)(amplitude)

def process_audio_signal(signal_data):
    band_accumulator = defaultdict(float)
    
    for freq_index, amplitude in enumerate(signal_data):
        band_id = freq_index % 5
        transformed_value = apply_transform(band_id, amplitude)
        band_accumulator[band_id] += transformed_value
    
    # Calculate overall signal strength
    total_components = sum(band_accumulator.values())
    processed_signal_strength = 0
    
    for band_key in sorted(band_accumulator.keys()):
        component_ratio = band_accumulator[band_key] / total_components if total_components > 0 else 0
        if component_ratio > 0.25:
            processed_signal_strength += int(band_accumulator[band_key]) << 1
        elif component_ratio > 0.1:
            processed_signal_strength += int(band_accumulator[band_key]) & 0xFF
        else:
            processed_signal_strength += int(band_accumulator[band_key]) ^ 0xF0
    
    return processed_signal_strength

# Input signal data representing amplitude values across frequency spectrum
input_spectrum = [16, 9, 25, -8, 4, 36, 49, -12, 64, 81]
processed_signal_strength = process_audio_signal(input_spectrum)
print(f"Result: {processed_signal_strength}")