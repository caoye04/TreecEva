# Analyzing diving conditions for reef exploration

# Water parameters
water_temp = 28  # in Celsius
water_clarity = 0.7  # visibility factor (0-1)
oxygen_level = 92  # percent saturation

# Calculate safety thresholds
safety_factor = water_temp * 0.5 + oxygen_level * 0.2
base_depth = 15  # meters

# Depth adjustments based on conditions
temp_adjustment = (water_temp - 25) * 1.2 if water_temp > 25 else 0
clarity_penalty = 0
if water_clarity < 0.4:
    clarity_penalty = 8
elif water_clarity < 0.7:
    clarity_penalty = 4
else:
    clarity_penalty = 0

# Calculate potential depths
max_depth = base_depth + temp_adjustment
safe_depth = max_depth - clarity_penalty

# Depth recommendations
ideal_depth = safe_depth * 0.8
min_depth = ideal_depth - 5
max_recommended = safe_depth * 0.9

# Calculate average depth for various dive profiles
dive_profiles = [min_depth, ideal_depth, safe_depth]
avg_depth = sum(dive_profiles) / len(dive_profiles)

# Unused variables for different analysis scenarios
current_strength = 2.5  # knots
wave_height = 0.8  # meters
wind_speed = 12  # knots

# Determine optimal depth based on water clarity
optimal_depth = max(avg_depth, min_depth) if water_clarity > 0.5 else min_depth

# Additional calculations for research purposes
survey_area = (optimal_depth * 2) ** 2  # square meters
estimated_species = int(survey_area * 0.15)  # species count estimate

print(f"Result: {optimal_depth}")