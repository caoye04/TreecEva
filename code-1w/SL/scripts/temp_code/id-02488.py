def main():
    # Sensor readings from renewable energy system
    solar_yield = 3.7
    wind_yield = 2.4
    efficiency_factor = 0.85

    # Lambda to adjust for grid load
    load_adjuster = lambda x: x * 1.1 if x < 4 else x * 0.95

    # Adjust yields based on current grid demand
    adjusted_solar = load_adjuster(solar_yield)
    adjusted_wind = load_adjuster(wind_yield)

    # Combined energy contribution
    total_energy = adjusted_solar + adjusted_wind

    # Apply system efficiency and convert to kWh
    energy_output = total_energy * efficiency_factor * 1000

    # Irrelevant telemetry (minimal distraction)
    status_code = 200
    timestamp = "12:34:56"

    return energy_output

result = main()
print(f"Result: {result}")