# Calculate total distance traveled during a hiking expedition

# Define elevation zones and their respective elevation gains
elevation_zones = {
    'forest': 120,
    'rocky': 250,
    'alpine': 180
}

# Trail segments with distance in kilometers and terrain type
trail_data = [
    {'distance': 3.5, 'terrain': 'forest'},
    {'distance': 2.8, 'terrain': 'rocky'},
    {'distance': 4.2, 'terrain': 'forest'},
    {'distance': 1.5, 'terrain': 'alpine'}
]

# Calculate adjusted distances based on terrain difficulty
trip_segments = [segment['distance'] * (1 + elevation_zones[segment['terrain']]/1000) 
                 for segment in trail_data]

# Total distance with elevation adjustment
final_distance = sum(trip_segments)

print(f"Adjusted hiking distance: {final_distance:.2f} km")
