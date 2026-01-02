from collections import defaultdict, Counter
import math

# Simulated agricultural sensor processing with extensive distractors
def analyze_growth_pattern(data):
    peak_phases = []
    base_levels = []
    for entry in data:
        if entry['stage'] == 'germination':
            base_levels.append(entry['health'])
        elif entry['stage'] == 'flowering':
            peak_phases.append(entry['vigor'])
    
    # Irrelevant transformation
    normalized_peaks = [p * 0.87 for p in peak_phases if p > 0]
    avg_base = sum(base_levels) / len(base_levels) if base_levels else 0
    
    # Decoy calculation - looks important but unused later
    trend_score = math.log(avg_base + 1) if avg_base > 0 else 0
    
    return {'avg_base': avg_base, 'peak_count': len(peak_phases)}

# Distractor function - never called in execution path
def calculate_soil_composition(readings):
    composition = defaultdict(int)
    for r in readings:
        composition[r['element']] += r['concentration']
    balance_ratio = composition['nitrogen'] / (composition['phosphorus'] + 1)
    return {'balance': balance_ratio, 'total_elements': len(composition)}

# Another red herring - complex but dead-end logic
def predict_pest_risk(temp_history, humidity_log):
    risk_factors = []
    for t, h in zip(temp_history, humidity_log):
        if t > 30 and h > 70:
            risk_factors.append(1.5)
        elif t > 35:
            risk_factors.append(0.8)
    severity_index = sum(risk_factors) * 0.3
    return round(severity_index, 2)

# Core processing chain - relevant path
def preprocess_harvest_data(raw_entries):
    filtered = [e for e in raw_entries if e['quality_flag'] != 'discarded']
    sorted_by_region = sorted(filtered, key=lambda x: x['region'])
    
    # Group by region using defaultdict - actual use case
    regional_aggregates = defaultdict(list)
    for item in sorted_by_region:
        regional_aggregates[item['region']].append(item['yield_amount'])
    
    stats_summary = {}
    for region, yields in regional_aggregates.items():
        avg_yield = sum(yields) / len(yields)
        yield_variance = sum((y - avg_yield) ** 2 for y in yields) / len(yields)
        stats_summary[region] = {
            'mean': avg_yield,
            'variance': yield_variance
        }
    
    # Dead code branch - looks like it modifies data but doesn't affect output
    if 'X9' in regional_aggregates:
        adjustment_factor = 1.1
        for y in regional_aggregates['X9']:
            y *= adjustment_factor  # No effect due to reassignment below

    return stats_summary

# Secondary processing with tuple unpacking and filtering
def extract_performance_metrics(aggregated_data):
    metrics = []
    thresholds = {'high': 80, 'medium': 50}
    
    for region_id, stats in aggregated_data.items():
        mean_val = stats['mean']
        var_val = stats['variance']
        
        # Complex conditional that evaluates but leads nowhere
        performance_tier = 'low'
        if mean_val >= thresholds['high'] and var_val < 200:
            performance_tier = 'excellent'
        elif mean_val >= thresholds['medium']:
            performance_tier = 'moderate'
        
        # Real computation buried among distractions
        efficiency_score = mean_val - (var_val * 0.01)
        metrics.append((region_id, efficiency_score))
    
    # Unused list comprehension - creates illusion of further processing
    [m for m in metrics if m[1] > 60]  # No assignment!
    
    return metrics

# Final result derivation - target execution point
def harvest_results(processed_metrics):
    # Tuple unpacking from previous step
    total_weighted = 0
    count_regions = 0
    
    for region_code, score in processed_metrics:
        # Artificial complexity with bitwise distraction
        region_key = hash(region_code) & 0xFFFF
        modifier = (region_key % 7) / 10.0
        adjusted_score = score * (1 + modifier) if region_key % 3 == 0 else score * (1 - modifier)
        
        # Only certain regions contribute meaningfully
        if region_code in ['R1', 'R2', 'R3', 'R7']:
            total_weighted += adjusted_score
            count_regions += 1
    
    # Critical answer computation
    final_yield = total_weighted / count_regions if count_regions > 0 else 0
    
    # Print required at end
    print(f"Target result: {final_yield}")
    return final_yield

# Main execution block - sets up scenario
if __name__ == '__main__':
    # Simulated input dataset
    field_data = [
        {'region': 'R1', 'yield_amount': 95, 'quality_flag': 'valid', 'stage': 'flowering', 'health': 78, 'vigor': 88},
        {'region': 'R2', 'yield_amount': 87, 'quality_flag': 'valid', 'stage': 'fruiting', 'health': 82, 'vigor': 76},
        {'region': 'R3', 'yield_amount': 91, 'quality_flag': 'valid', 'stage': 'flowering', 'health': 75, 'vigor': 85},
        {'region': 'R4', 'yield_amount': 64, 'quality_flag': 'discarded', 'stage': 'germination', 'health': 60, 'vigor': 54},
        {'region': 'R5', 'yield_amount': 73, 'quality_flag': 'valid', 'stage': 'maturation', 'health': 88, 'vigor': 67},
        {'region': 'R6', 'yield_amount': 68, 'quality_flag': 'valid', 'stage': 'germination', 'health': 59, 'vigor': 62},
        {'region': 'R7', 'yield_amount': 89, 'quality_flag': 'valid', 'stage': 'flowering', 'health': 81, 'vigor': 90},
        {'region': 'R8', 'yield_amount': 77, 'quality_flag': 'valid', 'stage': 'fruiting', 'health': 74, 'vigor': 70}
    ]

    # Begin processing pipeline
    analysis_result = analyze_growth_pattern(field_data)
    processed_summary = preprocess_harvest_data(field_data)
    performance_list = extract_performance_metrics(processed_summary)
    
    # Key execution point - determines final answer
    final_yield = harvest_results(performance_list)