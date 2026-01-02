def analyze_soil_quality(reading):
    # Complex but partially irrelevant transformation
    base = sum([r ** 0.5 for r in reading if r > 25])
    adjustment = len(reading) * 0.3 if base > 40 else len(reading) * 0.1
    return base + adjustment

# Simulated sensor data from agricultural plots
sensor_readings = [
    [30, 45, 50, 60],
    [20, 35, 40, 42],
    [55, 58, 65, 70],
    [10, 15, 20, 25]
]

# Irrelevant baseline metrics (distractor)
avg_temp = 22.5
rainfall_mm = 89.0
elevation_bias = 127

# Preprocessing with slicing and filtering
processed_plots = []
for i, reading in enumerate(sensor_readings):
    if sum(reading) < 100:
        continue  # Skip low-yield candidates
    segment = reading[1:3]  # Middle sensors only
    score = analyze_soil_quality(segment)
    processed_plots.append((i, score, len(segment)))

# Additional irrelevant computation (dead path)
temp_analysis = []
for p in sensor_readings:
    temp_analysis.append([x * 0.02 for x in p if x % 10 == 0])

# Core logic: yield estimation based on processed plot scores
def calculate_harvest_potential(plots):
    total = 0.0
    multiplier = 1.0
    for entry in plots:
        idx, score, length = entry
        # Real contribution
        if idx % 2 == 0:
            total += score * 1.2
        else:
            total += score * 0.8
        # Irrelevant internal tracking
        multiplier *= (score / max(score, 1))
    
    # Final adjustment using slicing on indices
    indices = [p[0] for p in plots]
    if len(indices) > 2:
        window = indices[1:3]
        total += sum(window) * 0.5
    return round(total, 4)

# State-tracking variables (some irrelevant)
execution_phase = "post-processing"
diagnostic_log = {"plots_analyzed": len(processed_plots)}

# Key execution point
final_yield = calculate_harvest_potential(processed_plots)

# Output result as required
print(f"Target result: {final_yield}")