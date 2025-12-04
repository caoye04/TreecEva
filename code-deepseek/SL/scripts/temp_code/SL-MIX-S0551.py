def coverage_analysis():
    regions = [45, 78, 23, 91, 67, 34, 56, 89, 12, 77]
    threshold = 50
    
    # Calculate coverage metrics
    high_coverage = [r for r in regions if r > threshold]
    low_coverage = [r for r in regions if r <= threshold]
    
    # Distractor calculations that don't affect final result
    total_regions = len(regions)
    avg_high = sum(high_coverage) / len(high_coverage) if high_coverage else 0
    avg_low = sum(low_coverage) / len(low_coverage) if low_coverage else 0
    
    # More distractors
    coverage_ratio = len(high_coverage) / total_regions if total_regions else 0
    potential_gain = sum([max(0, threshold - r) for r in low_coverage])
    
    # Core logic - only this affects final result
    qualified_regions = len([r for r in regions if r > 75])
    bonus_coverage = sum([r - 60 for r in regions if r > 60])
    
    # Final calculation
    coverage_score = qualified_regions * 10 + bonus_coverage
    
    # Additional irrelevant operations
    temp_metric = (avg_high + avg_low) / 2
    efficiency_factor = coverage_ratio * 100
    
    return coverage_score

final_coverage = coverage_analysis()
print(f"Result: {final_coverage}")