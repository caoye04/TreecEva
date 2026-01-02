def analyze_system_status():
    # System zone codes and active alert regions
    operational_zones = {f'Z{num}' for num in range(101, 115)}
    maintenance_zones = {f'Z{num}' for num in range(105, 120, 2)}
    
    # Simulate filtered valid access codes from security module
    raw_codes = ['Z101', 'Z102', 'Z103', 'Z106', 'Z108', 'Z110', 'Z112', 'Z114']
    valid_codes = set(raw_codes)
    
    # Current environmental alerts in specific zones
    alert_zones = {code for code in operational_zones if '4' in code or '6' in code}
    alert_zones.update(maintenance_zones.intersection({f'Z{num}' for num in [106, 110, 114]}))
    
    # Critical safety check: count overlapping zones between valid access and alerts
    final_count = len(valid_codes.intersection(alert_zones))
    
    # Log result
    print(f"Result: {final_count}")

analyze_system_status()