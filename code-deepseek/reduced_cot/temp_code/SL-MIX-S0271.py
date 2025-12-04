names_list = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
target_name = 'diana'
base_offset = 2
name_length = len(target_name)
offset_calc = base_offset * name_length
sorted_names = sorted(names_list)
final_index = sorted_names.index(target_name) + offset_calc
print(f"Result: {final_index}")