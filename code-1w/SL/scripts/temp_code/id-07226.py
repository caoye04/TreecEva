def analyze_stock():
    raw_data = 'AAABBBCCCCDDDEEEFFFGGGHHHIIIJJJKKK'
    segment_a = raw_data[3:15]
    segment_b = raw_data[10:20]
    
    # Count occurrences of specific items
    item_c_count = segment_a.count('C')
    item_d_count = segment_b.count('D')
    item_e_count = segment_b.count('E')
    
    base_count = item_c_count * 2 + item_d_count * 3
    extra_offset = len(segment_a) - len(segment_b)
    adjusted_count = base_count + extra_offset
    
    # Simulate unpacking of shipment batch
    batch_info = (17, 9)
    received_units, damage_units = batch_info
    
    final_count = adjusted_count + received_units
    reserved_units = item_e_count * 4 + damage_units
    inventory_balance = final_count - reserved_units
    
    # Irrelevant metric (distractor)
    avg_length = (len(segment_a) + len(segment_b)) / 2
    
    return inventory_balance

result = analyze_stock()
print(f"Target result: {result}")