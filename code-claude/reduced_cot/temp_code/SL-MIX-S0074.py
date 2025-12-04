def calculate_mountain_stats(peaks, base_height=1000):
    # Track highest and lowest peaks for reference
    highest_peak = max(peaks) if peaks else 0
    lowest_peak = min(peaks) if peaks else 0
    
    # Calculate average elevation and apply normalization
    raw_elevations = [p + base_height for p in peaks]
    avg_elevation = sum(raw_elevations) / len(raw_elevations) if raw_elevations else 0
    
    # Apply terrain correction factor based on peak distribution
    terrain_factor = (highest_peak - lowest_peak) / 100 if highest_peak != lowest_peak else 1
    
    # Process elevations with lambda functions
    process_elevation = lambda x: int(x / terrain_factor) if terrain_factor > 0 else x
    filter_significant = lambda x: x > avg_elevation / 2
    
    # Calculate primary and secondary metrics
    processed_elevations = [process_elevation(e) for e in raw_elevations]
    significant_elevations = [e for e in processed_elevations if filter_significant(e)]
    
    # Terrain complexity score (not used in final calculation)
    complexity = len([p for p in peaks if p > 50]) / len(peaks) if peaks else 0
    weather_impact = 15 if complexity > 0.5 else 0
    
    # Calculate the main elevation value
    actual_elevation = int(sum(significant_elevations) / len(significant_elevations)) if significant_elevations else 0
    
    # Apply seasonal adjustment (unnecessary calculation)
    seasonal_factor = lambda season: 1.1 if season == 'winter' else 0.9 if season == 'summer' else 1.0
    seasonal_adjustment = seasonal_factor('spring') * 10
    
    # Final elevation calculation with adjustment
    elevation_adjustment = int((highest_peak - lowest_peak) / 20)
    final_elevation = actual_elevation - elevation_adjustment
    
    return final_elevation

# Mountain peak heights relative to base (in meters)
mountain_peaks = [120, 340, 225, 190, 280]

# Calculate and output the result
result = calculate_mountain_stats(mountain_peaks)
print(f"Result: {result}")