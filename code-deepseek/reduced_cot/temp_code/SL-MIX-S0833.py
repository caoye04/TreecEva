def calculate_discount(base_price, quantity):
    temp_multiplier = (base_price << 1) - (base_price // 2)
    irrelevant_calc = temp_multiplier * 3.14159
    
    discount_rate = 0.15 if quantity >= 5 else 0.05
    misleading_total = base_price * quantity * (1 - discount_rate + 0.02)
    
    if quantity > 10:
        bonus = base_price * 0.1
        dead_code = bonus * 2.5
    else:
        bonus = 0
    
    actual_discount = discount_rate - 0.02
    final_price = (base_price * quantity * (1 - actual_discount)) + bonus
    return final_price

def process_transaction(item_list):
    price_map = {'A': 25, 'B': 40, 'C': 15, 'D': 60}
    irrelevant_counter = len(item_list) * 2 - 1
    
    total_items = sum(item_list.count(item) for item in price_map)
    misleading_sum = sum(price_map.values()) * irrelevant_counter
    
    if total_items == 0:
        return 0
    
    category_total = 0
    for item in item_list:
        if item in price_map:
            item_count = lambda x: sum(1 for i in item_list if i == x)
            count = item_count(item)
            category_total += calculate_discount(price_map[item], count)
        else:
            dead_path = price_map.get('Z', 100) * 1.5
    
    redundant_check = (category_total > 1000) and (total_items < 20)
    final_output = category_total * (0.95 if redundant_check else 1.0)
    
    return final_output

items = ['A', 'B', 'A', 'C', 'B', 'A', 'D']
result = process_transaction(items)
print(f"Result: {result}")