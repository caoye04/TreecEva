def calculate_habitability(temp, radius, atmosphere):
    # Calculate planet habitability score
    # Higher values are more Earth-like
    base_score = 100 - abs(temp - 15) * 1.5
    size_factor = 85 if 0.8 <= radius <= 1.5 else 65
    atmosphere_bonus = 25 if atmosphere else 0
    
    return base_score * 0.6 + size_factor * 0.3 + atmosphere_bonus * 0.4

# Database of exoplanets with [temperature(°C), radius(Earth=1), has_atmosphere]
# Positive values in filtered_planets will represent potentially habitable worlds
exoplanet_data = [
    [42, 0.7, False],  # Too hot, small
    [10, 1.2, True],   # Good candidate
    [-5, 1.8, True],   # Too large but otherwise ok
    [14, 1.1, True],   # Excellent candidate
    [120, 2.3, False], # Too hot, too large
    [-150, 0.9, False] # Too cold
]

# Threshold for habitability
habitability_threshold = 70

# Process each planet
raw_scores = []
filtered_planets = []
disqualified = 0

for planet in exoplanet_data:
    temp, radius, atmosphere = planet
    
    # Some planets are automatically disqualified
    if temp > 100 or temp < -100:
        disqualified += 1
        raw_scores.append(-999)  # Sentinel value
        filtered_planets.append(-1)  # Not habitable
        continue
    
    # Calculate habitability score
    score = calculate_habitability(temp, radius, atmosphere)
    raw_scores.append(score)
    
    # Apply additional filters
    gravity_factor = radius ** 2
    adjusted_score = score
    
    # Adjust score based on gravity (not actually used)
    if 0.8 <= gravity_factor <= 1.5:
        adjusted_score += 5
    
    # Lambda for filtering water presence based on temperature
    has_liquid_water = lambda t: 0 <= t <= 50
    
    # Apply final filtering
    if score >= habitability_threshold and has_liquid_water(temp):
        filtered_planets.append(1)  # Habitable
    else:
        filtered_planets.append(-1)  # Not habitable

# Slice to get the first half of raw scores (unused)
first_half_scores = raw_scores[:len(raw_scores)//2]

# Count eligible planets
eligible_planets = len([p for p in filtered_planets if p > 0])

# Calculate average score (unused)
average_score = sum(score for score in raw_scores if score > 0) / len([s for s in raw_scores if s > 0])

print(f"Result: {eligible_planets}")