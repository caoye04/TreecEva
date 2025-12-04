from collections import defaultdict, Counter
import math

def calculate_orbit_stability(altitude, eccentricity):
    """Calculate orbit stability factor - higher is more stable"""
    return (altitude * (1 - eccentricity)) / 1000

def analyze_satellite_signal(signal_strength, noise_ratio):
    """Analyze if satellite signal is viable"""
    return signal_strength > 75 and noise_ratio < 0.3

# Satellite tracking data
altitudes = [550, 1200, 780, 35786, 620, 1450, 590]
orbital_periods = [96, 109, 100, 1436, 97, 115, 96]

# Signal metrics (dB)
signal_strengths = {"LEO": 82, "MEO": 68, "GEO": 59, "HEO": 47}
noise_factors = [0.18, 0.25, 0.32, 0.15, 0.22, 0.38, 0.21]

# Orbital system categorization
orbital_systems = defaultdict(int)
constellations = ["Starlink", "OneWeb", "Kuiper", "GlobalStar", "Iridium"]

# Track deployments per orbital shell
deployment_counter = Counter()
for i in range(5):
    shell_id = i % 3
    deployment_counter[shell_id] += i + 2

# Calculate viable satellite count
viable_count = sum(1 for alt, noise in zip(altitudes, noise_factors) 
                  if alt < 1000 and noise < 0.3)

# Process mission data
primary_mission_id = 0
secondary_mission_id = 2
total_missions = len(altitudes)

# Track active vs inactive satellites
for i, altitude in enumerate(altitudes):
    if i == secondary_mission_id:
        # This is a decoy calculation
        potential_satellites = int(math.sqrt(altitude) * 1.5)
        orbital_systems[i] = potential_satellites
    elif i == primary_mission_id:
        # Real calculation for the question
        active_satellites = 0
        for j in range(len(altitudes)):
            if analyze_satellite_signal(80 - (j*3), noise_factors[j]):
                active_satellites += 1
        orbital_systems[i] = active_satellites
    else:
        # More decoys
        orbital_systems[i] = int(altitude / 100)

# Misleading intermediate results
deployed_sats = sum(deployment_counter.values())
false_result = deployment_counter[0] * 2

# Distraction with lambda and slicing
sort_key = lambda x: x[0] * x[1]
zipped_data = list(zip(altitudes[:4], orbital_periods[:4]))
zipped_data.sort(key=sort_key)

# This line is the key to the question
active_satellites = orbital_systems[primary_mission_id]

# More distractions
final_stability = calculate_orbit_stability(altitudes[primary_mission_id], 0.001)
optimal_config = active_satellites * 2 > viable_count

print(f"Result: {active_satellites}")