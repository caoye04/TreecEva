def calculate_peak_load():
    system_loads = [12, 15, 10, 23, 18, 27, 20, 14, 19, 22]
    maintenance_mode = True
    threshold = 25
    active_window = slice(2, 7)
    
    # Extract current operational segment
    current_segment = system_loads[active_window]
    
    # Calculate average load during active window
    avg_load = sum(current_segment) / len(current_segment)
    
    # Determine peak capacity in active window
    peak_capacity = max(system_loads[active_window])
    
    # Dummy variable for minor interference (LOW intervention)
    safety_margin = 1.1 if maintenance_mode else 1.3
    
    # Return result
    print(f"Result: {peak_capacity}")

# Execute function
calculate_peak_load()