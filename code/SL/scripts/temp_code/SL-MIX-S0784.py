from functools import reduce

def hash_string(s):
    return reduce(lambda acc, char: (acc * 31 + ord(char)) % 1000007, s, 0)

def assign_zone(weight, destination):
    base_zone = hash_string(destination)
    if weight > 50:
        return (base_zone + 7) % 13
    return base_zone % 13

packages = [
    {'weight': 45, 'destination': 'ZoneA'},
    {'weight': 60, 'destination': 'ZoneB'},
    {'weight': 30, 'destination': 'ZoneC'},
    {'weight': 75, 'destination': 'ZoneA'},
]

delivery_zone_load = 0
for pkg in packages:
    zone = assign_zone(pkg['weight'], pkg['destination'])
    if zone == 0:
        delivery_zone_load += pkg['weight'] * 2
        break
    elif zone % 2 == 0:
        delivery_zone_load += pkg['weight']
    else:
        delivery_zone_load -= pkg['weight'] // 2

print(f"Result: {delivery_zone_load}")