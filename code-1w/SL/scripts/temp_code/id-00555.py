def main():
    base_temperature = 36.5
    fluctuation_data = [1.2, -0.8, 0.5, -1.0, 0.3]
    
    # Calculate average deviation
    total_deviation = sum(abs(x) for x in fluctuation_data)
    avg_deviation = total_deviation / len(fluctuation_data)
    
    # Determine initial alert level based on thresholds
    if avg_deviation > 1.0:
        threshold_alert = 2
    elif avg_deviation > 0.5:
        threshold_alert = 1
    else:
        threshold_alert = 0
    
    # Irrelevant distraction: unused health metric
    peak_reading = max(fluctuation_data)
    baseline_stability = base_temperature + 0.1  # Not used
    
    # Performance checker using lambda
    performance_checker = lambda x: x * 2 if x > 0 else 0
    final_evaluation = performance_checker(threshold_alert)
    
    # Output target result
    print(f"Result: {threshold_alert}")

if __name__ == "__main__":
    main()