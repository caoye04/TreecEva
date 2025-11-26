customer_ids_a = {101, 102, 103, 104, 105}
customer_ids_b = {103, 104, 105, 106, 107}

# Calculate union and intersection
union_set = customer_ids_a | customer_ids_b
intersection_set = customer_ids_a & customer_ids_b

# Final calculation
final_result = union_set - intersection_set
print(f"Result: {len(final_result)}")