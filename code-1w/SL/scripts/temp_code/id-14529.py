def preprocess_soil_data(data):
    # Irrelevant preprocessing function (dead code path)
    return {k: v * 1.05 for k, v in data.items() if v > 30}

soil_health = {
    'north': 45,
    'south': 25,
    'east': 60,
    'west': 35,
    'central': 50
}

# Distractor: unused soil transformation
treated_soil = preprocess_soil_data(soil_health)

yield_potential = {
    'north': 80,
    'south': 30,
    'east': 90,
    'west': 70,
    'central': 85
}

efficiency_map = {
    'north': 0.85,
    'south': 0.45,
    'east': 0.92,
    'west': 0.78,
    'central': 0.88
}

# Misleading intermediate calculation (not part of final result)
total_health_score = sum(soil_health.values())
avg_health = total_health_score / len(soil_health)
adjusted_potential = {}
for region in yield_potential:
    adjusted_potential[region] = yield_potential[region] * (soil_health.get(region, 0) / 100)

# Dead code: complex but unused transformation
decoy_matrix = [[i * j for j in range(5)] for i in range(5)]
trace_sum = sum(decoy_matrix[i][i] for i in range(5))

# Unused logical branch with string manipulation distraction
disaster_log = "flood,fire,storm"
events = disaster_log.split(',')
event_flags = {e: e in ['drought', 'flood'] for e in events}

if 'drought' in event_flags and event_flags['drought']:
    for k in efficiency_map:
        efficiency_map[k] *= 0.7

# Real computation begins here — heavily buried
regions = ['north', 'east', 'west']  # Only these contribute
exclusion_zone = 'south'
backup_region = 'central'

penalty_factor = 1.0
if avg_health < 40:
    penalty_factor = 0.9
elif avg_health > 50:
    penalty_factor = 1.1  # This will trigger

penalty_factor *= 0.95  # Additional obscure adjustment

# Core logic hidden among distractions
def calculate_harvest(regions, efficiency):
    base_total = 0
    bonus = 0
    for r in regions:
        # Relevant arithmetic and dictionary lookup
        contribution = yield_potential[r] * efficiency[r]
        base_total += contribution
        
        # Conditional bonus logic (triggers for 'east')
        if r == 'east' and contribution > 80:
            bonus += 10 * efficiency[r]
    
    # Nested condition with early return red herring
    if 'south' in regions:
        return -1  # Dead path
    
    final = base_total + bonus
    final *= penalty_factor
    
    # Last-minute adjustment based on map size (misdirection: looks important)
    scale = len(efficiency)  # includes all, not just regions
    if scale >= 5:
        final *= 1.02
    
    return final

# Critical execution point
final_yield = calculate_harvest(regions, efficiency_map)

# Output required format
print(f"Result: {final_yield}")