import math

# Simulated satellite spectral band data (irrelevant initialization)
spectral_bands = [450, 530, 670, 780, 860, 1200, 1600, 2200]
band_weights = [0.1, 0.15, 0.2, 0.18, 0.12, 0.1, 0.08, 0.07]
decoys = [x ** 2 for x in range(10)]  # Irrelevant list comprehension

# Environmental constants (some irrelevant)
atmospheric_transmittance = 0.87
target_elevation = 34.5  # Unused
surface_albedo = 0.32      # Unused

# Calibration factors (mixed relevance)
calibration_matrix = {i: math.log(w * 10 + 1) for i, w in enumerate(band_weights)}
offset_map = {i: (i % 3) * 0.05 for i in range(len(spectral_bands))}

# Decoy function – never called
def analyze_vegetation_index(bands):
    ndvi = (bands[3] - bands[2]) / (bands[3] + bands[2])
    return round(ndvi * 1000)

# Another decoy – looks important but unused
temporal_cache = {}
for idx, val in enumerate(spectral_bands):
    temporal_cache[idx] = math.sin(val / 100) * calibration_matrix[idx]

# Real processing begins here
weighted_sum = sum(w * b for w, b in zip(band_weights, spectral_bands))
mean_band = sum(spectral_bands) / len(spectral_bands)
adjusted_bands = [b - mean_band + 100 for b in spectral_bands]  # Centering

# Apply non-linear response curve (only some bands matter)
nonlinear_response = []
for i, ab in enumerate(adjusted_bands):
    if i in {2, 4, 5, 6}:  # Only specific indices contribute
        if ab > 0:
            response = ab * math.sqrt(calibration_matrix[i])
        else:
            response = ab
        nonlinear_response.append(response)
    else:
        # Dead path: values not used later
        fake_response = ab * 0.1
        nonlinear_response.append(fake_response)  # Distractor assignment

# Filter and transform (list comprehension with filtering)
effective_signals = [sig for sig in nonlinear_response if abs(sig) > 50]

# Simulated atmospheric correction (irrelevant variables introduced)
correction_factor = 1.0
for i in range(3):  # Dummy loop
    correction_factor *= 0.995

# Actual signal integration
integration_key = 0
for i, sig in enumerate(effective_signals):
    integration_key += sig * (i + 1)  # Weight by position

# Hash-like transformation using dictionary lookup
signature_lookup = {i: math.tanh(val / 100) for i, val in enumerate(effective_signals)}
raw_signature = sum(signature_lookup[k] for k in signature_lookup)

# Secondary decoy: complex bit manipulation with no impact
bit_fiddling = 0
for x in [int(w * 100) for w in band_weights]:
    bit_fiddling ^= (x << 2) | (x >> 1)
bit_fiddling = bit_fiddling & 0xFFFF  # Mask to 16 bits, unused

# Critical function definition
def calculate_thermal_signature(bands):
    base = sum(bands[i] * 0.7 for i in range(len(bands)) if i % 2 == 0)
    penalty = 0
    for i in range(1, len(bands), 2):
        if bands[i] < 0:
            penalty += abs(bands[i]) * 0.1
    adjusted_base = base - penalty
    normalized = adjusted_base / 1.8
    return round(normalized, 4)

# Processing step chain
intermediate_frame = [math.log(abs(x) + 1) for x in effective_signals]
processed_bands = [int(x * 2.1) for x in intermediate_frame]

# Key assignment point
thermal_quotient = calculate_thermal_signature(processed_bands)

# Red herring: another variable that looks like answer
spectral_entropy = sum(math.log(abs(x) + 1) for x in processed_bands) / len(processed_bands)

# Final output
Result: thermal_quotient