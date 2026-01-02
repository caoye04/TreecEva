import re

def hex_to_int(hex_str):
    return int(hex_str, 16)

def elevation_filter(elevations, threshold=1000):
    return [e for e in elevations if e > threshold]

def calculate_volume(elevation_map, base_level=500):
    volume = 0
    for row in elevation_map:
        for elevation in row:
            if elevation > base_level:
                volume += elevation - base_level
    return volume

def process_terrain_data(terrain_hex_strings):
    # Convert hex strings to integers
    elevation_data = [[hex_to_int(cell) for cell in row.split()] for row in terrain_hex_strings]
    
    # Filter high elevation points
    filtered_elevation_data = [elevation_filter(row) for row in elevation_data]
    
    # Calculate required volume for site preparation
    total_volume = calculate_volume(filtered_elevation_data)
    return total_volume

# Terrain data in hexadecimal representation
raw_terrain_data = [
    "3E8 4B0 5DC 7D0 9C4",
    "1F4 2BC 3E8 4B0 5DC",
    "FA 1F4 2BC 3E8 4B0",
    "7D 1F4 2BC 3E8 5DC"
]

total_volume = process_terrain_data(raw_terrain_data)
print(f"Result: {total_volume}")