temperature_data = [23, 19, 17, 21, 26, 29, 18]
humidity_level = 75
scaling_factor = 3
offset = 5  # Irrelevant variable for minor distraction
days_of_week = ['Mon', 'Tue', 'Wed']  # Unused list

# Extract subset, reverse it, take first element, scale and add conditional bonus
temp_slice = temperature_data[2:5]  # [17, 21, 26]
reversed_slice = temp_slice[::-1]  # [26, 21, 17]
base_value = reversed_slice[0]  # 26
bonus = 10 if humidity_level > 70 else 0  # 10
result = base_value * scaling_factor + bonus

print(f"Result: {result}")