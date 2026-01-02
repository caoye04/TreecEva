def analyze_production_cycles():
    raw_data = [15, 23, 17, 44, 19, 31, 27]
    thresholds = [18, 25, 30, 40]
    
    # Irrelevant preprocessing: normalize data (not used in final logic)
    normalized = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)), 3) for x in raw_data]
    
    # Distractor variables
    peak_count = 0
    rolling_avg = 0.0
    temp_buffer = []
    
    total_output = 0
    cycle_count = 0
    efficiency_score = 0
    
    # Simulate multi-phase production analysis
    for i, output in enumerate(raw_data):
        if output >= thresholds[0]:
            phase_flags = []
            for j, thresh in enumerate(thresholds):
                if output >= thresh:
                    phase_flags.append(True)
                else:
                    phase_flags.append(False)
            
            # Only count cycles meeting early-stage threshold
            if phase_flags[0] and not phase_flags[-1]:
                total_output += output * (i + 1)  # Weight by time index
                cycle_count += 1
            
            # Dead code path: never executed due to condition mismatch
            if output < 0:
                temp_buffer.append(output)
                rolling_avg = sum(temp_buffer) / len(temp_buffer)
        
        # Extra computation: track peaks above secondary threshold
        if output > thresholds[1]:
            peak_count += 1

    # Key statement with target variable
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0
    
    # Print result for execution verification
    print(f"Result: {efficiency_score}")
    
    return efficiency_score

analyze_production_cycles()