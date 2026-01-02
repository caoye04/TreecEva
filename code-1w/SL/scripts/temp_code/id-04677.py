def main():
    # Sensor readings and calibration logic
    raw_readings = [23.5, 34.2, 18.9, 45.1, 29.8]
    base_offset = 1.2

    # Compute average with adjustment
    adjusted_sum = sum(x + base_offset for x in raw_readings)
    avg_reading = adjusted_sum / len(raw_readings)

    # Define dynamic threshold based on spread
    deviation_factor = max(raw_readings) - min(raw_readings)
    threshold_score = avg_reading + (deviation_factor * 0.1)

    # Calibration function using lambda
    apply_calibration = lambda x: x * 0.98 if x > 30 else x * 1.02

    # Apply final calibration
    final_diagnostic = apply_calibration(threshold_score)

    # Irrelevant auxiliary variable (minor distraction)
    status_flag = 'NORMAL'

    print(f'Result: {threshold_score}')

if __name__ == '__main__':
    main()