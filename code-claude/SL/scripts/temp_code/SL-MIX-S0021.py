# Function to analyze geographic data regions for environmental monitoring

def calculate_region_metrics(primary_data, secondary_data):
    # Primary data regions (coordinates as tuples)
    primary_regions = {(x, y) for x, y in primary_data}
    
    # Secondary data contains both active and inactive monitoring stations
    active_stations = {coord for coord, status in secondary_data.items() if status == 'active'}
    inactive_stations = {coord for coord, status in secondary_data.items() if status == 'inactive'}
    
    # Transform coordinates for active regions (shift by 2 units in both directions)
    active_regions = {(x+2, y+2) for x, y in active_stations}
    
    # Calculate potential monitoring zones
    candidate_regions = set()
    for x, y in primary_regions:
        if x % 2 == 0 and y % 3 == 0:  # Only select regions with specific coordinates
            candidate_regions.add((x, y))
    
    # Weather condition factor (doesn't affect final calculation)
    weather_factor = 0.75
    adjusted_stations = len(active_stations) * weather_factor
    
    # Calculate region density (unused in final answer)
    density = len(primary_regions) / (max(coord[0] for coord in primary_regions) * 
                                     max(coord[1] for coord in primary_regions))
    
    # Find overlapping regions between active and candidate regions
    overlap_size = len(active_regions.intersection(candidate_regions))
    
    # Calculate coverage percentage (not used in final result)
    if len(candidate_regions) > 0:
        coverage = (overlap_size / len(candidate_regions)) * 100
    else:
        coverage = 0
        
    return overlap_size

# Test data
primary_data = [(2, 3), (4, 6), (6, 3), (8, 9), (10, 12), (12, 15)]
secondary_data = {
    (0, 1): 'active',
    (2, 1): 'inactive',
    (4, 4): 'active',
    (6, 1): 'active',
    (8, 7): 'inactive',
    (10, 10): 'active'
}

# Execute analysis
result = calculate_region_metrics(primary_data, secondary_data)
print(f"Result: {result}")