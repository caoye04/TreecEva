from collections import defaultdict
import math

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

def prime_factors_count(n):
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    if n > 2:
        count += 1
    return count

particles = [
    ('C6H12O6', 24),
    ('H2O', 8),
    ('NaCl', 15),
    ('CO2', 10),
    ('CH4', 6)
]

interaction_map = defaultdict(int)
for identifier, count in particles:
    interaction_map[identifier] = count

sorted_identifiers = sorted(interaction_map.keys())
stability_weights = {}

for idx, identifier in enumerate(sorted_identifiers):
    interaction_count = interaction_map[identifier]
    prime_factor_count = prime_factors_count(interaction_count)
    position_weight = idx + 1
    
    match identifier[0]:
        case 'C':
            element_modifier = 4
        case 'H':
            element_modifier = 1
        case 'N':
            element_modifier = 7
        case 'O':
            element_modifier = 8
        case _:
            element_modifier = 2
    
    if is_prime(interaction_count):
        stability_weights[identifier] = prime_factor_count * position_weight * element_modifier * 2
    else:
        stability_weights[identifier] = prime_factor_count * position_weight * element_modifier

stability_index = sum(stability_weights.values())

print(f"Result: {stability_index}")