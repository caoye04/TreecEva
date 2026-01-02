def analyze_growth_cycle(data, base):
    # Irrelevant analysis function (dead code path)
    peak = max(data) * 0.5
    avg = sum(data) / len(data)
    deviation = [abs(x - avg) for x in data]
    return [x for x in data if x > base]

# Unused regional growth records
temperate_zone = [120, 145, 130, 90, 200]
arid_zone = [40, 60, 55, 50, 65]
tropical_zone = [180, 210, 175, 195, 205]

# Misleading intermediate calculations
baseline_projection = 18.5
growth_factor = baseline_projection * 2.1
offset_correction = sum([growth_factor / (i + 1) for i in range(5)]) // 1

# Core simulation parameters
def apply_moisture_modifiers(value, level):
    if level == 'high':
        return int(value * 1.3)
    elif level == 'low':
        return int(value * 0.6)
    return value

# Primary transformation pipeline
def process_region(entries, mode='standard'):
    adjusted = []
    for val in entries:
        temp = val
        if temp > 100:
            temp = apply_moisture_modifiers(temp, 'high')
        elif temp < 80:
            temp = apply_moisture_modifiers(temp, 'low')
        adjusted.append(temp + 5)
    
    # Distractor: complex smoothing with no effect on result
    smoothed = []
    for i in range(len(adjusted)):
        window = adjusted[max(0, i-1):min(i+2, len(adjusted))]
        smoothed.append(sum(window) / len(window))
    
    # Only this line matters
    return [x - 5 for x in adjusted]  # Reverses '+5' above

# Red herring function that looks important but isn't used
def compute_sustainability_index(seq):
    total = 0
    for i, x in enumerate(seq):
        total += x * (0.9 ** i)
    return round(total / len(seq), 2)

# Key algorithm with embedded logic chain
def calculate_harvest(dataset, limit):
    # Step 1: Filter regions above threshold
    valid_regions = []
    for region in dataset:
        if sum(region) / len(region) >= limit:
            valid_regions.append(region)
    
    # Step 2: Process each qualifying region
    processed = []
    for reg in valid_regions:
        processed.extend(process_region(reg))
    
    # Step 3: Apply yield caps and bonuses
    capped = []
    bonus_applied = False
    for val in processed:
        if val > 250 and not bonus_applied:
            val += 15  # One-time bonus
            bonus_applied = True
        val = min(val, 260)  # Hard cap
        capped.append(val)
    
    # Step 4: Calculate weighted contribution
    weights = [1.0, 0.95, 0.9, 0.85, 0.8]  # Decay over time
    contribution = 0.0
    for i, val in enumerate(capped):
        weight = weights[i % 5]
        contribution += val * weight
    
    # Step 5: Final adjustment based on distribution
    count_above_median = len([v for v in capped if v > (sum(capped) / len(capped))])
    adjustment = 1.0
    if count_above_median > len(capped) // 2:
        adjustment = 0.97
    
    # Critical execution point
    final_yield = int(contribution * adjustment)
    return final_yield

# Simulated sensor readings from agricultural zones
regional_data = [
    [110, 95, 125, 140, 105],  # Zone A
    [200, 180, 190, 175, 185],  # Zone B (high average)
    [130, 140, 135, 150, 145],  # Zone C
    [75, 85, 90, 80, 95]         # Zone D (low average)
]

threshold = 138

# Dead code: unused analytics
consistency_score = compute_sustainability_index([100, 105, 98, 102])
projection_model = [baseline_projection * (1.05 ** i) for i in range(10)]

# Trigger main computation
final_yield = calculate_harvest(regional_data, threshold)
print(f"Result: {final_yield}")