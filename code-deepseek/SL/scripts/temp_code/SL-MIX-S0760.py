def process_data(records, condition):
    filtered_records = {}
    temp_calculations = []
    
    for emp_id, emp_data in records.items():
        if condition(emp_data['performance']):
            filtered_records[emp_id] = emp_data
            # Distractor calculation - not used in final result
            bonus_estimate = emp_data['hours'] * 15.5
            temp_calculations.append(bonus_estimate)
    
    # Relevant processing
    total_hours = 0
    valid_count = 0
    
    for emp_id, emp_data in filtered_records.items():
        if emp_data['department'] == 'Engineering':
            total_hours += emp_data['hours']
            valid_count += 1
    
    # Semi-relevant intermediate step
    avg_hours = total_hours / valid_count if valid_count > 0 else 0
    
    # Final calculation
    efficiency_score = (total_hours * 0.85) + (valid_count * 25)
    
    # Distractor operation - doesn't affect final result
    unused_metric = len(temp_calculations) * 3.14
    
    return efficiency_score

def filter_condition(performance):
    return performance >= 75

employee_records = {
    'E001': {'name': 'Alice', 'department': 'Engineering', 'hours': 160, 'performance': 82},
    'E002': {'name': 'Bob', 'department': 'Marketing', 'hours': 140, 'performance': 78},
    'E003': {'name': 'Charlie', 'department': 'Engineering', 'hours': 175, 'performance': 91},
    'E004': {'name': 'Diana', 'department': 'Engineering', 'hours': 152, 'performance': 68},
    'E005': {'name': 'Eve', 'department': 'Engineering', 'hours': 168, 'performance': 87}
}

final_calculation = process_data(employee_records, filter_condition)
result_value = int(final_calculation)
print(f"Result: {result_value}")