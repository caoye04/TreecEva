import math

def process_survey_data(points_file):
    coordinates = []
    with open(points_file, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split(','))
            coordinates.append((x, y))
    
    boundary_segments = []
    for i in range(len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % len(coordinates)]
        segment_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        boundary_segments.append(segment_length)
    
    return boundary_segments

def calculate_property_metrics(segments):
    total_perimeter = sum(segments)
    avg_segment = total_perimeter / len(segments) if segments else 0
    
    # Normalize using modular arithmetic
    normalized_indices = [
        int(round(seg / avg_segment)) % 7 
        for seg in segments 
        if seg > 0 and avg_segment > 0
    ]
    
    return normalized_indices

def main():
    # Simulate file creation
    with open('survey_points.txt', 'w') as f:
        f.write("0,0\n4,0\n4,3\n0,3\n-1,1\n2,5\n")
    
    # Process survey data with context manager
    survey_segments = process_survey_data('survey_points.txt')
    
    # Calculate metrics using list comprehension
    metric_indices = calculate_property_metrics(survey_segments)
    
    # Apply geometric validation with short-circuit evaluation
    boundary_index = 0
    for idx, metric in enumerate(metric_indices):
        is_valid_geometry = metric > 0 and (
            metric < len(survey_segments) or 
            (metric == len(survey_segments) and idx % 2 == 0)
        )
        
        if is_valid_geometry:
            # Use modular arithmetic to update boundary index
            boundary_index = (boundary_index * 3 + idx * 2) % 13
    
    return boundary_index

boundary_index = main()
print(f"Result: {boundary_index}")