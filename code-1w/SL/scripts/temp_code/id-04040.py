def main():
    # System calibration parameters (some are distractions)
    base_frequency = 440.23
    signal_buffer = [0.1, 0.3, 0.5, 0.7, 0.9]
    adjustment_factor = 1.87
    max_iterations = 15
    
    # Core variables for computation
    raw_metrics = [3, 7, 2, 8, 5, 9, 1]
    filtered_data = [x for x in raw_metrics if x > 4]
    logic_weight = sum(filtered_data) * 0.5
    
    # Distractor: irrelevant signal processing simulation
    processed_signals = []
    for i in range(len(signal_buffer)):
        temp_val = signal_buffer[i] * base_frequency
        if temp_val > 300:
            processed_signals.append(temp_val % 50)
    
    # Lambda function used in actual logic (required feature)
    threshold_func = lambda x: x ** 0.5 if x > 6 else x / 2
    
    # Helper function that appears complex but is deterministic
    def calculate_efficiency(weight, threshold_op):
        initial = weight + 10
        if initial > 20:
            intermediate = 0
            for val in filtered_data:
                if threshold_op(val) > 2:
                    intermediate += val // 2
            result = intermediate * adjustment_factor  # Uses distraction variable
        else:
            result = weight * 1.5
        
        # Dead code path - never executed due to logic above
        if len(processed_signals) > 100:
            fallback = sum(processed_signals) / 1000
            return fallback
            
        return result + 5  # Final adjustment

    # Irrelevant sequence generation
    sequence_cache = []
    for n in range(3):
        seq = [i * (n+1) for i in range(5)]
        sequence_cache.append(seq)
    
    # Key assignment - target of evaluation
    thermal_capacity = calculate_efficiency(logic_weight, threshold_func)
    
    # Additional red herring calculation
    diagnostic_score = len(sequence_cache) * adjustment_factor
    if diagnostic_score > 5:
        diagnostic_score -= 2.7

    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()