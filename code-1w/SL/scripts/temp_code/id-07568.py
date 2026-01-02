def evaluate_performance():
    # Simulate geographic zones with high foot traffic
    high_traffic_areas = set(range(10, 26))  # Zones 10-25
    
    # Identify zones where service response time is under threshold
    fast_response_zones = set(range(5, 20))   # Zones 5-19
    
    # Calculate overlap: areas with both high traffic and fast response
    optimal_coverage = high_traffic_areas.intersection(fast_response_zones)
    
    # Define passing performance as meeting minimum coverage threshold
    passing_zones = {zone for zone in optimal_coverage if zone > 12}
    
    # Efficient zones are those divisible by 3 within a strategic region
    efficient_zones = set(x for x in range(12, 30) if x % 3 == 0)
    
    # Final evaluation score based on intersection of passing and efficient zones
    final_score = len(passing_zones.intersection(efficient_zones))
    
    # Irrelevant tracking variable (minimal distraction)
    audit_log = [f'Zone-{z}' for z in sorted(high_traffic_areas)]
    
    print(f'Result: {final_score}')

evaluate_performance()