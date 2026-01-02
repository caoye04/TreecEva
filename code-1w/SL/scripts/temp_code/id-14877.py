def main():
    # Sensor data from a thermal system
    raw_readings = [23.5, 19.8, 21.0, 24.2, 18.7]
    
    # Apply calibration factor using lambda
    calibrate = lambda x: x * 1.02 + 0.5
    corrected_readings = [calibrate(val) for val in raw_readings]
    
    # Identify stable readings (within normal operating range)
    filtered_readings = [val for val in corrected_readings if 20.0 <= val <= 25.0]
    
    # Transform data for efficiency calculation
    transformed_data = sum(filtered_readings) / len(filtered_readings)
    
    # Efficiency model: logarithmic scaling with small offset
    def calculate_efficiency(avg_temp):
        import math
        return math.log(avg_temp) * 10
    
    energy_output = calculate_efficiency(transformed_data)
    print(f"Result: {energy_output}")

if __name__ == "__main__":
    main()