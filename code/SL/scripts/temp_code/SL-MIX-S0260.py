from functools import reduce
from collections import Counter

def compute_modular_hash(timestamps):
    return reduce(lambda x, y: (x * 31 + y) % 1009, timestamps, 0)

def get_role_weights(roles):
    weights = {'admin': 97, 'operator': 71, 'analyst': 53, 'guest': 11}
    return [weights[r] for r in roles if r in weights]

# System configuration
active_roles = ['operator', 'analyst', 'guest', 'admin']
time_markers = [1623456789, 1623456889, 1623456989, 1623457089]

# Token generation process
role_weights = get_role_weights(active_roles)
hash_value = compute_modular_hash(time_markers)

# Clearance computation with short-circuit logic
is_critical_window = (time_markers[-1] % 86400) > 75600  # Last 3 hours of day
has_admin_role = 'admin' in active_roles

if is_critical_window and has_admin_role:
    clearance_boost = 2
elif is_critical_window or not has_admin_role:
    clearance_boost = 1
else:
    clearance_boost = 0

# Final clearance calculation
base_clearance = sum(role_weights) % 100
weighted_hash = (hash_value * clearance_boost) % 100
final_clearance_level = (base_clearance + weighted_hash) % 50

print(f'Result: {final_clearance_level}')