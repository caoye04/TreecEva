# Satellite Fleet Management System
# Calculate active satellites in optimal orbits

# Initial satellite configuration
satellite_ids = ["SAT-A", "SAT-B", "SAT-C", "SAT-D", "SAT-E", "SAT-F"]
operational_status = [True, False, True, True, True, False]
altitude_data = [720, 680, 790, 750, 810, 700]  # km
telemetry_signals = [98, 0, 87, 92, 76, 0]  # signal strength percentage

# Configuration parameters
min_altitude = 700  # minimum operational altitude
optimal_signal = 80  # optimal signal strength threshold

# Analyze satellite performance metrics
performance_index = 0
signal_quality = 0

# Process satellite fleet data
for i, (sat_id, status) in enumerate(zip(satellite_ids, operational_status)):
    # Calculate potential coverage area (not used in final calculation)
    potential_coverage = 3.14 * (altitude_data[i] ** 2) / 100
    
    # Track signal quality for reporting purposes
    if status and telemetry_signals[i] > 0:
        signal_quality += telemetry_signals[i]
    
    # Check if satellite meets performance criteria
    if status and telemetry_signals[i] >= optimal_signal:
        performance_index += 1

# Determine average signal quality
avg_signal = signal_quality / sum(1 for status, signal in zip(operational_status, telemetry_signals) 
                                if status and signal > 0)

# Count satellites that are operational and above minimum altitude
active_satellites = sum(1 for sat_id, status in zip(satellite_ids, operational_status) 
                      if status and altitude_data[i] > min_altitude)

# Calculate fleet reliability score (not used in final result)
reliability_score = (active_satellites / len(satellite_ids)) * 100

# Determine if fleet meets operational requirements
fleet_operational = active_satellites >= 3 and avg_signal > 85

print(f"Result: {active_satellites}")