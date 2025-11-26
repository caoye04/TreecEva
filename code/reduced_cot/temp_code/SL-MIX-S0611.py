def analyze_inventory_similarity(items_a, items_b):
    item_frequency_a = {}
    item_frequency_b = {}
    
    for idx, item in enumerate(items_a):
        item_frequency_a[item] = item_frequency_a.get(item, 0) + (idx % 2 + 1)
    
    for idx, item in enumerate(items_b):
        item_frequency_b[item] = item_frequency_b.get(item, 0) + (idx // 2 + 1)
    
    potential_pairs = 0
    for item_a, freq_a in item_frequency_a.items():
        for item_b, freq_b in item_frequency_b.items():
            if item_a == item_b:
                potential_pairs += freq_a * freq_b
    
    matching_items = []
    for item_a, item_b in zip(items_a, items_b):
        if item_a == item_b:
            matching_items.append((item_a, item_b))
    
    valid_pairs_count = 0
    for match in matching_items:
        if match[0] in item_frequency_a and match[1] in item_frequency_b:
            valid_pairs_count += item_frequency_a[match[0]] + item_frequency_b[match[1]]
    
    redundant_matches = len(matching_items) * 2
    offset_calculation = (len(items_a) + len(items_b)) // 3
    final_count = valid_pairs_count - redundant_matches
    
    print(f"Result: {final_count}")

inventory_alpha = ['widget', 'gadget', 'widget', 'device', 'tool']
inventory_beta = ['gadget', 'widget', 'device', 'widget', 'part']
analyze_inventory_similarity(inventory_alpha, inventory_beta)