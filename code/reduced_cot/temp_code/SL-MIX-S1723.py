from collections import defaultdict
from math import gcd

def calculate_min_delivery_cost(cities_pop, toll_routes):
    # Create a DP table initialized with infinity
    dp = defaultdict(lambda: float('inf'))
    start_city = 'A'
    dp[start_city] = 0
    
    # Process each route
    for _ in range(len(cities_pop) - 1):
        updated = False
        for (u, v), toll in toll_routes.items():
            if dp[u] != float('inf') and gcd(cities_pop[u], cities_pop[v]) > 1:
                if dp[u] + toll < dp[v]:
                    dp[v] = dp[u] + toll
                    updated = True
        if not updated:
            break
    
    return dp['E']

# City populations
populations = {
    'A': 120,
    'B': 80,
    'C': 150,
    'D': 90,
    'E': 100
}

# Toll routes between cities
routes = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('B', 'C'): 5,
    ('B', 'D'): 20,
    ('C', 'D'): 10,
    ('C', 'E'): 25,
    ('D', 'E'): 5
}

optimized_cost = calculate_min_delivery_cost(populations, routes)
print(f"Result: {optimized_cost}")