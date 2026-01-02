import math

# Simulated sensor data from a thermal imaging array
temperature_readings = [23.4, 25.1, 24.8, 26.7, 22.9, 27.3, 28.0, 25.6, 24.2, 26.1]

def preprocess_sensor_array(raw_input):
    # Irrelevant transformation: normalize to z-score (not used in final result)
    mean_val = sum(raw_input) / len(raw_input)
    std_dev = (sum((x - mean_val) ** 2 for x in raw_input) / len(raw_input)) ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in raw_input]  # Dead end

    # Relevant path: filter anomalies above 27.0
    filtered_data = [temp for temp in raw_input if temp <= 27.0]

    # Distractor: apply arbitrary weighting (unused)
    weighted_values = list(map(lambda t: t * 1.05 if t < 24.0 else t * 0.98, raw_input))

    # Correct preprocessing: scale by logarithmic factor only on valid entries
    scaled_data = [math.log(temp) * 10 for temp in filtered_data]
    return scaled_data

# Misleading intermediate analysis (never called)
def legacy_diagnostic(data):
    return sum([d**2 for d in data]) / len(data)

# Auxiliary function for noise estimation (irrelevant)
def estimate_noise_floor(signal):
    peak = max(signal)
    floor = min(signal)
    return (peak - floor) * 0.01  # Not used anywhere

# Core signal analysis logic
def analyze_signal(cleaned_signal):
    # Apply windowing function (distraction: not affecting final computation)
    windowed = [cleaned_signal[i] * (1 - abs(i - len(cleaned_signal)//2) / len(cleaned_signal)) 
                for i in range(len(cleaned_signal))]

    # Red herring: FFT simulation (unused result)
    fft_magnitude = sum([abs(math.sin(x) + math.cos(x)) for x in cleaned_signal])

    # Actual diagnostic formula: sum of even-indexed elements minus odd-indexed ones
    even_sum = sum(cleaned_signal[i] for i in range(0, len(cleaned_signal), 2))
    odd_sum = sum(cleaned_signal[i] for i in range(1, len(cleaned_signal), 2))
    primary_metric = even_sum - odd_sum

    # Final adjustment using character count from metadata (hidden dependency)
    metadata_tag = 'THERMAL_DIAG_V2'
    adjustment_factor = len([c for c in metadata_tag if c in 'AEIOU'])  # Count vowels

    final_diagnostic = int(primary_metric + adjustment_factor)
    return final_diagnostic

# Unused backup method
def fallback_reconstruction(seq):
    return sum(seq[i] * (-1)**i for i in range(len(seq)))

# Execution pipeline
processed_data = preprocess_sensor_array(temperature_readings)
noise_level = estimate_noise_floor(temperature_readings)  # Dead assignment
legacy_score = legacy_diagnostic(processed_data)  # Unused metric

# Critical execution point
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")