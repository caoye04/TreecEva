from collections import Counter, defaultdict
import math

def analyze_frequency_band(frequencies, noise_threshold=0.3):
    # Analyze frequency distribution and return metrics
    freq_counter = Counter(frequencies)
    dominant_freq = freq_counter.most_common(1)[0][0] if freq_counter else 0
    noise_level = sum(freq_counter.values()) / len(frequencies) if frequencies else 0
    return {'dominant': dominant_freq, 'noise': noise_level * noise_threshold}

def calculate_transmission_efficiency(power_levels, distance_factors):
    # Calculate efficiency based on power and distance
    if not power_levels or not distance_factors:
        return 0.0
    
    efficiency_map = defaultdict(float)
    for p, d in zip(power_levels, distance_factors):
        key = p // 10  # Bucket by power level
        efficiency_map[key] += (p / (d ** 2)) if d > 0 else p
    
    # Return max efficiency (not actually used in main calculation)
    return max(efficiency_map.values()) if efficiency_map else 0.0

def apply_atmospheric_correction(signal_value, humidity, temperature):
    # Apply atmospheric corrections to signal
    correction_factor = 1.0
    if humidity > 0.7:
        correction_factor *= 0.85
    elif humidity < 0.3:
        correction_factor *= 1.15
    
    # Temperature adjustment (not actually used)
    temp_factor = 1 + (temperature - 20) * 0.01
    
    return signal_value * correction_factor

def calculate_signal_metric(frequency_data, power):
    # Main calculation function
    base_signal = 0
    frequency_sum = sum(f for f in frequency_data if 30 <= f <= 70)
    
    modulation_factor = 2.5
    interference_level = len([f for f in frequency_data if f < 20 or f > 80])
    
    # This is the critical calculation path
    base_signal = frequency_sum * power / 100
    
    # Apply modulation (distractor - not used in final calculation)
    modulated_signal = base_signal * modulation_factor
    
    # Apply interference reduction
    adjusted_signal = base_signal - (interference_level * 1.5)
    
    # Calculate bitwise components (distractor)
    bit_factor = power & 0x0F  # Get lower 4 bits
    
    # Final calculation with bitwise component
    return max(0, adjusted_signal + (bit_factor / 2))

# Main signal processing
raw_frequencies = [45, 67, 32, 58, 72, 15, 92, 23, 45, 67, 33]
power_values = [120, 95, 150, 80, 110]
distances = [2, 4, 3, 5, 1]

# Environmental factors (distractors)
humidity_readings = [0.65, 0.72, 0.68, 0.75, 0.70]
avg_humidity = sum(humidity_readings) / len(humidity_readings)
temperatures = [22.5, 23.1, 21.8, 22.0, 23.4]
avg_temperature = sum(temperatures) / len(temperatures)

# Process frequency data
frequency_analysis = analyze_frequency_band(raw_frequencies)
dominant_frequency = frequency_analysis['dominant']
noise_level = frequency_analysis['noise']

# Calculate transmission metrics (distractor)
transmission_efficiency = calculate_transmission_efficiency(power_values, distances)

# Filter frequencies based on dominant frequency
filtered_frequencies = [f for f in raw_frequencies if abs(f - dominant_frequency) <= 25]

# Determine power level based on conditions
transmission_power = 100  # Default
if dominant_frequency > 60:
    transmission_power = 120
elif dominant_frequency < 40:
    transmission_power = 80

# Calculate signal strength with atmospheric correction
raw_signal = sum(filtered_frequencies) / len(filtered_frequencies) if filtered_frequencies else 0
corrected_signal = apply_atmospheric_correction(raw_signal, avg_humidity, avg_temperature)

# Apply conditional processing
processed_signal = corrected_signal * (1.2 if noise_level < 10 else 0.8)

# Generate potential signal metrics (distractors)
potential_metrics = {
    'standard': processed_signal * 1.5,
    'enhanced': processed_signal * 2.0 - noise_level,
    'reduced': processed_signal * 0.75 + dominant_frequency / 10
}

# Calculate final signal strength
final_signal_strength = calculate_signal_metric(filtered_frequencies, transmission_power)

# Print results
print(f"Frequency Analysis: {frequency_analysis}")
print(f"Filtered Frequencies: {filtered_frequencies}")
print(f"Transmission Power: {transmission_power}")
print(f"Potential Metrics: {potential_metrics}")
print(f"Result: {final_signal_strength}")