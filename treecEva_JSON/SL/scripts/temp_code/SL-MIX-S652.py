import math
from collections import defaultdict

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

ingredient_requirements = {
    'flour': [200, 150, 300],
    'sugar': [100, 75, 200],
    'eggs': [6, 4, 8]
}

ingredient_package_sizes = {
    'flour': 500,
    'sugar': 250,
    'eggs': 12
}

total_packages = 0
for ingredient, amounts in ingredient_requirements.items():
    package_size = ingredient_package_sizes[ingredient]
    # Find LCM of all required amounts for this ingredient
    current_lcm = amounts[0]
    for amount in amounts[1:]:
        current_lcm = lcm(current_lcm, amount)
    # Calculate packages needed for this LCM batch size
    packages_for_lcm = current_lcm // package_size
    total_packages += packages_for_lcm

print(f"Result: {total_packages}")