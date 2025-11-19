import math

class SurveyContext:
    def __init__(self, points):
        self.points = points
        self.processed_areas = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.points.clear()
    
    def calculate_triangle_area(self, p1, p2, p3):
        # Using shoelace formula
        return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)
    
    def find_optimal_triangle(self):
        max_area = 0
        n = len(self.points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    area = self.calculate_triangle_area(self.points[i], self.points[j], self.points[k])
                    if area > max_area:
                        max_area = area
        return max_area

# Tokenize coordinate data
def parse_coordinates(coord_str):
    tokens = coord_str.split(';')
    points = []
    for token in tokens:
        if token.strip():
            x, y = map(float, token.split(','))
            points.append((x, y))
    return points

# Input data representing surveyed points
survey_data = "0,0; 4,0; 2,3; 1,1; 3,2; 0,4; 4,4"

# Parse and process the data
parsed_points = parse_coordinates(survey_data)

visited_points = set()
unvisited_points = frozenset(parsed_points)

optimal_area = 0

with SurveyContext(parsed_points.copy()) as survey:
    temp_area = survey.find_optimal_triangle()
    if temp_area > optimal_area:
        optimal_area = temp_area
    
    # Greedy selection: remove one point and recalculate
    if parsed_points:
        parsed_points.pop()  # Remove last point
        temp_area = survey.find_optimal_triangle()
        if temp_area > optimal_area:
            optimal_area = temp_area

# Final calculation after context exit
if len(parsed_points) >= 3:
    with SurveyContext(parsed_points.copy()) as survey:
        final_area = survey.find_optimal_triangle()
        if final_area > optimal_area:
            optimal_area = final_area

print(f"Result: {optimal_area}")