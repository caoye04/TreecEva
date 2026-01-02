def analyze_production_efficiency():
    raw_data = [124, 87, 156, 203, 98, 142, 111]
    adjustments = [0.9, 1.1, 0.95, 1.0, 1.05, 0.98, 1.02]
    
    # Irrelevant transformation - case conversion on numeric identifiers
    item_codes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    upper_codes = [code.lower() for code in item_codes]  # Distractor: unused lower conversion
    reverse_map = {i: code.upper() for i, code in enumerate(item_codes)}  # Unused mapping
    
    # Tracking variables with some red herrings
    total_output = 0
    temp_buffer = []
    peak_count = 0
    cycle_time = len(raw_data) * 1.5
    
    # Simulate adjusted output with filtering
    for i, (value, adj) in enumerate(zip(raw_data, adjustments)):
        adjusted_value = value * adj
        
        # Filtering logic based on threshold
        if adjusted_value > 100:
            total_output += int(adjusted_value // 1)  # Integer division
            temp_buffer.append(adjusted_value)
            
            # Nested check for high performers
            if adjusted_value > 150:
                peak_count += 1
                if i % 2 == 0:
                    total_output -= 5  # Small correction for even indices
    
    # Secondary computation - not directly affecting result but adds complexity
    average_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    fluctuation_index = max(temp_buffer) - min(temp_buffer)
    
    # Key statement: efficiency score calculation
    efficiency_score = total_output / (cycle_time * 0.75)
    
    # Dead code path - never executed unless data changes
    if len(raw_data) > 20:
        fallback_metric = sum(raw_data) / 1000
        efficiency_score = fallback_metric
    
    # Final adjustment based on peak performance (unused branch)
    if peak_count >= 10:
        efficiency_score *= 1.2
    
    print(f"Result: {efficiency_score}")

analyze_production_efficiency()