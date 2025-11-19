import math
from collections import defaultdict

def calculate_skyline_visibility(buildings):
    n = len(buildings)
    if n <= 1:
        return n
    
    # Dynamic programming approach to find maximum visible buildings
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if buildings[j] < buildings[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def compute_geometric_visibility_area(heights):
    total_area = 0
    for i, h in enumerate(heights):
        base_width = 1.0
        left_shadow = sum(1 for j in range(i) if heights[j] >= h)
        right_shadow = sum(1 for j in range(i+1, len(heights)) if heights[j] >= h)
        effective_width = max(0, base_width - 0.1 * (left_shadow + right_shadow))
        total_area += h * effective_width
    return total_area

def optimize_visibility_index(areas, threshold=10.0):
    def backtrack(index, current_sum, count):
        if index == len(areas):
            return count if current_sum > threshold else 0
        
        # Include current area
        include = backtrack(index + 1, current_sum + areas[index], count + 1)
        # Exclude current area (short-circuit if sum already exceeds threshold)
        exclude = backtrack(index + 1, current_sum, count) if current_sum <= threshold else 0
        
        return max(include, exclude)
    
    return backtrack(0, 0, 0)

def main():
    building_heights = [3, 1, 4, 2, 5, 3, 6, 2, 4, 7]
    
    # Step 1: Calculate skyline visibility using DP
    max_visible_buildings = calculate_skyline_visibility(building_heights)
    
    # Step 2: Compute geometric visibility areas
    visibility_areas = []
    for i in range(len(building_heights)):
        subset = building_heights[:i+1]
        area = compute_geometric_visibility_area(subset)
        visibility_areas.append(area)
    
    # Step 3: Statistical analysis
    mean_area = sum(visibility_areas) / len(visibility_areas)
    variance = sum((x - mean_area) ** 2 for x in visibility_areas) / len(visibility_areas)
    
    # Step 4: Optimize visibility index using backtracking
    optimal_visibility_index = optimize_visibility_index(visibility_areas, mean_area + math.sqrt(variance))
    
    # Step 5: Apply set operations for final calculation
    high_rise_set = frozenset(i for i, h in enumerate(building_heights) if h > mean_area)
    visible_set = set(range(optimal_visibility_index))
    intersection_count = len(high_rise_set & visible_set)
    
    # Final calculation combining all factors
    final_metric = max_visible_buildings * optimal_visibility_index + intersection_count
    
    print(f"Result: {final_metric}")

if __name__ == "__main__":
    main()