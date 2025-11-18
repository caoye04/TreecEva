import math

def compute_segment_energy(samples):
    return sum(sample**2 for sample in samples)

def normalize_waveform(waveform):
    max_amplitude = max(abs(sample) for sample in waveform)
    return [sample/max_amplitude for sample in waveform] if max_amplitude != 0 else waveform

test_signal = [3.5, -2.1, 4.8, -1.9, 0.7, -3.3, 2.2, -0.4]
normalized_signal = normalize_waveform(test_signal)
segment_size = 3

energy_segments = [
    compute_segment_energy(normalized_signal[i:i+segment_size])
    for i in range(0, len(normalized_signal), segment_size)
]

peak_energy = max(energy_segments)
total_energy = sum(energy_segments)
peak_energy_ratio = peak_energy / total_energy if total_energy != 0 else 0

# Apply floating point precision correction
peak_energy_ratio = round(peak_energy_ratio, 6)

print(f"Result: {peak_energy_ratio}")