import itertools

def analyze_growth_cycle(data):
    # Irrelevant preprocessing - distractor
    temp_log = [x ** 2 for x in data if x > 5]
    offset = sum(temp_log) // len(temp_log) if temp_log else 0

    # Real transformation path
    filtered = [x for x in data if x % 2 == 1]  # Keep odd values
    shifted = [(x * 3 + 2) % 17 for x in filtered]
    return shifted

def decode_nutrient_sequence(seq):
    # Decoy function - never called but looks important
    return [sum(seq[:i]) % 11 for i in range(1, len(seq)+1)]

def validate_soil_ph(level):
    # Dead code path - misleading
    if 6.0 <= level <= 7.5:
        return True
    return False

def transform_yield_curve(values):
    # Complex but partially relevant transformation
    base_curve = [v * 1.5 for v in values]
    adjusted = []
    for i, val in enumerate(base_curve):
        if i % 3 == 0:
            adjusted.append(int(val) + (i // 3))
        elif i % 4 == 0:
            adjusted.append(int(val) - 1)
        else:
            adjusted.append(int(val))
    # Red herring: unused variable
    peak_analysis = max(adjusted) * len(adjusted)
    return adjusted

def calculate_harvest_efficiency(dataset):
    # Core logic buried in noise
    stage_one = transform_yield_curve(dataset)
    
    # Distracting bit manipulation - looks critical but isn't
    decoy_mask = 0b110101
    masked_values = [v ^ decoy_mask & 0xF for v in stage_one]
    
    # Actual key calculation
    valid_windows = []
    for window in itertools.sliding_window_view(stage_one, window_shape=3):
        if window[0] < window[1] > window[2]:  # Local maxima
            valid_windows.append(window[1])
    
    # More distractions
    outlier_check = [w for w in valid_windows if w > 20]
    if len(outlier_check) > 2:
        adjustment_factor = 0.85
    else:
        adjustment_factor = 1.05  # This will be used
    
    # Final computation
    raw_total = sum(valid_windows)
    final_score = raw_total * adjustment_factor
    
    # Key variable
    final_yield = int(final_score)  # Answer is derived here
    return final_yield

# Simulated sensor readings from agricultural plot
raw_input_data = [4, 7, 2, 9, 6, 11, 8, 13, 10]

# Phantom variable - looks like it's used
baseline_reference = sum(x**2 for x in raw_input_data if x < 8)

# Unused function call placeholder - visual noise
potential_ph = 6.8
# validate_soil_ph(potential_ph)  # Commented out — red herring

# Main processing pipeline
processed_data = analyze_growth_cycle(raw_input_data)

# Critical execution point
final_yield = calculate_harvest_efficiency(processed_data)

print(f"Result: {final_yield}")