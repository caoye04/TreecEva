def analyze_sensor_overlap():
    sensor_a_readings = {x for x in range(10, 101, 5)}
    sensor_b_readings = {x for x in range(25, 150, 7)}
    sensor_c_readings = {x for x in range(40, 200, 9)}

    valid_range = set(range(30, 120))

    filtered_a = sensor_a_readings & valid_range
    filtered_b = sensor_b_readings & valid_range
    filtered_c = sensor_c_readings & valid_range

    common_elements = filtered_a & filtered_b & filtered_c

    temp_counter = 0
    for val in filtered_a:
        if val % 4 == 0:
            temp_counter += 1

    overlap_sum = sum(common_elements)

    extra_calc = len(filtered_a) + len(filtered_b)
    dummy_result = [i for i in enumerate(range(5))]

    return overlap_sum

result = analyze_sensor_overlap()
print(f"Result: {result}")