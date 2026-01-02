from itertools import combinations

def analyze_traffic(hubs):
    traffic_score = 0
    for i, hub in enumerate(hubs):
        if i % 2 == 0:
            traffic_score += len(hub) * (i + 1)
    return traffic_score

def preprocess_hubs(raw_data, threshold=3):
    processed = []
    temp_store = []
    for entry in raw_data:
        clean_entry = [x for x in entry if x > threshold]
        temp_store.append(sum(clean_entry))  # distractor: not directly used
        if sum(clean_entry) > 10:
            processed.append(clean_entry)
    scaling_factor = sum(temp_store) / len(temp_store) if temp_store else 1
    normalized = [[int(x * scaling_factor / 2) for x in p] for p in processed]
    return normalized

def build_efficiency_map(hubs):
    efficiency_map = {}
    for idx, hub in enumerate(hubs):
        base_eff = sum(hub) / (idx + 1) if idx >= 0 else 0
        adjustments = [base_eff * 0.1 for _ in range(len(hub))]
        efficiency_map[idx] = {
            'base': base_eff,
            'adjustments': adjustments,
            'status': 'active' if base_eff > 5 else 'standby'
        }
    return efficiency_map

def optimize_distribution(hubs, eff_map):
    total_capacity = 0
    for i, hub in enumerate(hubs):
        hub_base = eff_map[i]['base']
        adjustment_sum = sum(eff_map[i]['adjustments'])
        temp_capacity = hub_base + adjustment_sum
        
        # Simulate load redistribution
        if len(hub) > 2:
            pairs = list(combinations(hub, 2))
            pair_boost = 0
            for p in pairs[:2]:
                pair_boost += abs(p[0] - p[1])
            temp_capacity += pair_boost / 4
        
        # Distractor: irrelevant tracking
        debug_trace = []
        for val in hub:
            debug_trace.append(val ** 0.5)  # unused computation
        
        total_capacity += int(temp_capacity)
    
    # Final adjustment based on global pattern
    if len(hubs) >= 3:
        total_capacity -= 2
    return total_capacity

# Main execution
raw_hub_data = [
    [2, 4, 6],
    [1, 8, 5, 7],
    [3, 3, 9],
    [5, 5, 5, 5]
]

# Step 1: Analyze traffic (distractor step - result not used in final answer)
analyze_traffic(raw_hub_data)

# Step 2: Preprocess hubs
processed_hubs = preprocess_hubs(raw_hub_data)

# Step 3: Build efficiency map
efficiency_map = build_efficiency_map(processed_hubs)

# Step 4: Optimize distribution
final_capacity = optimize_distribution(processed_hubs, efficiency_map)

print(f"Result: {final_capacity}")