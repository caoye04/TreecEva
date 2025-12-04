def data_validator(items, keys):
    # Irrelevant helper function that distracts from main logic
    def fake_processor(x):
        return (x * 3 + 7) % 11
    
    # Misleading intermediate computations
    temp_sum = 0
    for i in range(len(items)):
        temp_sum += items[i] * (i + 1)
    
    # Dead code path that never executes
    if temp_sum > 1000:
        unused_result = temp_sum // 2
    else:
        unused_result = temp_sum * 2
    
    # Main logic using zip and enumerate
    validation_sum = 0
    for idx, (item, key) in enumerate(zip(items, keys)):
        # Distracting computation
        fake_check = (item ^ key) & 0xFF
        
        # Actual validation logic
        if item % 2 == 0:
            validation_sum += item + key
        else:
            validation_sum += item - key
        
        # More irrelevant operations
        distraction = fake_processor(idx)
    
    # Final computation with misleading variable
    intermediate = validation_sum % 50
    checksum = intermediate * 3 - 7
    
    return checksum

data_items = [12, 8, 15, 23, 6]
verification_keys = [3, 5, 2, 7, 4]

# Irrelevant parallel computation
distraction_list = [x * 2 for x in data_items]
fake_total = sum(distraction_list)

final_checksum = data_validator(data_items, verification_keys)
print(f"Result: {final_checksum}")