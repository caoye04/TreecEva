def analyze_crop_zones(plots):
    zones = set()
    for plot in plots:
        for zone_id in plot['zones']:
            zones.add(zone_id)
    return zones

import math

def compute_moisture_index(history):
    total = 0
    count = 0
    baseline = 25.0
    fluctuation_buffer = 0
    for entry in history:
        if entry['valid']:
            total += entry['moisture']
            count += 1
        else:
            fluctuation_buffer += 1
    avg = total / count if count > 0 else 0
    return round(avg - baseline + fluctuation_buffer * 0.1, 2)

plots_data = [
    {'id': 101, 'zones': [1, 2, 3], 'status': 'active', 'yield_hist': [88, 92, 85]},
    {'id': 102, 'zones': [2, 3, 4], 'status': 'inactive', 'yield_hist': [76, 79, 73]},
    {'id': 103, 'zones': [3, 4, 5], 'status': 'active', 'yield_hist': [90, 88, 91]}
]

sensor_logs = [
    {'moisture': 24.1, 'valid': True},
    {'moisture': 26.3, 'valid': True},
    {'moisture': 22.7, 'valid': True},
    {'moisture': 31.5, 'valid': False},
    {'moisture': 25.0, 'valid': True}
]

# Irrelevant helper function (dead utility)
def normalize_readings(data):
    max_val = max(data)
    return [round(x / max_val, 3) for x in data]

# Distractor variables
temp_correction_factor = 1.05
pressure_adjustment = 0.97
baseline_offset = 12
redundant_sum = 0
for i in range(3):
    redundant_sum += i * 2

# Critical data structures
field_data = {
    'plots': [],
    'total_area': 0,
    'avg_yield': 0
}

yield_acc = 0
plot_count = 0
for p in plots_data:
    if p['status'] == 'active':
        field_data['plots'].append(p)
        yield_acc += sum(p['yield_hist']) / len(p['yield_hist'])
        plot_count += 1

if plot_count > 0:
    field_data['avg_yield'] = yield_acc / plot_count

all_zones = analyze_crop_zones(plots_data)
sorted_zones = sorted(all_zones)
midpoint = len(sorted_zones) // 2
median_zone = sorted_zones[midpoint] if sorted_zones else 0

irrelevant_map = {z: z * z for z in sorted_zones if z % 2 == 1}

moisture_score = compute_moisture_index(sensor_logs)

threshold_set = set()
for z in all_zones:
    if z >= median_zone:
        threshold_set.add(z)

# Secondary distractor loop
dummy_vals = []
for x in range(1, 6):
    temp = x ** 2 - x
    dummy_vals.append(temp)

auxiliary_total = sum(dummy_vals)
scaling_constant = auxiliary_total / 10 if auxiliary_total > 0 else 1

# Core logic with interference
previous_yield = {}
cumulative_shift = 0
for idx, plot in enumerate(field_data['plots']):
    plot_avg = sum(plot['yield_hist']) / len(plot['yield_hist'])
    previous_yield[plot['id']] = plot_avg
    cumulative_shift += plot_avg * 0.01

# Key function with multiple concepts
def calculate_harvest_efficiency(farm_data, valid_zones):
    efficiency = 0
    base_multiplier = 1.5
    zone_bonus = 0
    
    # Set difference distraction
    unused_zones = {1,2,3,4,5} - valid_zones
    penalty = len(unused_zones) * 0.5
    
    for plot in farm_data['plots']:
        plot_id = plot['id']
        recent_yield = plot['yield_hist'][-1]
        historical_avg = sum(plot['yield_hist']) / len(plot['yield_hist'])
        improvement = recent_yield - historical_avg
        
        # Logical complexity and comparisons
        if improvement > 2:
            bonus = 10
        elif improvement > 0:
            bonus = 5
        else:
            bonus = 0
        
        # Arithmetic chain
        contribution = (historical_avg * base_multiplier) + bonus
        efficiency += contribution
    
    # Final adjustment using set size
    zone_bonus = len(valid_zones) * 3
    final_efficiency = efficiency + zone_bonus - penalty
    
    # Red herring calculation
    outlier_check = efficiency / (len(farm_data['plots']) + 1)
    if outlier_check > 100:
        final_efficiency *= 0.95  # Never triggers
        
    return int(final_efficiency)

# Execution point of interest
final_yield = calculate_harvest_efficiency(field_data, threshold_set)

Result: {final_yield}