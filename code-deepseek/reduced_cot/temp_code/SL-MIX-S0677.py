def analyze_network_devices():
    # Network device inventory analysis
    department_a_devices = {'router-1', 'switch-2', 'server-3', 'firewall-4', 'switch-2', 'router-1'}
    department_b_devices = {'switch-2', 'server-3', 'workstation-5', 'router-6', 'server-3'}
    
    # Remove duplicates using sets
    unique_a = set(department_a_devices)
    unique_b = set(department_b_devices)
    
    # Find common devices between departments
    final_intersection = unique_a.intersection(unique_b)
    
    # Calculate result based on intersection size
    common_device_count = len(final_intersection)
    result = common_device_count * 25
    
    print(f"Result: {result}")
    return result

analyze_network_devices()