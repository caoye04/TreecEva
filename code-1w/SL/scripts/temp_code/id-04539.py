def analyze_soil_composition(data):
    # Irrelevant function: analyzes soil but not used in final calculation
    return sum(x * 0.3 for x in data if x > 5)


def preprocess_growth_pattern(sequence):
    # Distractor: transforms sequence but result is unused
    processed = [seq ** 0.5 for seq in sequence if seq % 2 == 0]
    normalized = [p / max(processed) for p in processed]
    return normalized

def compute_root_depth(profile):
    # Dead code path: never called
    return sum(p * 2 for p in profile)

def calculate_harvest_efficiency(metrics, cycles):
    # Core logic begins
    base_efficiency = 0
    adjustment_factor = 1.75
    
    # Step 1: filter valid quadrants
    valid_zones = [m for m in metrics if m > 3 and m < 9]
    
    # Step 2: slice middle portion (slicing operation)
    mid_zones = valid_zones[1:-1]  # Remove first and last
    
    # Step 3: apply cycle-based decay
    decayed_values = []
    for i, zone in enumerate(mid_zones):
        decay = zone * (0.9 ** (i + 1))
        decayed_values.append(decay)
    
    # Step 4: accumulate base efficiency
    for val in decayed_values:
        base_efficiency += val * adjustment_factor
    
    # Step 5: incorporate cycle count with conditional boost
    if len(cycles) > 4:
        cycle_boost = len(cycles) * 0.6
    else:
        cycle_boost = len(cycles) * 0.3
    
    # Step 6: apply boost
    base_efficiency *= (1 + cycle_boost / 10)
    
    # Step 7: bit manipulation for 'genetic stability' (red herring but actually used)
    stability_key = len(valid_zones) ^ 5
    modifier = (stability_key << 1) & 7  # Bitwise AND to cap
    
    # Step 8: apply modifier as fractional adjustment
    base_efficiency += modifier * 0.4
    
    # Step 9: string-based condition from encoded rule (irrelevant parsing)
    rule_code = 'A7X-TRIG-2024'
    threshold_flag = rule_code[1:3] == '7X'  # False, distractor
    if threshold_flag:
        base_efficiency *= 1.2  # Never executed
    
    # Step 10: combinatorics - number of ways to select 2 zones from mid_zones
    n = len(mid_zones)
    if n >= 2:
        combinations = (n * (n - 1)) // 2
        base_efficiency += combinations * 0.25
    
    # Final assignment
    final_yield = round(base_efficiency, 6)
    return final_yield

# Main execution
area_metrics = [2.1, 4.5, 6.8, 7.2, 9.1, 8.3, 5.7, 3.4]
growth_cycles = [1, 2, 3, 4, 5]  # 5 cycles

# Irrelevant preprocessing calls
soil_analysis = analyze_soil_composition(area_metrics)
temp_pattern = preprocess_growth_pattern(growth_cycles)

# Key statement
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Output result
print(f"Target result: {final_yield}")