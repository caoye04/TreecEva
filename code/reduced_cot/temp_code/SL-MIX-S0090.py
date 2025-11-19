import math

def call_tracker(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_tracker
def process_frequency_band(band_data, attenuation_factor):
    return [math.floor(x * attenuation_factor) for x in band_data]

@call_tracker
def apply_noise_gate(signal_values, threshold):
    return list(map(lambda x: x if x > threshold else 0, signal_values))

# Audio signal processing pipeline
frequency_bands = [[120, 180, 240], [95, 155, 215], [110, 170, 230]]
attenuation_matrix = [0.8, 0.7, 0.9]
noise_threshold = 100

processed_signals = []
for i in range(len(frequency_bands)):
    if i % 2 == 0:
        processed_band = process_frequency_band(frequency_bands[i], attenuation_matrix[i])
    else:
        processed_band = apply_noise_gate(frequency_bands[i], noise_threshold)
    processed_signals.append(processed_band)

# Final signal strength calculation
signal_weights = {0: 1.2, 1: 1.5, 2: 1.1}
weighted_sum = sum(
    signal_weights[band_idx] * sum(processed_signals[band_idx])
    for band_idx in range(len(processed_signals))
    if sum(processed_signals[band_idx]) > 0
)

final_signal_strength = math.ceil(weighted_sum / (process_frequency_band.call_count + apply_noise_gate.call_count))
print(f"Result: {final_signal_strength}")