data_pairs = [('item_a', 15), ('item_b', 22), ('item_c', 8), ('item_d', 31), ('item_e', 42)]
result_data = {k: v for k, v in data_pairs if v % 2 == 0}
filtered_items = set(result_data.keys())
reference_set = {'item_b', 'item_c', 'item_e'}
final_count = len(filtered_items & reference_set)
print(f"Result: {final_count}")