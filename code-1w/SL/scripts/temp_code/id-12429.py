def main():
    # Reactor core parameters
    temperature = 5800
    pressure = 230
    fuel_rod_count = 37

    # Safety threshold constants (irrelevant distractors)
    max_temperature_limit = 6000
    min_pressure_threshold = 100

    # Core state represented as tuple
    nuclear_state = (temperature, pressure, fuel_rod_count)

    # Lambda to compute efficiency from core state
    calculate_efficiency = lambda state: (state[0] // 100) * (state[2] % 10) - state[1] // 20

    # Critical computation step
    energy_output = calculate_efficiency(nuclear_state)

    # Print result for evaluation
    print(f"Result: {energy_output}")

if __name__ == "__main__":
    main()