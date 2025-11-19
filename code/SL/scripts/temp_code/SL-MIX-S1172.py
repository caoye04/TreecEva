import math
from collections import defaultdict
from functools import wraps

def compute_intensity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@compute_intensity
def calculate_wave_superposition(frequencies, damping_factors):
    total_energy = 0.0
    phase_map = defaultdict(list)
    
    for i, freq in enumerate(frequencies):
        # Calculate logarithmic energy scaling
        log_energy = math.log(freq + 1) * damping_factors[i]
        total_energy += log_energy
        
        # Map phases based on frequency relationships
        for j in range(i+1, len(frequencies)):
            phase_diff = abs(freq - frequencies[j])
            if phase_diff > 0:
                phase_map[freq].append(math.exp(-phase_diff))
    
    # Calculate statistical measures
    phase_values = [item for sublist in phase_map.values() for item in sublist]
    if not phase_values:
        return 0.0
    
    mean_phase = sum(phase_values) / len(phase_values)
    variance = sum((x - mean_phase) ** 2 for x in phase_values) / len(phase_values)
    
    # Apply number theory for harmonic relationships
    gcd_all = frequencies[0]
    for f in frequencies[1:]:
        gcd_all = math.gcd(int(gcd_all), int(f))
    
    # Final metric combines all factors
    interference_metric = total_energy * math.sqrt(variance) * math.log(gcd_all + 2)
    return interference_metric

# Research parameters
acoustic_frequencies = [120.5, 240.0, 360.5, 480.0, 600.5]
damping_coefficients = [0.8, 0.6, 0.9, 0.7, 0.5]

final_interference_metric = calculate_wave_superposition(acoustic_frequencies, damping_coefficients)
print(f"Result: {final_interference_metric}")