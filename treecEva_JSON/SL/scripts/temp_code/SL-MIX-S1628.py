import math
from dataclasses import dataclass
from typing import List

def operation_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@dataclass
class SignalData:
    amplitude_values: List[float]
    frequency_components: List[float]
    
@operation_logger
def compute_spectral_density(signal: SignalData) -> float:
    # Calculate root mean square of amplitudes
    rms = math.sqrt(sum(x**2 for x in signal.amplitude_values) / len(signal.amplitude_values))
    # Calculate mean of frequency components
    mean_freq = sum(signal.frequency_components) / len(signal.frequency_components)
    return rms * mean_freq

@operation_logger
def apply_noise_filter(matrix_data: List[List[float]], threshold_set: frozenset) -> List[List[float]]:
    filtered_matrix = []
    for row in matrix_data:
        filtered_row = [val if int(val*10) not in threshold_set else 0.0 for val in row]
        filtered_matrix.append(filtered_row)
    return filtered_matrix

# Initialize sensor data
sensor_data = SignalData(
    amplitude_values=[2.5, 3.7, 1.2, 4.8, 2.1],
    frequency_components=[10.5, 15.2, 8.7, 12.3]
)

# Process matrix data
raw_matrix = [
    [1.5, 2.3, 3.7],
    [4.2, 5.1, 6.8],
    [7.3, 8.9, 9.4]
]

filter_thresholds = frozenset({23, 51, 89})

# Apply transformations
spectral_value = compute_spectral_density(sensor_data)
filtered_data = apply_noise_filter(raw_matrix, filter_thresholds)

# Further calculations
matrix_sum = sum(sum(row) for row in filtered_data)
adjusted_spectral = spectral_value * 1.5

# Final metric calculation
if matrix_sum > 30.0:
    correction_factor = math.log(matrix_sum) / math.log(10)
else:
    correction_factor = math.exp(matrix_sum / 100)
    
final_metric = adjusted_spectral + correction_factor
print(f"Result: {final_metric}")