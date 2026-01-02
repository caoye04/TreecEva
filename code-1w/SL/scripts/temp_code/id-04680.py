def calculate_system_load(baseline, processes, overhead_factor=1.2):
    total_load = sum(processes) * overhead_factor + baseline
    peak_capacity = 500
    normalized_load = total_load / peak_capacity * 10
    
    # Irrelevant tracking variables (minimal distraction)
    status_flags = [False, True, False]
    cycle_count = len(processes)
    
    # Key computation with bitwise adjustment
    if cycle_count & 1:
        normalized_load ^= 3  # XOR adjustment for odd process counts
    
    # Conditional clamping
    if normalized_load > 7:
        threshold_alert = 9
    else:
        threshold_alert = 5
    
    # Final override based on clamped value
    threshold_alert = max(0, min(normalized_load, 10))
    
    # Additional benign operations
    final_diagnostic = f"LoadOK={threshold_alert < 8}"
    return threshold_alert

# Input data
active_processes = [23, 45, 67, 12, 89]
base = 20

result = calculate_system_load(base, active_processes)
print(f"Target result: {result}")