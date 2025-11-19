import re
import math

def temperature_correction(temp_celsius):
    return 1.0 + (temp_celsius - 20.0) * 0.02

class SalinityAdjuster:
    def __init__(self):
        self.baseline_salinity = 35.0
    
    def adjust_for_salinity(self, current_salinity):
        return current_salinity / self.baseline_salinity

def process_sonar_data(readings_log):
    adjuster = SalinityAdjuster()
    corrected_readings = []
    
    for entry in readings_log:
        temp_match = re.search(r'T:(\d+\.\d+)', entry)
        salinity_match = re.search(r'S:(\d+\.\d+)', entry)
        signal_match = re.search(r'Signal:(\d+\.\d+)', entry)
        
        if temp_match and salinity_match and signal_match:
            temp = float(temp_match.group(1))
            salinity = float(salinity_match.group(1))
            signal = float(signal_match.group(1))
            
            temp_factor = temperature_correction(temp)
            salinity_factor = adjuster.adjust_for_salinity(salinity)
            corrected_signal = signal * temp_factor * salinity_factor
            corrected_readings.append(corrected_signal)
    
    return corrected_readings

data_log = [
    "T:18.5 S:34.2 Signal:45.7",
    "T:19.2 S:35.0 Signal:47.3",
    "T:21.0 S:36.1 Signal:44.8",
    "T:22.3 S:34.8 Signal:46.9",
    "T:20.7 S:35.5 Signal:48.2"
]

corrected_values = process_sonar_data(data_log)
weighted_sum = sum(val * math.log(i+2) for i, val in enumerate(corrected_values))
pod_migration_index = round(weighted_sum / len(corrected_values), 3)

print(f"Result: {pod_migration_index}")