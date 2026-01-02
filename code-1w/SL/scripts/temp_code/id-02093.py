def preprocess_soil(samples):
    adjusted = []
    for val in samples:
        if val < 3.0:
            adjusted.append(val * 1.5)
        elif val > 7.0:
            adjusted.append(val * 0.8)
        else:
            adjusted.append(val)
    return [round(x, 2) for x in adjusted]

# Irrelevant helper (dead path)
def analyze_rainfall(patterns):
    total = 0
    for p in patterns:
        total += p * 0.3
    return total  # Never used

# Decoy function with misleading intermediate output
def compute_growth_index(data):
    index = 1
    for i, x in enumerate(data):
        index *= (i + 1) if x > 4 else 1
    print(f'Decoy growth index: {index}')  # Misleading print
    return -999

# Core logic disguised among distractions
def calculate_harvest(soil, crops):
    base_yield = 0
    modifier = 1.0
    
    # Real processing begins
    for idx, (level, crop) in enumerate(zip(soil, crops)):
        if crop == 'wheat':
            if level < 4.5:
                base_yield += 20
            elif level >= 6.0:
                base_yield += 50
            else:
                base_yield += 35
        elif crop == 'corn':
            shift = level % 3
            temp = int(level << 1)  # Bit manipulation red herring
            if shift == 1:
                base_yield += 40
            else:
                base_yield += 60
        elif crop == 'rice':
            base_yield += 55 if level > 5.0 else 25
    
    # Multi-step adjustment chain (relevant)
    adjustment_factor = 0.9
    for _ in range(2):
        adjustment_factor = round(adjustment_factor * 1.05, 3)
    
    # Distractor: unused transformation
    normalized = [abs(x - 5.5) for x in soil]
    normalized = [x for x in normalized if x < 2.0]
    
    # Final calculation (key step)
    final_yield = int(base_yield * adjustment_factor)
    
    # Irrelevant sorting
    sorted_crops = sorted(crops, key=lambda x: len(x), reverse=True)
    for c in sorted_crops:
        pass  # Dead loop
    
    return final_yield

# Unused variables and fake data paths
rainfall_history = [0.3, 0.7, 1.2, 0.4, 0.0]
data_checksum = sum(rainfall_history) * 100
temp_buffer = [0] * 5

# Actual input data
soil_readings = [4.2, 6.1, 3.8, 7.3, 5.0, 4.4]
crop_layout = ['wheat', 'corn', 'wheat', 'rice', 'corn', 'wheat']

# Preprocessing (relevant but obscured)
processed_soil = preprocess_soil(soil_readings)

# Fake analysis call (distraction)
growth_idx = compute_growth_index(processed_soil)

# Key statement
final_yield = calculate_harvest(processed_soil, crop_layout)

# Output result
print(f'Result: {final_yield}')