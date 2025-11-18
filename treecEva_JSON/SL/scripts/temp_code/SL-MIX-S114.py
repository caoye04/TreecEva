import math
from collections import defaultdict, deque

class DistrictNode:
    def __init__(self, district_id, vehicle_emissions):
        self.district_id = district_id
        self.vehicle_emissions = vehicle_emissions
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def calculate_pollution_score(emissions):
    # Modular arithmetic with geometry - emissions mod circle circumference (2*pi*10)
    circumference = 2 * math.pi * 10
    return int((emissions * 17) % circumference)

def compute_compliance_modifier(district_id, pollution_score):
    if is_prime(district_id):
        # Prime districts get compliance boost based on LCM with fixed value
        return lcm(pollution_score, 12)
    else:
        # Non-prime districts get penalty based on GCD
        return -gcd(pollution_score, 15)

# Build district tree
root_district = DistrictNode(1, 250)
child_2 = DistrictNode(2, 180)
child_3 = DistrictNode(3, 320)
child_4 = DistrictNode(4, 95)
child_5 = DistrictNode(5, 140)
child_6 = DistrictNode(6, 210)

root_district.add_child(child_2)
root_district.add_child(child_3)
child_2.add_child(child_4)
child_2.add_child(child_5)
child_3.add_child(child_6)

# Process districts using stack for DFS
processing_stack = [root_district]
cumulative_compliance_score = 0

while processing_stack:
    current_district = processing_stack.pop()
    pollution = calculate_pollution_score(current_district.vehicle_emissions)
    compliance_mod = compute_compliance_modifier(current_district.district_id, pollution)
    cumulative_compliance_score += compliance_mod
    
    # Add children to stack (reversed to maintain left-to-right processing)
    for child in reversed(current_district.children):
        processing_stack.append(child)

print(f"Result: {cumulative_compliance_score}")