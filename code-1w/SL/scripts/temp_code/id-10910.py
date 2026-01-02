def analyze_terrain_data():
    # Terrain elevation data (in meters)
    elevations = [127, 89, 203, 65, 154, 98, 188, 76, 142]

    # Temperature readings (in tenths of °C)
    temperatures = [235, 198, 276, 165, 250, 187, 266, 175, 241]

    # Initial filtering: regions suitable for vegetation (elevation between 70 and 190)
    viable_elevations = {i for i, e in enumerate(elevations) if 70 <= e <= 190}

    # Regions with temperature conducive to growth (> 180)
    warm_regions = {i for i, t in enumerate(temperatures) if t > 180}

    # Candidate zones based on combined criteria
    candidate_zones = viable_elevations.intersection(warm_regions)

    # Simulated soil quality index (arbitrary units)
    soil_quality = [0.4, 0.8, 0.3, 0.9, 0.6, 0.7, 0.2, 0.85, 0.5]

    # Identify high-quality soil patches
    high_soil_quality = {i for i, sq in enumerate(soil_quality) if sq >= 0.7}

    # Overhead computation: normalize temperature values (not used later)
    normalized_temps = [round((t - min(temperatures)) / (max(temperatures) - min(temperatures)), 3) for t in temperatures]

    # Historical rainfall data (mm per year, last 5 years)
    rainfall_history = [
        [450, 480, 510, 490, 530],
        [390, 410, 400, 420, 440],
        [520, 550, 530, 570, 590],
        [310, 330, 350, 340, 360],
        [470, 460, 490, 500, 510],
        [400, 420, 410, 430, 450],
        [290, 300, 320, 310, 330],
        [460, 480, 470, 490, 500],
        [440, 450, 460, 470, 480]
    ]

    # Average rainfall per region
    avg_rainfall = [sum(rains)/len(rains) for rains in rainfall_history]

    # Identify regions with stable rainfall (low variance)
    rainfall_variance = [(sum((r - avg_rainfall[i])**2 for r in rainfall_history[i]) / len(rainfall_history[i]))**0.5 for i in range(len(rainfall_history))]
    stable_rainfall = {i for i, rv in enumerate(rainfall_variance) if rv < 15}

    # Combine ecological factors
    ecological_fragments = candidate_zones.union(high_soil_quality).intersection(stable_rainfall)

    # Unused backup set for alternative logic path
    fallback_regions = {i for i in range(len(elevations)) if elevations[i] > 100 and temperatures[i] > 200}

    # Potential zones from satellite imagery analysis (some overlap)
    potential_zones = {0, 1, 3, 4, 5, 7, 8}

    # Qualified regions from field survey
    qualified_regions = {1, 2, 4, 5, 7}

    # Correction factor based on atmospheric pressure drift (simulated)
    base_pressure = 1013.25
    daily_drift = [0.1, -0.2, 0.3, -0.1, 0.0, 0.2]
    adjusted_pressure = base_pressure
    for delta in daily_drift:
        adjusted_pressure += delta * 2.5
    correction_factor = int(round(adjusted_pressure / 100))  # Results in 10

    # Irrelevant transformation: reverse slicing of elevation segments
    reversed_segments = [elevations[i:i+3][::-1] for i in range(0, len(elevations), 3)]

    # Key computation with set operations and slicing
    partial_overlap = len(set(elevations[1:6]).intersection(set([150, 100, 200, 98, 154])))

    # Main scoring metric
    filtration_score = len(qualified_regions.intersection(potential_zones)) * correction_factor

    # Additional unused state tracking
    state_log = []
    for idx in sorted(ecological_fragments):
        state_log.append(f"Region{idx}: Active")

    print(f"Result: {filtration_score}")

analyze_terrain_data()