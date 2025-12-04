def process_data(text):
    # Process text data to count valid entries
    temp_list = text.split(',')
    processed = [item.strip().upper() for item in temp_list]
    
    # Some intermediate processing (distractor)
    char_counts = [len(item) for item in processed]
    total_chars = sum(char_counts)
    
    # Actual filtering logic using lambda and conditional
    filter_func = lambda x: len(x) > 3 and x.startswith('ITEM')
    valid_items = list(filter(filter_func, processed))
    
    # More intermediate calculations (distractor)
    max_length = max(len(item) for item in processed) if processed else 0
    
    return len(valid_items)

data_string = "item1, ITEM_A, item_b, ITEM_DATA, test, ITEM_INFO, ITEM_123"
final_count = process_data(data_string)
print(f"Result: {final_count}")