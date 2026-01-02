from collections import defaultdict, Counter

def analyze_growth_patterns(data, threshold=3):
    growth_trends = defaultdict(int)
    volatility = defaultdict(float)
    
    for region, records in data.items():
        prev = records[0]
        trend_count = 0
        squared_diffs = 0
        
        for current in records[1:]:
            if current > prev:
                trend_count += 1
            diff = current - prev
            squared_diffs += diff * diff
            prev = current
            
        growth_trends[region] = trend_count
        volatility[region] = (squared_diffs / (len(records) - 1)) ** 0.5 if records else 0
    
    # Distractor: unused transformation
    transformed_volatility = {k: round(v * 1.23, 2) for k, v in volatility.items()}
    return growth_trends, volatility

def calculate_optimal_yield(base_yield, modifiers, penalties):
    base_modifier = sum(modifiers.values()) * 0.1
    penalty_factor = max(penalties.values()) * 0.05 if penalties else 0
    adjusted = base_yield * (1 + base_modifier - penalty_factor)
    
    # Complex but partially irrelevant logic
    safety_buffer = 5
    if adjusted > 80:
        safety_buffer += 10
    elif adjusted < 50:
        safety_buffer -= 3
    
    # Real adjustment
    stability_bonus = 0
    if len(modifiers) >= 3 and sum(1 for x in modifiers.values() if x > 4) >= 2:
        stability_bonus = 7.5
    
    final_yield = adjusted + safety_buffer + stability_bonus
    
    # Dead code path (never reached due to structure)
    temp_debug = [x for x in range(10) if x == 100]
    
    return final_yield

def main():
    # Simulated agricultural dataset
    crop_data = {
        'north': [23, 25, 29, 32, 31, 34],
        'south': [18, 22, 25, 27, 30, 33, 36],
        'east': [45, 44, 46, 48, 47],
        'west': [19, 21, 20, 24, 26, 28]
    }
    
    # Extract trends (used)
    trends, _ = analyze_growth_patterns(crop_data)
    
    # Unused intermediate analysis
    record_counter = Counter([len(records) for records in crop_data.values()])
    avg_length = sum(record_counter.elements()) / len(record_counter)
    
    # Prepare yield calculation inputs
    base_yield = 40
    modifiers = {
        'sun_exposure': 5,
        'soil_quality': 6,
        'water_access': 4,
        'pest_control': 7
    }
    
    # Penalty factors (some misleading)
    penalties = {
        'frost_days': 8,
        'market_demand': 2,  # Irrelevant but looks important
        'labor_shortage': 3
    }
    
    # Key computation with distractors around
    intermediate_result = base_yield * 0.85 + len(trends) * 2.5
    debug_snapshot = {'step': 'pre_final', 'value': intermediate_result}
    
    final_yield = calculate_optimal_yield(base_yield, modifiers, penalties)
    
    # Print result as required
    print(f"Target result: {final_yield}")

if __name__ == "__main__":
    main()