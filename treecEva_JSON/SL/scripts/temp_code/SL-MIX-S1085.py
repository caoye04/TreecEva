import base64
import hashlib

def calculate_package_priority(identifier):
    encoded = base64.b64encode(identifier.encode()).decode()
    hash_obj = hashlib.md5(encoded.encode())
    return int(hash_obj.hexdigest(), 16) % 1000

package_manifest = [
    {'id': 'PKG001', 'weight': 25},
    {'id': 'PKG002', 'weight': 18},
    {'id': 'PKG003', 'weight': 32},
    {'id': 'PKG004', 'weight': 15},
    {'id': 'PKG005', 'weight': 28}
]

# Encode and calculate priorities
encoded_priorities = [(pkg['id'], calculate_package_priority(pkg['id']), pkg['weight']) for pkg in package_manifest]

# Sort by priority (descending) and apply greedy selection
sorted_packages = sorted(encoded_priorities, key=lambda x: x[1], reverse=True)

# Greedy selection: select packages where priority > 500 AND weight <= 30
selected_weights = [pkg[2] for pkg in sorted_packages if pkg[1] > 500 and pkg[2] <= 30]

# Apply another filter using logical OR
final_selection = list(filter(lambda w: w > 20 or w < 16, selected_weights))

# Calculate optimized load
optimized_load = sum(final_selection)

print(f"Result: {optimized_load}")