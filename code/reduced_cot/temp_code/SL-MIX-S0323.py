def process_data_sets():
    primary_data = {1, 3, 5, 7, 9, 11, 13}
    secondary_data = {2, 3, 5, 7, 11, 13, 17}
    
    # Main computation
    union_set = primary_data | secondary_data
    intersection_set = primary_data & secondary_data
    
    # Distraction operations (intervention level 7)
    temp_sum = sum(primary_data) + sum(secondary_data)
    unused_difference = len(primary_data) - len(secondary_data)
    dummy_ratio = temp_sum / (len(union_set) + 1)
    
    # Filter relevant intersection
    valid_intersection = len([x for x in intersection_set if x % 2 != 0])
    union_size = len(union_set)
    
    # Intermediate distraction
    potential_max = max(union_set) + min(secondary_data)
    
    final_output = union_size - valid_intersection
    print(f"Result: {final_output}")
    return final_output

process_data_sets()