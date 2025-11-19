from collections import defaultdict

class EnergyZone:
    def __init__(self, name, consumption_data):
        self.name = name
        self.consumption_data = consumption_data
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def compute_zone_efficiency(zone_data):
    base_efficiency = sum(zone_data) // len(zone_data)
    peak_consumption = max(zone_data)
    if peak_consumption > 0:
        return base_efficiency * 100 // peak_consumption
    return 0

building_zones = {
    'ZONE_ALPHA': [120, 90, 110, 80],
    'ZONE_BETA': [200, 150, 180, 160],
    'ZONE_GAMMA': [75, 85, 95, 105]
}

zone_efficiencies = {}
cumulative_efficiency_score = 0
threshold = 70

for zone_name, data in building_zones.items():
    with EnergyZone(zone_name, data) as zone:
        efficiency = compute_zone_efficiency(zone.consumption_data)
        zone_efficiencies[zone_name] = efficiency
        
        if efficiency >= threshold and (efficiency & 0x01):  # Check if efficiency meets threshold AND is odd
            cumulative_efficiency_score += efficiency
        elif efficiency < threshold or not (efficiency & 0x01):  # Short-circuit evaluation
            cumulative_efficiency_score -= efficiency >> 2  # Right shift by 2 (equivalent to dividing by 4)

# Adjust final score based on overall performance
if all(eff >= threshold for eff in zone_efficiencies.values()):
    cumulative_efficiency_score <<= 1  # Left shift by 1 (multiply by 2)
elif any(eff < threshold for eff in zone_efficiencies.values()):
    cumulative_efficiency_score >>= 1  # Right shift by 1 (divide by 2)

print(f"Result: {cumulative_efficiency_score}")