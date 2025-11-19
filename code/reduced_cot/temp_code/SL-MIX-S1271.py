import itertools

package_weights = [12, 29, 8, 45, 17, 33, 26]
valid_route_count = 0

# Calculate reference modulus from first package
reference_mod = package_weights[0] % 17

# Generate all 3-package combinations
for combo in itertools.combinations(package_weights, 3):
    total_weight = sum(combo)
    if total_weight % 17 == reference_mod:
        valid_route_count += 1

print(f"Result: {valid_route_count}")