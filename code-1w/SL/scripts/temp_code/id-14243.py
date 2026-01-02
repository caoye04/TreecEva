from itertools import combinations

# Simulate signal harmonics analysis in acoustic engineering
def analyze_harmonics(frequencies):
    pairs = list(combinations(frequencies, 2))
    products = []
    for a, b in pairs:
        if (a + b) % 2 == 0:
            products.append(a * b)
    return sum(products)

base_freqs = [3, 5, 7, 9]
raw_product_sum = analyze_harmonics(base_freqs)

damping_factor = 0.85
adjusted_energy = raw_product_sum * damping_factor

# Apply nonlinear correction using lambda
nonlinear_correction = lambda x: x ** 1.5 if x > 50 else x ** 0.9
composite_score = nonlinear_correction(adjusted_energy)

harmonic_weight = round(composite_score, 3)

# Print final result
print(f"Result: {harmonic_weight}")