def storage_optimizer(volumes, pools):
    # Calculate initial capacity metrics
    total_volume = sum(volumes)
    avg_pool_size = sum(pools) / len(pools) if pools else 0
    
    # Distractor: unused intermediate calculation
    volume_product = volumes[0] * volumes[1] if len(volumes) >= 2 else 1
    
    # Core logic with conditional expressions and slicing
    active_threshold = 500
    qualified_pools = [p for p in pools if p > active_threshold]
    
    # Distractor: unused list operation
    pool_variance = max(pools) - min(pools) if pools else 0
    
    # Key calculation with conditional logic
    if qualified_pools:
        optimal_capacity = total_volume + sum(qualified_pools[-2:])  # Last two qualified pools
    else:
        optimal_capacity = total_volume + (avg_pool_size * 1.5)
    
    # Final adjustment based on volume distribution
    volume_ratio = volumes[-1] / volumes[0] if volumes else 1
    final_value = optimal_capacity * (0.8 if volume_ratio > 2 else 1.2)
    
    return round(final_value, 2)

# Main execution
backup_volumes = [320, 480, 210, 650]
active_pools = [420, 580, 310, 720, 490]

# Distractor: unused intermediate variable
pool_analysis = [p * 1.1 for p in active_pools]

final_capacity = storage_optimizer(backup_volumes, active_pools)
print(f"Result: {final_capacity}")