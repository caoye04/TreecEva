import math
from collections import defaultdict

def calculate_building_efficiency(footprints, energy_usage):
    scores = defaultdict(float)
    for building_id in footprints:
        area = footprints[building_id]
        energy = energy_usage.get(building_id, 0)
        
        # Normalize area using logarithm
        log_area = math.log(area + 1) if area > 0 else 0
        
        # Exponential decay of energy usage
        exp_energy = math.exp(-energy / 100) if energy > 0 else 1
        
        # Base efficiency score
        base_score = log_area * exp_energy * 10
        scores[building_id] = base_score
    
    # Statistical adjustment using mean and standard deviation
    values = list(scores.values())
    mean_score = sum(values) / len(values) if values else 0
    variance = sum((x - mean_score) ** 2 for x in values) / len(values) if values else 0
    std_dev = math.sqrt(variance) if variance > 0 else 1
    
    # Adjust scores using statistical measures
    adjusted_scores = {}
    for b_id, score in scores.items():
        z_score = (score - mean_score) / std_dev if std_dev != 0 else 0
        adjusted_scores[b_id] = score + z_score  # Apply adjustment
    
    return adjusted_scores

# Building data: footprint areas in square meters
building_footprints = {
    'B001': 1200,
    'B002': 800,
    'B003': 1600,
    'B004': 950,
    'B005': 1300
}

# Energy usage in kWh
building_energy = {
    'B001': 2400,
    'B002': 1800,
    'B003': 3200,
    'B004': 2100,
    'B005': 2600
}

# Calculate efficiencies
efficiencies = calculate_building_efficiency(building_footprints, building_energy)

# Spatial adjustment factor based on relative positions
spatial_factors = {
    'B001': 1.05,
    'B002': 0.98,
    'B003': 1.12,
    'B004': 1.02,
    'B005': 0.99
}

# Apply spatial factors
final_adjusted = {}
for b_id in efficiencies:
    factor = spatial_factors.get(b_id, 1.0)
    final_adjusted[b_id] = efficiencies[b_id] * factor

# Determine final score as the maximum adjusted score
final_score = max(final_adjusted.values()) if final_adjusted else 0

print(f"Result: {final_score}")