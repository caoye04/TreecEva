def analyze_system_performance(log_entries):
    total_chars = 0
    uppercase_count = 0
    valid_cycles = []
    temp_buffer = []
    cycle_count = 0
    total_output = 0
    efficiency_score = 0
    
    for entry in log_entries:
        if not entry.strip():
            continue
        
        # Irrelevant character analysis (distractor)
        total_chars += len(entry)
        uppercase_count += sum(1 for c in entry if c.isupper())
        
        # Core logic: extract performance cycles
        parts = entry.split('|')
        if len(parts) < 3:
            continue
            
        try:
            cycle_id = int(parts[0].strip())
            output_level = float(parts[1].strip())
            status_flag = parts[2].strip()
            
            if status_flag == 'ACTIVE':
                cycle_count += 1
                total_output += output_level
                valid_cycles.append((cycle_id, output_level))
                
                # Nested condition with dead computation (interference)
                if output_level > 50:
                    normalized = output_level / (cycle_id + 1)
                    temp_buffer.append(normalized * 0.1)  # Not used later
                    
        except ValueError:
            continue
    
    # Red herring: unused statistical calculation
    if valid_cycles:
        avg_cycle_id = sum(x[0] for x in valid_cycles) / len(valid_cycles)
        peak_output = max(x[1] for x in valid_cycles)
        fluctuation_index = (peak_output - avg_cycle_id) * 0.01  # Unused

    # Key statement
    efficiency_score = total_output / cycle_count if cycle_count > 0 else 0
    
    # Print result for evaluation
    print(f"Result: {efficiency_score}")

# Input data
logs = [
    "101|78.5|ACTIVE",
    "102|45.0|INACTIVE",
    "103|88.2|ACTIVE",
    "104|34.1|ACTIVE",
    "105|92.7|ACTIVE",
    "106|23.0|ACTIVE",
    "|55.5|ACTIVE",         # Invalid ID
    "108|77.8|ACTIVE",
    "abc|60.0|ACTIVE",     # Invalid ID
    "110|85.3|ACTIVE"
]

analyze_system_performance(logs)