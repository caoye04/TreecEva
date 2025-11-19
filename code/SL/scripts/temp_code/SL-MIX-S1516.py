from functools import reduce

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

class FilterProcessor:
    def __init__(self):
        self.coefficients_cache = {}
    
    @call_counter
    def compute_coefficient(self, n):
        if n in self.coefficients_cache:
            return self.coefficients_cache[n]
        if n <= 1:
            result = 1
        else:
            result = self.compute_coefficient(n-1) + 2 * self.compute_coefficient(n-2)
        self.coefficients_cache[n] = result
        return result

# Initialize processor
processor = FilterProcessor()

# Audio signal parameters
frequencies = [3, 5, 7, 9]
attenuation_factors = [0.8, 0.6, 0.4, 0.2]

# Process signals
processed_signals = []
for i, freq in enumerate(frequencies):
    coeff = processor.compute_coefficient(freq)
    adjusted_signal = coeff * attenuation_factors[i]
    processed_signals.append(adjusted_signal)

# Apply functional transformations
squared_signals = list(map(lambda x: x**2, processed_signals))
filtered_signals = list(filter(lambda x: x > 10, squared_signals))

# Calculate final gain using reduce
if filtered_signals:
    total_energy = reduce(lambda a, b: a + b, filtered_signals, 0)
    signal_count = len(filtered_signals)
    optimized_gain = (total_energy / signal_count) if signal_count > 0 else 0
else:
    optimized_gain = 0

print(f"Result: {int(optimized_gain)}")