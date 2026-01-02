def compute_integrity_score(input_str):
    data_length = len(input_str)
    reversed_str = input_str[::-1]
    uppercase_count = sum(1 for c in input_str if c.isupper())
    lowercase_count = sum(1 for c in input_str if c.islower())
    
    # Dummy variables for slight interference (LOW level)
    placeholder = data_length * 2  # not used in final calculation
    temp_flag = lowercase_count > uppercase_count
    
    pivot = data_length % 7
    offset = input_str.count('e') * 3
    checksum = (data_length ^ pivot) + offset
    
    return checksum

result = compute_integrity_score('QuantumEntanglement')
print(f"Result: {result}")