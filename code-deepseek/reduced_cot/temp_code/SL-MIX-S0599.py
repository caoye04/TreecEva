from collections import Counter

def analyze_storage_utilization():
    storage_volumes = [45, 23, 67, 45, 89, 23, 45, 12]
    capacity_threshold = 50
    
    volume_counter = Counter(storage_volumes)
    frequent_volumes = [vol for vol, count in volume_counter.items() if count >= 2]
    
    # Distractor: Calculate total but don't use it
    total_storage = sum(storage_volumes)
    
    # Relevant: Filter volumes above threshold
    high_volumes = [vol for vol in frequent_volumes if vol > capacity_threshold]
    
    # Distractor: Calculate average but don't use it
    avg_volume = total_storage / len(storage_volumes) if storage_volumes else 0
    
    # Relevant: Process high volumes
    capacity_adjustments = []
    for idx, vol in enumerate(high_volumes):
        adjustment = vol * 0.8 if idx % 2 == 0 else vol * 0.9
        capacity_adjustments.append(adjustment)
    
    # Final calculation
    final_capacity = sum(capacity_adjustments) if capacity_adjustments else 0
    
    print("Result:", final_capacity)

analyze_storage_utilization()