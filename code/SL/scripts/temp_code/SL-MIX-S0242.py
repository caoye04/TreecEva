from collections import defaultdict

def calculate_loading_efficiency(weights):
    # Step 1: Initialize containers
    weight_groups = defaultdict(list)
    efficiency_score = 0
    
    # Step 2: Group weights by their magnitude ranges
    for w in weights:
        if w < 10:
            weight_groups['light'].append(w)
        elif 10 <= w < 50:
            weight_groups['medium'].append(w)
        else:
            weight_groups['heavy'].append(w)
    
    # Step 3: Apply efficiency calculation for each group
    for group_name, group_weights in weight_groups.items():
        if not group_weights:
            continue
        
        # Sort weights in descending order for optimal loading
        group_weights.sort(reverse=True)
        
        # Calculate group efficiency using divide and conquer approach
        def group_efficiency(sub_weights):
            n = len(sub_weights)
            if n == 0:
                return 0
            if n == 1:
                return sub_weights[0] * 2
            
            mid = n // 2
            left_eff = group_efficiency(sub_weights[:mid])
            right_eff = group_efficiency(sub_weights[mid:])
            
            # Combine results with penalty for imbalance
            balance_penalty = abs(sum(sub_weights[:mid]) - sum(sub_weights[mid:]))
            return left_eff + right_eff - balance_penalty
        
        # Add group efficiency to total score
        efficiency_score += group_efficiency(group_weights)
    
    # Step 4: Apply final adjustment based on loading pattern
    light_count = len(weight_groups['light'])
    medium_count = len(weight_groups['medium'])
    heavy_count = len(weight_groups['heavy'])
    
    if light_count > medium_count and light_count > heavy_count:
        efficiency_score *= 1.1
    elif heavy_count > medium_count and heavy_count > light_count:
        efficiency_score *= 0.9
    
    return int(efficiency_score)

# Main execution
package_weights = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
efficiency_score = calculate_loading_efficiency(package_weights)
print(f"Result: {efficiency_score}")