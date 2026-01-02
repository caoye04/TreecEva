def analyze_water_reservoir():
    # Simulate sensor readings from different zones in a water reservoir
    zone_a_readings = [12.5, 13.0, 11.8, 14.2, 13.7]
    zone_b_readings = [9.8, 10.4, 11.0, 10.1, 9.5]
    zone_c_readings = [7.6, 8.0, 7.4, 8.2, 7.9]

    # Calculate average flow per zone (distraction - not directly used)
    avg_a = sum(zone_a_readings) / len(zone_a_readings)
    avg_b = sum(zone_b_readings) / len(zone_b_readings)
    avg_c = sum(zone_c_readings) / len(zone_c_readings)

    # Identify peak readings for maintenance log (distractor data)
    peak_readings = []
    for i, val in enumerate(zone_a_readings):
        if val > 13.0:
            peak_readings.append((i, val))
    
    # Track temporal trends (semi-relevant but unused later)
    trends = []
    for prev, curr in zip(zone_a_readings, zone_a_readings[1:]):
        trends.append(curr - prev)

    # Actual inflow sources (relevant)
    inflows = [120, 85, 135, 95]  # Water input from rivers, rainfall, etc.
    inflow_labels = ['river', 'rain', 'groundwater', 'recycled']

    # Outflows through usage and evaporation (relevant)
    outflows = [98, 45, 102, 33, 12]  # Usage in agriculture, households, losses
    outflow_labels = ['agriculture', 'household', 'evaporation', 'industry', 'overflow']

    # Redundant safety check with no impact (dead code path)
    safety_margin = 5.0
    total_capacity = 500
    current_estimate = sum(inflows) * 0.9
    if current_estimate > total_capacity - safety_margin:
        status = 'WARNING'
    else:
        status = 'NORMAL'

    # Core calculation: net water flow into the system
    net_flow = sum(inflows) - sum(outflows)

    # Spurious transformation on labels (irrelevant)
    processed_labels = [label.upper()[:3] for label in inflow_labels]

    # Print result as required
    print(f"Result: {net_flow}")

analyze_water_reservoir()