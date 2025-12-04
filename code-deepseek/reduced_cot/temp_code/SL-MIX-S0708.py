def transform_coordinates(x_values, y_values):
    coordinate_shift = 15
    irrelevant_offset = 42
    temp_x = [x + coordinate_shift for x in x_values]
    temp_y = [y * 2 - coordinate_shift for y in y_values]
    dead_code_result = irrelevant_offset * 3 - 100
    return [temp_x[i] * temp_y[i] for i in range(len(temp_x))]

def compute_final_value(transformed_data, threshold_dict):
    base_multiplier = 7
    distraction_factor = 3.14
    irrelevant_sum = sum(threshold_dict.values()) * distraction_factor
    
    relevant_data = [x for x in transformed_data if x > threshold_dict['critical']]
    if not relevant_data:
        fallback_calc = (threshold_dict['warning'] << 2) + base_multiplier
        return fallback_calc
    
    intermediate = (sum(relevant_data) // len(relevant_data)) if len(relevant_data) > 1 else relevant_data[0]
    final_adjustment = intermediate - threshold_dict['warning'] if intermediate > threshold_dict['warning'] else intermediate + threshold_dict['critical']
    
    return final_adjustment * base_multiplier

x_points = [3, 7, 11]
y_points = [5, 9, 2]
threshold_map = {'critical': 50, 'warning': 30, 'irrelevant': 100}
distraction_var = 25
misleading_intermediate = distraction_var * 4 - 10
final_result = compute_final_value(transform_coordinates(x_points, y_points), threshold_map)
print(f"Result: {final_result}")