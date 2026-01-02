import math

def analyze_soil_ph(readings):
    # Irrelevant function: analyzes pH but not used in final calculation
    avg = sum(readings) / len(readings)
    return 'acidic' if avg < 6 else 'alkaline' if avg > 7 else 'neutral'

def collect_sensor_data(plots):
    # Distractor function: simulates sensor collection but returns unused data
    sensor_grid = []
    for i, plot in enumerate(plots):
        row_data = []
        for j, crop in enumerate(plot):
            checksum = (i * 31 + j * 23 + hash(crop)) % 100
            row_data.append({
                'sensor_id': i * 10 + j,
                'value': checksum,
                'status': 'OK' if checksum > 10 else 'ERROR'
            })
        sensor_grid.append(row_data)
    return sensor_grid  # Never actually used

def simulate_irrigation_schedule(plots):
    # Dead code path: calculates water distribution but irrelevant
    schedule = []
    total_area = 0
    for plot in plots:
        area = len(plot)
        total_area += area
        schedule.append({'area': area, 'duration_mins': area * 5})
    normalized = [s['duration_mins'] / total_area for s in schedule]
    return normalized  # Unused

def calculate_moisture_score(sensor_data):
    # Decoy function that looks important but isn't called
    score = 0
    for row in sensor_data:
        for entry in row:
            if entry['status'] == 'OK':
                score += entry['value'] * 0.1
    return round(score, 2)

def evaluate_crop_resilience(crops):
    # Another red herring: computes resilience index not used in logic
    base_scores = {'wheat': 70, 'corn': 85, 'rice': 60, 'barley': 75, 'oats': 68}
    total = 0
    count = 0
    for row in crops:
        for crop in row:
            if crop in base_scores:
                # Apply arbitrary decay factor
                adjusted = base_scores[crop] * (0.95 ** count)
                total += adjusted
                count += 1
    return total / max(count, 1) if count else 0

def calculate_optimal_harvest(plots, sensors):
    # Core logic begins here — heavily masked by prior noise
    
    # Step 1: Extract plot yields using hidden pattern
    yields = []
    for i, plot in enumerate(plots):
        row_yield = 0
        for j, crop in enumerate(plot):
            # Hidden rule: yield based on position and crop length
            base = len(crop) * (i + 1) * 10
            bonus = (j + 1) ** 2 if 'r' in crop else 0
            row_yield += base + bonus
        yields.append(row_yield)
    
    # Step 2: Filter using sensor threshold (only specific indices matter)
    valid_indices = []
    for idx, sensor_row in enumerate(sensors):
        active_count = sum(1 for s in sensor_row if s % 7 == 0)  # Only multiples of 7
        if active_count >= 2:
            valid_indices.append(idx)
    
    # Step 3: Map yields to valid plots only
    filtered_yields = [yields[i] for i in valid_indices if i < len(yields)]
    
    # Step 4: Apply transformation using list comprehension and zip
    shifted = [yields[(i + 1) % len(yields)] for i in range(len(yields))]
    pairwise_diffs = [abs(a - b) for a, b in zip(yields, shifted)]
    
    # Step 5: Use enumerate to find correction factor
    correction = 0
    for i, diff in enumerate(pairwise_diffs):
        if i % 2 == 0 and diff > 50:
            correction += int(math.log(diff, 2))
    
    # Step 6: Aggregate filtered values with adjustment
    raw_total = sum(filtered_yields)
    adjusted_total = raw_total - correction * 10
    
    # Step 7: Secondary filter based on parity of index
    final_candidates = [v for i, v in enumerate(filtered_yields) if i % 3 != 2]
    
    # Step 8: Compute average, then scale by number of sensors active
    total_active_sensors = sum(sum(1 for s in row if s % 7 == 0) for row in sensors)
    base_average = sum(final_candidates) / len(final_candidates) if final_candidates else 0
    final_yield = int(base_average + total_active_sensors)
    
    # Irrelevant logging
    debug_log = f"Final yield {final_yield} from {len(final_candidates)} candidates"
    
    return final_yield

def main():
    # Define input data
    plots = [
        ['wheat', 'corn', 'rice'],
        ['barley', 'oats'],
        ['wheat', 'wheat', 'corn', 'barley'],
        ['rice', 'oats', 'wheat', 'corn', 'barley']
    ]
    
    # Sensor matrix: only modulo 7 matters
    sensors = [
        [14, 21, 8],      # Two multiples of 7 → valid
        [35, 42, 49],     # Three multiples → valid
        [10, 11, 12],     # None → invalid
        [56, 63, 70, 77]  # Four multiples → valid
    ]
    
    # Call decoy functions to increase interference
    ph_analysis = analyze_soil_ph([5.8, 6.2, 6.0, 7.1])
    grid = collect_sensor_data(plots)
    irrigation = simulate_irrigation_schedule(plots)
    resilience = evaluate_crop_resilience(plots)
    
    # Core execution point
    final_yield = calculate_optimal_harvest(plots, sensors)
    
    # Output result as required
    print(f"Result: {final_yield}")

if __name__ == '__main__':
    main()