import itertools

def analyze_growth_cycle(plots):
    # Irrelevant analysis function (dead code path)
    peak_phases = []
    for idx, plot in enumerate(plots):
        if len(plot) > 3:
            peak_phases.append(max(plot) * 0.75)
    return [p ** 0.5 for p in peak_phases]

def normalize_readings(readings):
    # Distractor: normalizes sensor data but not used in final result
    base = min(readings)
    return [(r - base) / (max(readings) - base) * 100 for r in readings if r > base]

def simulate_irrigation(schedule, moisture_levels):
    # Misleading simulation with no impact on answer
    updated = moisture_levels.copy()
    for day, amount in enumerate(schedule):
        if day % 2 == 0:
            updated = [m + amount * 0.3 for m in updated]
    return updated

def calculate_harvest_efficiency(fields, climate_log):
    # Core logic embedded within distractions
    total_yield = 0
    adjustment_factor = 0.85
    
    # Real processing begins
    for field_id, crops in fields.items():
        growth_cycles = []
        for _, data in enumerate(crops):
            phase_sum = 0
            for reading in data['readings']:
                # Bit manipulation to obscure relevance
                scaled = (reading >> 2) & ~((1 << 3) - 1)
                phase_sum += scaled + (reading % 4)
            growth_cycles.append(phase_sum)
        
        # Accumulation via dictionary transform
        cycle_stats = {i: val for i, val in enumerate(growth_cycles)}
        raw_total = sum(cycle_stats.values())
        
        # Conditional adjustment based on weather log (real dependency)
        stress_days = 0
        for record in climate_log:
            temp, humidity = record[0], record[1]
            if temp > 35 and humidity < 40:
                stress_days += 1
        
        efficiency_ratio = (10 - min(stress_days, 10)) / 10.0
        harvested = raw_total * efficiency_ratio * adjustment_factor
        total_yield += harvested
    
    # Final transformation
    outlier_filter = [x for x in [total_yield * 1.1, total_yield, total_yield * 0.9] if x < total_yield * 1.05]
    refined_yield = sum(outlier_filter) / len(outlier_filter)
    
    # Key assignment point
    final_yield = int(round(refined_yield))
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Input data setup
    field_data = {
        'F01': [
            {'readings': [120, 134, 98, 145, 112]},
            {'readings': [103, 119, 126]}
        ],
        'F02': [
            {'readings': [130, 142, 138, 127]},
            {'readings': [111, 124, 117, 133]},
            {'readings': [99, 105]}
        ]
    }
    
    weather_log = [
        (28, 65), (31, 58), (36, 37), (29, 70), 
        (33, 50), (37, 39), (26, 80), (30, 60),
        (38, 35), (32, 55), (27, 75)
    ]
    
    # Dead variables - red herrings
    sensor_fidelity = [0.98, 0.99, 0.97, 0.96]
    calibration_matrix = list(itertools.product([1, 0], repeat=2))
    baseline_metrics = normalize_readings([50, 60, 70, 80, 90])
    irrigation_schedule = [5, 3, 0, 6, 2]
    simulated_moisture = simulate_irrigation(irrigation_schedule, [30, 40, 35])
    ignored_cycles = analyze_growth_cycle(field_data.values())
    
    # Critical statement
    final_yield = calculate_harvest_efficiency(field_data, weather_log)
    
    print(f"Target result: {final_yield}")