def analyze_overlap():
    sensors_a = {101, 102, 103, 104, 105}
    sensors_b = {103, 104, 105, 106, 107}
    sensors_c = {105, 106, 107, 108}

    # Find sensors that are active in both A and B
    shared_ab = sensors_a.intersection(sensors_b)

    # Ignore isolated maintenance log (minimal interference)
    maintenance_log = [102, 108]

    # Find overlap between AB and C
    common_items = shared_ab.intersection(sensors_c)

    result = len(common_items)
    print(f"Result: {result}")

analyze_overlap()