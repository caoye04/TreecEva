from collections import defaultdict
import math

def compute_spectral_moment(coefficients, order):
    if not coefficients:
        return 0
    mean_val = sum(coefficients) / len(coefficients)
    moment = sum((x - mean_val) ** order for x in coefficients) / len(coefficients)
    return moment

def process_audio_channel(channel_data):
    spectral_features = []
    for time_frame in channel_data:
        # Compute energy and kurtosis for each time frame
        energy = sum(c * c for c in time_frame)
        kurtosis = compute_spectral_moment(time_frame, 4)
        spectral_features.append(energy * (1 + kurtosis))
    return spectral_features

# Multi-channel spectro-temporal representation
audio_channels = [
    [[0.5, 0.2, -0.1], [0.3, -0.4, 0.6], [-0.2, 0.7, -0.3]],
    [[0.1, -0.3, 0.4], [-0.5, 0.2, 0.1], [0.6, -0.2, -0.4]],
    [[-0.4, 0.5, 0.3], [0.2, -0.6, 0.1], [0.3, 0.4, -0.5]]
]

channel_metrics = defaultdict(list)
for idx, channel in enumerate(audio_channels):
    features = process_audio_channel(channel)
    channel_metrics['energies'].append(sum(features))
    channel_metrics['peak_features'].append(max(features))

# Compute cross-channel dispersion metric
mean_energy = sum(channel_metrics['energies']) / len(channel_metrics['energies'])
cross_channel_variance = sum((e - mean_energy) ** 2 for e in channel_metrics['energies']) / len(channel_metrics['energies'])

# Spectral flux computation using list comprehension
instantaneous_fluctuations = [
    abs(channel_metrics['peak_features'][i] - channel_metrics['peak_features'][i-1])
    for i in range(1, len(channel_metrics['peak_features']))
]

spectral_flux_index = (sum(instantaneous_fluctuations) / len(instantaneous_fluctuations)) * math.sqrt(cross_channel_variance)

print(f"Result: {round(spectral_flux_index, 6)}")