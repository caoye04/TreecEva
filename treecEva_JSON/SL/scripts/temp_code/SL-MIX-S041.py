import math
from functools import reduce

def signal_transform_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return round(result, 6)
    return wrapper

@signal_transform_decorator
def compute_filter_gain(freq, quality_factor):
    return 20 * math.log10(quality_factor * math.sqrt(freq))

# Audio filter parameters
base_frequency = 1200.0
quality_factors = [0.707, 1.414, 2.828]
frequency_multipliers = [0.5, 1.0, 2.0]

# Process filter coefficients
processed_gains = []
for q_factor in quality_factors:
    temp_gain = 0
    for mult in frequency_multipliers:
        freq = base_frequency * mult
        gain = compute_filter_gain(freq, q_factor)
        match gain:
            case g if g > 50.0:
                temp_gain += g * 0.1
            case g if g > 30.0:
                temp_gain += g * 0.5
            case _:
                temp_gain += g * 0.9
    processed_gains.append(temp_gain)

# Calculate impulse response
impulse_components = []
for i, gain in enumerate(processed_gains):
    component = gain * math.sin(math.pi * i / len(processed_gains))
    impulse_components.append(component)

final_impulse_response = reduce(lambda x, y: x + y, impulse_components, 0.0)
print(f'Result: {final_impulse_response}')