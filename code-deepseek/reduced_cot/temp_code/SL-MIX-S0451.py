data_a = {2, 5, 8, 11, 14}
data_b = {5, 11, 17, 23, 29}
preliminary_check = len(data_a) + len(data_b)
final_result = len((data_a.union(data_b) - data_a.intersection(data_b)))
print(f"Result: {final_result}")