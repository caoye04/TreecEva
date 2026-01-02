def calculate_lab_capacity():
    lab_sections = [32, 45, 27, 50, 33]
    maintenance_rooms = {45, 50}
    expansion_planned = [33, 32]

    total_capacity = sum(lab_sections)
    reserved_capacity = 0
    
    for section in lab_sections:
        if section in maintenance_rooms:
            reserved_capacity += section

    available_spaces = set(lab_sections)
    allocated_spaces = {section for section in lab_sections if section > 40}
    allocated_spaces.add(27)
    
    temp_buffer = [x * 2 for x in expansion_planned]  # Irrelevant computation
    buffer_sum = sum(temp_buffer)  # Distractor variable

    final_capacity = max(available_spaces.difference(allocated_spaces))
    return final_capacity

result = calculate_lab_capacity()
print(f"Target result: {result}")