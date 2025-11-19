import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def calculate_terrain_segment_value(x, y):
    elevation_profile = x**2 + 3*x*y + y**2
    prime_factorization = prime_factors(elevation_profile)
    if not prime_factorization:
        return 0
    segment_lcm = prime_factorization[0]
    for factor in prime_factorization[1:]:
        segment_lcm = lcm(segment_lcm, factor)
    return segment_lcm

def backtrack_optimal_path(terrain_grid, row, col, visited, current_score):
    if row < 0 or row >= len(terrain_grid) or col < 0 or col >= len(terrain_grid[0]):
        return current_score
    if (row, col) in visited:
        return current_score
    
    visited.add((row, col))
    cell_value = calculate_terrain_segment_value(row, col)
    new_score = current_score + cell_value
    
    # Recursive exploration in four directions
    scores = [
        backtrack_optimal_path(terrain_grid, row+1, col, visited.copy(), new_score),
        backtrack_optimal_path(terrain_grid, row-1, col, visited.copy(), new_score),
        backtrack_optimal_path(terrain_grid, row, col+1, visited.copy(), new_score),
        backtrack_optimal_path(terrain_grid, row, col-1, visited.copy(), new_score)
    ]
    
    return max(scores)

def analyze_survey_zone():
    survey_area = [
        [10, 15, 20],
        [25, 30, 35],
        [40, 45, 50]
    ]
    
    with open('survey_log.txt', 'w') as log_file:
        log_file.write("Survey initiated\n")
        max_scores = [
            backtrack_optimal_path(survey_area, i, j, set(), 0)
            for i in range(len(survey_area))
            for j in range(len(survey_area[0]))
        ]
        log_file.write("Analysis complete\n")
    
    optimal_survey_score = max(max_scores)
    return optimal_survey_score

# Execute the geospatial analysis
optimal_survey_score = analyze_survey_zone()
print(f"Result: {optimal_survey_score}")