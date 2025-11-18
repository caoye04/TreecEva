preserved_set = {1001, 1002, 1003, 1004}
archived_set = {1003, 1004, 1005, 1006}

unique_to_preserved = preserved_set - archived_set
permanent_index = frozenset(unique_to_preserved)
final_index_sum = sum(permanent_index)

print(f"Result: {final_index_sum}")