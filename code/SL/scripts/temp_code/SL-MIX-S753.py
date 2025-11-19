from functools import reduce
from collections import namedtuple

# Define a named tuple for frequency band data
BandData = namedtuple('BandData', ['frequency', 'amplitude', 'phase'])

# Sample input representing processed frequency bands
processed_bands = [
    BandData(120, 0.5, 0.3),
    BandData(250, 1.2, -0.7),
    BandData(500, 0.8, 1.5),
    BandData(1000, 2.1, -0.2),
    BandData(2000, 0.9, 0.9)
]

def calculate_band_effect(band):
    # Apply a logarithmic transformation if amplitude > 1.0
    transformed_amplitude = band.amplitude if band.amplitude <= 1.0 else (band.amplitude * 0.7 + 0.3)
    # Calculate effect as product of frequency and transformed amplitude, adjusted by phase
    return int(band.frequency * transformed_amplitude * (1 + band.phase))

def validate_band(band):
    # Check if band meets minimum quality criteria
    return band.amplitude > 0.4 and band.frequency > 100

cumulative_effect = 0
filter_count = 0

for band in processed_bands:
    if validate_band(band) and (band.phase >= 0 or band.frequency < 1500):
        effect = calculate_band_effect(band)
        # Only apply effect if it's positive and less than threshold
        if effect > 0 and effect < 2000:
            cumulative_effect += effect
            filter_count += 1
            # Early termination condition for efficiency
            if filter_count >= 3 and cumulative_effect > 1000:
                break

# Final adjustment using functional approach
if filter_count > 0:
    adjustments = list(map(lambda x: x % 100, [calculate_band_effect(b) for b in processed_bands[:filter_count]]))
    total_adjustment = reduce(lambda a, b: a ^ b, adjustments, 0)  # XOR all adjustments
    cumulative_effect ^= total_adjustment  # Apply final adjustment

print(f"Result: {cumulative_effect}")