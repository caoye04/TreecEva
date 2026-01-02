from collections import defaultdict

# Simulate agricultural field sensor data across zones
def collect_field_data():
    raw_readings = [
        (1, 'A', 120), (1, 'B', 150), (1, 'C', 130),
        (2, 'A', 110), (2, 'B', 0),   (2, 'C', 140),
        (3, 'A', 160), (3, 'B', 155), (3, 'C', 135)
    ]
    
    # Misleading aggregation: average per zone (not used in final logic)
    zone_totals = defaultdict(lambda: [0, 0])  # [sum, count]
    for zone_id, sector, reading in raw_readings:
        zone_totals[sector][0] += reading
        zone_totals[sector][1] += 1
    
    avg_per_sector = {sec: tot[0]/tot[1] for sec, tot in zone_totals.items()}
    
    # Correct grouping: by zone_id with non-zero readings only
    field_data = defaultdict(list)
    for zone_id, sector, reading in raw_readings:
        if reading > 0:  # Filter out malfunctioning sensors
            field_data[zone_id].append(reading)
    
    return field_data, avg_per_sector

# Analyze harvest efficiency based on consistency and mean yield
def calculate_harvest_efficiency(data, min_threshold):
    efficiency_scores = []
    consistency_flags = []
    
    for zone_id, readings in data.items():
        base_mean = sum(readings) / len(readings)
        deviation = sum((r - base_mean) ** 2 for r in readings) / len(readings)
        std_dev = deviation ** 0.5
        
        # Determine consistency (low variance = consistent)
        is_consistent = std_dev < 15
        consistency_flags.append(is_consistent)
        
        # Scale score by mean but cap at threshold
        raw_score = base_mean * (1.2 if is_consistent else 0.8)
        capped_score = min(raw_score, min_threshold * 1.5)
        efficiency_scores.append(capped_score)
    
    # Final yield calculation: average of capped scores
    total_yield = sum(efficiency_scores)
    final_yield = total_yield / len(efficiency_scores) if efficiency_scores else 0
    
    # Irrelevant secondary metric (dead computation path)
    peak_zone = max((sum(v)/len(v), k) for k, v in data.items())
    peak_contribution = peak_zone[0] * 0.1  # Not used
    
    return final_yield

# Secondary helper: estimates water loss (unused in main flow)
def estimate_water_loss(zones):
    total_loss = 0
    for zid, vals in zones.items():
        loss_rate = 0.05 if len(vals) > 2 else 0.07
        total_loss += sum(vals) * loss_rate
    return round(total_loss, 2)

# Main execution
field_data, sector_averages = collect_field_data()
threshold = 130
final_yield = calculate_harvest_efficiency(field_data, threshold)

# Print result
print(f"Result: {final_yield}")