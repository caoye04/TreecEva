# Spectral Analysis System
# This program processes spectral data from a fictional instrument

def analyze_noise(spectrum):
    # Calculate noise level in spectrum (distractor function)
    noise_sum = 0
    for i in range(len(spectrum) - 1):
        noise_sum += abs(spectrum[i] - spectrum[i+1])
    return noise_sum / (len(spectrum) - 1)

def calibrate_spectrum(raw_values, reference_points):
    # Distractor function that appears to calibrate values
    calibrated = []
    for val in raw_values:
        adjusted = val * reference_points[0] / reference_points[-1]
        calibrated.append(adjusted + reference_points[1])
    return calibrated

# Main data processing
data_series = [42, 39, 56, 27, 68, 53, 71, 82, 36, 48, 91, 55, 44, 39, 27]
reference_wavelengths = [435.8, 546.1, 578.2]

# Distractor variables and calculations
signal_to_noise = 12.5
baseline = sum(data_series[:3]) / 3
max_intensity = max(data_series)
min_intensity = min(data_series)
dynamic_range = max_intensity / min_intensity

# Processing parameters
start_idx = 2
end_idx = 14
step = 3

# More distractor calculations
temperature_correction = 0.97
humidity_factor = 1.03
optical_density = 0.5 * baseline / signal_to_noise

# Extract relevant data subset with slicing
subset = data_series[start_idx:end_idx:step]

# Distracting operation that looks important
processed_values = []
for i, val in enumerate(subset):
    if i % 2 == 0:
        processed_values.append(val * temperature_correction)
    else:
        processed_values.append(val * humidity_factor)

# Calibration factors
calibration_factor = 0.25
distractor_factor = 1.75

# Calculate statistics on processed data (distractors)
mean_value = sum(processed_values) / len(processed_values)
variance = sum((x - mean_value) ** 2 for x in processed_values) / len(processed_values)

# Misleading calculation that looks like it might be relevant
potential_wavelength = subset[0] * calibration_factor * optical_density

# The critical calculation we're asking about
final_wavelength = data_series[start_idx:end_idx:step][-1] * calibration_factor

# More distractor calculations after the target value is computed
adjusted_wavelength = final_wavelength * temperature_correction / humidity_factor
wavelength_index = int(final_wavelength / 10) if final_wavelength > 0 else 0

if wavelength_index < len(reference_wavelengths):
    reference_value = reference_wavelengths[wavelength_index]
else:
    reference_value = reference_wavelengths[-1]

# Printing results
print(f"Baseline: {baseline}")
print(f"Dynamic range: {dynamic_range}")
print(f"Mean processed value: {mean_value}")
print(f"Target result: {final_wavelength}")