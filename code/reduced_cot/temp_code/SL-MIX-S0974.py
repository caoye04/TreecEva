set_a = {2, 5, 8, 11, 14}
set_b = {3, 6, 9, 12, 15}
set_c = {4, 7, 10, 13, 16}

# Perform set operations
union_ab = set_a.union(set_b)
intersection_ab = set_a.intersection(set_b)
union_abc = union_ab.union(set_c)
intersection_abc = union_ab.intersection(set_c)

# Calculate symmetric difference
union_set = union_abc
intersection_set = intersection_abc
final_value = len(union_set - intersection_set)

print(f"Result: {final_value}")