class SecureProcessor:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def calculate_perimeter(coords):
    coords.append(coords[0])
    perimeter = sum(
        ((coords[i][0] - coords[i+1][0])**2 + (coords[i][1] - coords[i+1][1])**2)**0.5
        for i in range(len(coords)-1)
    )
    return round(perimeter, 2)

elevation_points = [100, 102, 101, 105, 103, 107]
survey_coordinates = [(0,0), (3,0), (3,4), (0,4)]

with SecureProcessor() as sp:
    differences = [
        abs(elevation_points[i] - elevation_points[i+1])
        for i in range(len(elevation_points)-1)
    ]
    consistent_changes = sum(1 for d in differences if d <= 2)
    total_comparisons = len(differences)
    consistency_ratio = consistent_changes / total_comparisons if total_comparisons else 0
    
    area = 3 * 4
    perimeter = calculate_perimeter(survey_coordinates)
    geometric_factor = perimeter / (area**0.5)
    
    stability_index = round(consistency_ratio * geometric_factor, 4)

print(f"Result: {stability_index}")