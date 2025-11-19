import math

def compute_egg_packages(croissants, tarts, muffins):
    egg_per_croissant = 4
    egg_per_tart = 6
    egg_per_muffin = 3
    eggs_per_package = 12
    
    total_eggs = (croissants * egg_per_croissant +
                  tarts * egg_per_tart +
                  muffins * egg_per_muffin)
    
    return math.ceil(total_eggs / eggs_per_package)

# Daily orders
bakery_orders = {
    'croissants': 15,
    'tarts': 10,
    'muffins': 20
}

# Calculate packages needed
packages_needed = compute_egg_packages(
    bakery_orders['croissants'],
    bakery_orders['tarts'],
    bakery_orders['muffins']
)

print(f"Result: {packages_needed}")