def analyze_system_efficiency():
    base_frequency = 2.4
    peak_frequency = 3.8
    
    # Simulated sensor readings for thermal loads (in degrees Celsius)
    thermal_loads = [22.5, 30.1, 25.8, 33.4, 28.9]
    avg_load = sum(thermal_loads) / len(thermal_loads)
    
    # Operational thresholds based on frequency scaling
    normal_op = base_frequency * 0.75
    boosted_op = peak_frequency * 1.15
    
    # Performance ratings under different conditions (unitless score)
    performance_scores = [normal_op * 1.2, boosted_op * 0.85, base_frequency * 1.5]
    operational_ratings = [score * 2.1 for score in performance_scores]
    
    # Calculate safety margin: difference between minimum acceptable rating and worst-case load
    thermal_margin = min(operational_ratings) - max(thermal_loads)
    
    # Irrelevant diagnostic string (minimal distraction)
    status_report = "System nominal".upper().replace(" ", "_")
    report_length = len(status_report)
    
    # Final result output
    print(f"Result: {thermal_margin}")

analyze_system_efficiency()