from math import gcd, sqrt
from collections import namedtuple

# Define celestial body data structure
Body = namedtuple('Body', ['name', 'x', 'y', 'mass'])

# Prime generator function
def get_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# Context manager for coordinate transformation
class CoordinateTransformer:
    def __init__(self, bodies):
        self.bodies = bodies
        self.transformed = []
    
    def __enter__(self):
        # Apply geometric transformation: rotation by 45 degrees
        cos_45 = sin_45 = sqrt(2)/2
        for body in self.bodies:
            new_x = body.x * cos_45 - body.y * sin_45
            new_y = body.x * sin_45 + body.y * cos_45
            self.transformed.append(Body(body.name, new_x, new_y, body.mass))
        return self.transformed
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Initialize celestial bodies
celestial_bodies = [
    Body('Alpha', 10, 20, 5),
    Body('Beta', 15, 25, 3),
    Body('Gamma', 30, 10, 7),
    Body('Delta', 5, 15, 2)
]

# Get primes up to 100
prime_numbers = get_primes(100)

# Dictionary comprehension for body-prime mapping
body_prime_map = {body.name: prime for body, prime in zip(celestial_bodies, prime_numbers)}

# Apply coordinate transformation
with CoordinateTransformer(celestial_bodies) as transformed_bodies:
    # Filter bodies based on distance from origin and mass
    filtered_bodies = [
        body for body in transformed_bodies 
        if sqrt(body.x**2 + body.y**2) > 20 and body.mass >= 3
    ]
    
    # Calculate hash values using prime mapping and GCD
    hash_values = [
        body_prime_map.get(body.name, 1) * gcd(int(body.x), int(body.y))
        for body in filtered_bodies
        if body.name in body_prime_map  # Short-circuit evaluation
    ]
    
    # Compute final hash sum using ternary operator for conditional addition
    final_hash_sum = sum(
        value if value % 2 == 0 else value * 2
        for value in hash_values
    )

print(f"Result: {final_hash_sum}")