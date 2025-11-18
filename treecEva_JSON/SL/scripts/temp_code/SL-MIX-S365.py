from collections import defaultdict
import math

def hamming_window(n, N):
    return 0.54 - 0.46 * math.cos(2 * math.pi * n / (N - 1))

audio_samples = [0.1, -0.3, 0.5, -0.7, 0.9, -0.2, 0.4]
sample_count = len(audio_samples)
weighted_sum = 0.0

for idx in range(sample_count):
    window_value = hamming_window(idx, sample_count)
    weighted_sum += audio_samples[idx] * window_value

threshold = 0.1
is_above_threshold = weighted_sum > threshold

energy_map = defaultdict(float)
for i, sample in enumerate(audio_samples):
    energy_map[i] = sample ** 2

total_energy = sum(energy_map.values())
high_energy_flag = total_energy > 0.5

# Signal detection logic combines both metrics
signal_detected = int(is_above_threshold and high_energy_flag)

print(f"Result: {signal_detected}")