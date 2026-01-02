def main():
    # Sensor data from thermal array (simulated)
    raw_readings = [23.5, 24.1, 22.8, 25.6, 26.3, 21.9, 27.0, 20.4]
    
    # Filter out values below median to focus on high-heat zones
    sorted_readings = sorted(raw_readings)
    median_value = sorted_readings[len(sorted_readings) // 2]
    high_heat_zones = [x for x in raw_readings if x >= median_value]
    
    # Apply nonlinear transformation using lambda for thermal weighting
    thermal_weight = lambda t: round(t ** 1.15, 2)
    transformed_data = list(map(thermal_weight, high_heat_zones))
    
    # Calculate system efficiency based on transformed sensor data
    def calculate_efficiency(data):
        base_efficiency = sum(data) / len(data)
        adjustment_factor = 0.92 if len(data) > 3 else 1.05
        return int(base_efficiency * adjustment_factor)
    
    energy_threshold = None
    energy_threshold = calculate_efficiency(transformed_data)
    
    # Irrelevant diagnostic log (minimal distraction)
    debug_mode = False
    if debug_mode:
        print(f"Raw: {raw_readings}, Transformed: {transformed_data}")
    
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()