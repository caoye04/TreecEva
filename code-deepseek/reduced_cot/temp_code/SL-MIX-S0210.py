from collections import defaultdict

def process_inventory_data():
    inventory_items = ['widget_a', 'widget_b', 'widget_c', 'widget_a', 'widget_b', 'widget_a']
    price_mapping = {'widget_a': 25, 'widget_b': 40, 'widget_c': 60}
    
    item_counts = defaultdict(int)
    for item in inventory_items:
        item_counts[item] += 1
    
    total_revenue = 0
    temp_calculation = 0
    for item, count in item_counts.items():
        total_revenue += price_mapping[item] * count
        temp_calculation += count ** 2
    
    key_modifier = len(inventory_items) % 4
    processed_key = f'rev_mod_{key_modifier}'
    
    result_mapping = {
        'rev_mod_0': total_revenue // 2,
        'rev_mod_1': total_revenue - 50,
        'rev_mod_2': total_revenue * 0.75,
        'rev_mod_3': total_revenue + 25
    }
    
    intermediate_value = temp_calculation - 10
    fallback_value = total_revenue // 3
    
    final_result = result_mapping.get(processed_key, fallback_value)
    print(f"Result: {final_result}")
    return final_result

process_inventory_data()