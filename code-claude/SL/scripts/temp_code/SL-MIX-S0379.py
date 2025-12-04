# Solar Panel Efficiency Analysis

def calculate_panel_rating(efficiency, age):
    """Calculate panel rating based on efficiency and age"""
    base_score = efficiency * 100
    age_factor = max(0, 1 - (age / 20))  # Panels degrade over time
    return base_score * age_factor

# Panel data: (efficiency percentage, age in years, orientation)
raw_panels = [
    (0.21, 2, 'south'),
    (0.18, 5, 'west'),
    (0.22, 1, 'south'),
    (0.17, 7, 'east'),
    (0.19, 4, 'south'),
    (0.20, 3, 'west')
]

# Weather conditions - not directly used for final calculation
weather_factors = {
    'sunny': 1.0,
    'partly_cloudy': 0.8,
    'overcast': 0.6,
    'rainy': 0.4
}

# Current weather - for informational purposes only
current_weather = 'partly_cloudy'
weather_impact = weather_factors[current_weather]

# Calculate theoretical max output based on panel specs
theoretical_max = sum(eff for eff, _, _ in raw_panels)

# Extract just the south-facing panels for analysis
south_panels = [panel for panel in raw_panels if panel[2] == 'south']

# Calculate adjusted ratings for all panels
panel_ratings = [calculate_panel_rating(eff, age) for eff, age, _ in raw_panels]

# Threshold for high-efficiency panels (>= 0.19 efficiency)
high_efficiency_threshold = 0.19

# Filter panels based on efficiency threshold
efficient_panels = [eff for eff, _, _ in raw_panels if eff >= high_efficiency_threshold]

# Alternative filtering approach - not used in final calculation
alternative_filter = [(eff, age) for eff, age, _ in raw_panels if eff >= 0.20 or age <= 3]

# Apply orientation bonus to theoretical calculation (not used in final answer)
orientation_bonus = {'south': 1.2, 'west': 1.0, 'east': 0.9, 'north': 0.7}
theoretical_with_bonus = sum(eff * orientation_bonus[orient] for eff, _, orient in raw_panels)

# Calculate the main metric - sum of high efficiency panel values
filter_result = [eff for eff in efficient_panels]
filtered_efficiency = sum(filter_result)

# Calculate average age - not used in final answer
average_age = sum(age for _, age, _ in raw_panels) / len(raw_panels)

print(f"Result: {filtered_efficiency}")