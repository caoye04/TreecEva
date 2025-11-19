import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

flour_required = 240
dough_required = 360

minimum_packages = lcm(flour_required, dough_required) // 120
print(f'Result: {minimum_packages}')