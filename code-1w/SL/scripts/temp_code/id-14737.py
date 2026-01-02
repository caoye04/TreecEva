import itertools

# Simulate a complex bioinformatics pipeline with decoy computations

def analyze_sequence_complexity(seq):
    return sum(1 for c in seq if c in 'GC') / len(seq)

# Irrelevant data structures and functions (distractors)
decoy_matrix = [[i * j for j in range(5)] for i in range(5)]
activation_map = {'A': 1, 'T': 0, 'C': -1, 'G': 2}
scaling_factor = 0.987

# Real data: gene expression flux values across time series
time_series_flux = [12.4, 15.6, 10.2, 18.9, 13.1, 16.8, 11.4, 14.7]

# Misleading intermediate calculation (dead path)
aggregate_response = 0
for val in time_series_flux:
    if val > 15:
        aggregate_response += val * 0.1

# Unused transformation function
def transform_signal(x):
    return x ** 2 + 2 * x + 1

# Primary analysis: filter based on dynamic threshold
threshold = 13.0
filtered_fluxes = [x for x in time_series_flux if x > threshold]

# Conditional expression with meaningful logic
base_efficiency = 0.85
adjustment = 0.1 if len(filtered_fluxes) > 4 else 0.05
efficiency_factor = base_efficiency + adjustment

# Key computation buried among distractions
filtration_yield = sum(filtered_fluxes) * efficiency_factor

# Decoy operations using itertools (irrelevant to final result)
combinations_test = list(itertools.combinations([1, 2, 3, 4], 2))
repeat_check = list(itertools.repeat('dummy', 3))

# Red herring: bit manipulation on unrelated metric
status_flag = 0b1010
status_flag ^= 0b1100
status_flag |= 0b0010

# Spurious array reshaping
reshaped_data = [[time_series_flux[i], time_series_flux[i+1]] for i in range(0, len(time_series_flux)-1, 2)]

# Final output
print(f"Result: {filtration_yield}")