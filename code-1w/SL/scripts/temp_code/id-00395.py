import math

# Simulate agricultural yield prediction with multiple distractions
def analyze_soil_composition(sensor_readings):
    # Irrelevant computation: soil pH analysis (not used in final result)
    ph_levels = [r[1] for r in sensor_readings]
    avg_ph = sum(ph_levels) / len(ph_levels)
    stability_score = math.exp(-abs(avg_ph - 6.5))
    return stability_score  # Dead end

def compute_irrigation_efficiency(logs):
    # Distractor function: calculates water usage efficiency (unused)
    total_flow = sum([log['flow'] for log in logs if log['active']])
    duration = len(logs)
    if duration == 0:
        return 0
    return total_flow / duration

def calculate_harvest_efficiency(fields, cfg):
    # Core logic embedded in noise
    
    # Irrelevant preprocessing
    thresholds = cfg.get('thresholds', {})
    min_rainfall = thresholds.get('rainfall', 20)
    max_acidity = thresholds.get('acidity', 7.0)
    
    # Real logic begins
    base_multiplier = cfg['base_yield_factor']
    total_area = 0
    effective_yield = 0
    penalty_adjustment = 0
    
    # Hidden accumulation logic
    for field in fields:
        area = field['area']
        rainfall = field['rainfall']
        crop_type = field['crop']
        
        # Real condition affecting result
        if rainfall < min_rainfall:
            penalty_adjustment += area * 0.15
        
        # This branch contains key contribution
        if crop_type == 'wheat':
            # Critical path: wheat fields contribute with bonus
            wheat_bonus = 1.2 if rainfall >= min_rainfall else 0.85
            effective_yield += area * base_multiplier * wheat_bonus
        elif crop_type == 'corn':
            # Corn has no effect on final yield in this config
            continue
        else:
            effective_yield += area * base_multiplier * 0.75
        
        total_area += area
    
    # Misleading normalization (not actually used)
    normalized_penalty = penalty_adjustment / (total_area + 1e-5) if total_area > 0 else 0
    
    # Key result calculation
    raw_result = effective_yield - penalty_adjustment
    
    # Final adjustment using lambda-based transformation (important!)
    scale_fn = lambda x: x * 1.08 if x > 500 else x * 1.02
    final_output = int(scale_fn(raw_result))
    
    return final_output

# Simulated sensor and irrigation data (distractors)
sensor_data = [(1001, 6.8), (1002, 6.3), (1003, 7.1), (1004, 6.9)]
irrigation_logs = [
    {'flow': 120, 'duration': 30, 'active': True},
    {'flow': 0, 'duration': 15, 'active': False},
    {'flow': 95, 'duration': 45, 'active': True}
]

# Actual field data that matters
field_data = [
    {'area': 45, 'rainfall': 18, 'crop': 'wheat'},
    {'area': 60, 'rainfall': 25, 'crop': 'wheat'},
    {'area': 30, 'rainfall': 22, 'crop': 'barley'},
    {'area': 50, 'rainfall': 15, 'crop': 'wheat'},
    {'area': 40, 'rainfall': 30, 'crop': 'corn'}  # Corn ignored
]

# Configuration with red herring keys
config = {
    'base_yield_factor': 10,
    'enable_optimization': True,
    'thresholds': {
        'rainfall': 20,
        'acidity': 6.8,
        'temperature': 25
    },
    'debug_mode': False,
    'logging_interval': 5
}

# Execute core function
soil_health = analyze_soil_composition(sensor_data)  # Unused
water_efficiency = compute_irrigation_efficiency(irrigation_logs)  # Unused
final_yield = calculate_harvest_efficiency(field_data, config)

# Track irrelevant stats
inspection_count = len(field_data)
disputed_fields = [f for f in field_data if f['rainfall'] < 18]
review_needed = len(disputed_fields) > 0

# Output target result
Result: {final_yield}