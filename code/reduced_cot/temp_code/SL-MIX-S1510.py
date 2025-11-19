from functools import reduce
from collections import namedtuple

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_orbital_zone(radius):
    return radius ** 2 * 3.14159 // 10

def is_stable(orbit_a, orbit_b):
    return abs(orbit_a - orbit_b) > 5 or orbit_a + orbit_b < 50

Planet = namedtuple('Planet', ['name', 'orbital_radius', 'period_base'])

# Initialize planets with orbital data
planets = [
    Planet('Meridian', 12, 3),
    Planet('Vortex', 18, 5),
    Planet('Nebulus', 25, 8)
]

# Calculate orbital zones
zones = list(map(calculate_orbital_zone, [p.orbital_radius for p in planets]))

# Determine stability between adjacent planets
stability_flags = [
    is_stable(zones[i], zones[i+1]) 
    for i in range(len(zones)-1)
]

# Compute Fibonacci-adjusted periods
fib_periods = [
    fibonacci(p.period_base) * (2 if stable else 1)
    for p, stable in zip(planets, stability_flags + [True])
]

# Calculate resonance index using short-circuit evaluation
resonance_index = 0
i = 0
while i < len(fib_periods) and (lambda x: x < 100)(fib_periods[i]):
    resonance_index += fib_periods[i] if fib_periods[i] > 10 else 0
    i += 1

# Final adjustment using ternary operator
resonance_index = resonance_index if resonance_index % 2 == 0 else resonance_index * 2

print(f"Result: {resonance_index}")