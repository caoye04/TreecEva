def main():
    # Sensor readings and calibration parameters
    raw_readings = [23.4, 19.5, 20.1, 25.3, 18.7]
    base_offset = 1.8
    
    # Compute dynamic threshold based on filtered readings
    filtered_readings = list(filter(lambda x: x > 20.0, raw_readings))
    avg_reading = sum(filtered_readings) / len(filtered_readings)
    
    # Apply safety margin and offset
    threshold_score = avg_reading * 0.9 + base_offset
    
    # Calibration function for diagnostic systems
    def apply_calibration(value):
        adjustments = {"fine": 0.95, "coarse": 1.1}
        return value * adjustments["fine"] if value < 25 else value * adjustments["coarse"]
    
    final_diagnostic = apply_calibration(threshold_score)
    
    # Irrelevant tracking variable (minor distraction)
    reading_count = len(raw_readings)
    
    print(f"Result: {threshold_score}")

if __name__ == "__main__":
    main()