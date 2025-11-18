from collections import defaultdict
from functools import reduce
import statistics

def compute_weighted_harmonic_mean(values, weights):
    if len(values) != len(weights) or any(w == 0 for w in weights):
        return 0
    return len(values) / sum(w/v for v, w in zip(values, weights) if v != 0)

# Audio spectral data
spectral_magnitudes = [4.2, 3.8, 5.1, 2.9, 6.3]

# Metadata tag for weighting
metadata_tag = "AUDIO_XYZ_v2.1"

# Generate weights from character positions (1-indexed) of alphanumeric chars only
weight_map = defaultdict(int)
for idx, char in enumerate(metadata_tag, 1):
    if char.isalnum():
        weight_map[char] += idx

# Extract weights corresponding to unique characters in order of appearance
unique_chars = []
seen = set()
for c in metadata_tag:
    if c.isalnum() and c not in seen:
        unique_chars.append(c)
        seen.add(c)

weights = [weight_map[c] for c in unique_chars]

# Normalize weights to match the length of spectral_magnitudes
if len(weights) > len(spectral_magnitudes):
    weights = weights[:len(spectral_magnitudes)]
elif len(weights) < len(spectral_magnitudes):
    # Repeat weights cyclically
    weights = (weights * ((len(spectral_magnitudes) // len(weights)) + 1))[:len(spectral_magnitudes)]

# Compute base metric
harmonic_mean = compute_weighted_harmonic_mean(spectral_magnitudes, weights)

# Apply signal transformation
transformed_values = list(map(lambda x: round(x * 10), spectral_magnitudes))
median_transform = statistics.median(transformed_values)

# Final signal strength calculation
processed_signal_strength = int(harmonic_mean * median_transform / 100)

print(f"Result: {processed_signal_strength}")