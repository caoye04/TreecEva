import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
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

# Rover state machine
states = {
    'NORTH': {'L': 'WEST', 'R': 'EAST'},
    'EAST': {'L': 'NORTH', 'R': 'SOUTH'},
    'SOUTH': {'L': 'EAST', 'R': 'WEST'},
    'WEST': {'L': 'SOUTH', 'R': 'NORTH'}
}

# Command sequence
commands = [12, 15, 8, 9, 7]

# Initialize rover
position = [0, 0]  # x, y
orientation = 'NORTH'

# Process commands
for cmd in commands:
    if cmd <= 1:
        continue
    
    factors = prime_factors(cmd)
    prime_count = sum(1 for f in factors if is_prime(f))
    
    if prime_count == 0:
        # No prime factors - turn right
        orientation = states[orientation]['R']
        continue
    elif prime_count == 1:
        # One prime factor - move forward
        distance = lcm(cmd, 6)
    else:
        # Multiple prime factors - move with modified distance
        distance = 1
        for f in set(factors):  # Unique factors only
            if is_prime(f):
                distance *= f
    
    # Movement based on orientation
    if orientation == 'NORTH':
        position[1] += distance
    elif orientation == 'EAST':
        position[0] += distance
    elif orientation == 'SOUTH':
        position[1] -= distance
    elif orientation == 'WEST':
        position[0] -= distance
    
    # Early termination condition
    if abs(position[0]) > 100 or abs(position[1]) > 100:
        break

# Calculate Euclidean distance
final_distance = math.sqrt(position[0]**2 + position[1]**2)
print(f"Result: {round(final_distance)}")