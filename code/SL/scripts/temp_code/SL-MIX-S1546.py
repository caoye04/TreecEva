import math
from functools import reduce

def signal_intensity_decay(initial_intensity, time_elapsed):
    return initial_intensity * math.exp(-0.1 * time_elapsed)

def log_scale_accumulator(accumulated, new_value):
    return accumulated + math.log(new_value + 1)

# Signal measurements over time
signals = [100, 80, 60, 40]
time_stamps = [0, 1, 2, 3]

# Calculate decayed intensities
intensities = [signal_intensity_decay(s, t) for s, t in zip(signals, time_stamps)]

# Apply logarithmic accumulation
cumulative_effect = reduce(log_scale_accumulator, intensities, 0)

print(f"Result: {cumulative_effect}")