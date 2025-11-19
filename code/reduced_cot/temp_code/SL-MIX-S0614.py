total_items = 120
# Let s be sourdough breads, c be croissants
# Constraint 1: s + c = 120
# Constraint 2: c >= 2*s

# To maximize s, we use the boundary condition where c = 2*s
# Substituting into constraint 1: s + 2*s = 120 => 3*s = 120 => s = 40
max_sourdough = total_items // 3

# Verify with logical operations
s = max_sourdough
c = total_items - s
is_valid = (s + c == total_items) and (c >= 2 * s)

if is_valid:
    result = max_sourdough
else:
    result = -1  # Should not happen with correct calculation

print(f'Result: {result}')