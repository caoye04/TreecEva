def analyze_network_devices():
    device_types = ['router', 'switch', 'firewall', 'access_point', 'server']
    deployment_zones = ['core', 'distribution', 'access']
    
    # Calculate all possible device-zone combinations
    all_combinations = [(device, zone) for device in device_types for zone in deployment_zones]
    total_possible = len(all_combinations)
    
    # Apply deployment constraints (distractor: unused variable)
    constrained_pairs = [(d, z) for d, z in all_combinations if z != 'core' or d != 'access_point']
    temp_count = len(constrained_pairs)
    
    # Apply security restrictions
    high_security_zones = ['core', 'distribution']
    valid_combinations = [pair for pair in all_combinations if pair[1] in high_security_zones]
    
    # Calculate discount for router-switch pairs (distractor: unused calculation)
    discount_count = len([pair for pair in valid_combinations if pair[0] in ['router', 'switch']])
    
    # Apply bonus for firewall deployments
    bonus_count = len([pair for pair in all_combinations if pair[0] == 'firewall'])
    
    # Final calculation
    final_count = len(valid_combinations) - discount_count + bonus_count
    
    print(f"Result: {final_count}")
    return final_count

final_count = analyze_network_devices()