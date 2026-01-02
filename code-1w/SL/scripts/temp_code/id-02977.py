def analyze_data_stream():
    # Simulated sensor readings and metadata
    raw_readings = [107, 214, 198, 235, 189, 203, 176, 241, 167, 228]
    timestamps = [1623456780 + i*30 for i in range(10)]
    statuses = ['OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK', 'OK', 'ERROR', 'OK', 'WARNING']

    # Irrelevant transformations (distractors)
    squared_offsets = [t % 100 for t in timestamps]
    offset_map = {i: sq for i, sq in enumerate(squared_offsets)}
    cumulative_noise = 0
    for idx in range(len(timestamps)):
        if statuses[idx] == 'ERROR':
            cumulative_noise += raw_readings[idx] % 17
    noise_floor = cumulative_noise / 2 if cumulative_noise > 0 else 0.5

    # Core processing with mixed paradigms
    threshold = 200
    high_readings = [x for x in raw_readings if x > threshold]  # list comprehension

    # Bit manipulation on selected elements
    processed_values = []
    for val in high_readings:
        shifted = (val ^ 0b110011) >> 2  # XOR and right shift
        processed_values.append(shifted)

    # Multiple assignments and tuple unpacking (distractor)
    a, b = 12, 15
    a, b = b, a + 1  # swapping and update

    # Generate all pairwise products
    all_pairs = [(i, j) for i in processed_values for j in processed_values]
    product_dict = {}  # dictionary operation
    for i, j in all_pairs:
        product_dict[(i, j)] = i * j

    # Extract products above threshold and not self-multiplied
    relevant_products = []
    for (i, j), prod in product_dict.items():
        if i != j and prod > 5000:
            relevant_products.append(prod)

    # Decoy loop with no effect on final result
    temp_results = []
    for _ in range(3):
        temp = [p // 3 for p in relevant_products if p % 3 == 0]
        temp_results.extend(temp)

    filtered_sum = sum(relevant_products)

    # Unused complex data structure (red herring)
    class DataNode:
        def __init__(self, value):
            self.value = value
            self.children = []

    root = DataNode(1)
    for val in raw_readings[:3]:
        root.children.append(DataNode(val))

    # Final output
    print(f"Result: {filtered_sum}")

analyze_data_stream()