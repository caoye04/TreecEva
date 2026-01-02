def analyze_network_security():
    expected_ports = {22, 25, 53, 80, 110, 143, 443, 993, 995}
    active_ports = {22, 80, 443, 53}
    
    # Log current scan timestamp (irrelevant to result)
    scan_timestamp = 1712049600
    
    # Determine which required ports are not actively secured
    coverage_gaps = expected_ports - active_ports
    
    # Additional diagnostic info (not used in computation)
    gap_count = len(coverage_gaps)
    
    # Output result as required
    print(f"Result: {coverage_gaps}")

analyze_network_security()