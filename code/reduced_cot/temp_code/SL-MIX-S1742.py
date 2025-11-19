import statistics
from collections import defaultdict

class SensorCalibrationContext:
    def __init__(self, factors):
        self.factors = factors
        self.adjusted_factors = {}
    
    def __enter__(self):
        return self.factors
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Apply adjustment if needed
        variance = statistics.variance(self.factors.values())
        if variance > 2.0:
            adjustment = 0.5 if variance > 5 else 0.2
            for sensor_id in self.factors:
                self.adjusted_factors[sensor_id] = self.factors[sensor_id] + adjustment
        else:
            self.adjusted_factors = self.factors.copy()

# Sensor data: sensor_id -> [readings]
sensor_data = {
    'THERMAL_01': [23.4, 23.8, 24.1, 23.9],
    'THERMAL_02': [19.2, 19.5, 19.3, 19.7],
    'THERMAL_03': [25.1, 25.3, 25.0, 25.2]
}

# Initial calibration factors
initial_calibrations = {
    'THERMAL_01': 1.02,
    'THERMAL_02': 0.98,
    'THERMAL_03': 1.05
}

adjusted_calibration_sum = 0.0

with SensorCalibrationContext(initial_calibrations) as cal_factors:
    calibrated_readings = []
    for sensor_id, readings in sensor_data.items():
        avg_reading = statistics.mean(readings)
        calibrated_value = avg_reading * cal_factors[sensor_id]
        calibrated_readings.append(calibrated_value)
    
    overall_mean = statistics.mean(calibrated_readings)
    overall_variance = statistics.variance(calibrated_readings)
    
    # Determine if we need to adjust based on overall stats
    needs_adjustment = overall_variance > 1.5
    
    # Apply adjustment to calibration factors
    for sensor_id in cal_factors:
        adjustment_factor = 0.1 if needs_adjustment else 0.0
        final_calibration = cal_factors[sensor_id] + adjustment_factor
        adjusted_calibration_sum += final_calibration

print(f"Result: {adjusted_calibration_sum}")