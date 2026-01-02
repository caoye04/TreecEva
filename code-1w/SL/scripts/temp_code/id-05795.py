def process_data(entries):
    sum_values = 0
    flags = []
    
    for i, entry in enumerate(entries):
        if isinstance(entry, str) and entry.isnumeric():
            numeric_value = int(entry)
            sum_values += numeric_value
            parity_flag = (numeric_value ^ i) & 1
            flags.append(parity_flag)
    
    def finalize(total, flag_list):
        result = total
        for idx, flag in enumerate(flag_list):
            if flag:
                result += idx * 2
        return result | 1  # Ensure odd final value
    
    checksum = finalize(sum_values, flags)
    return checksum

# Simulated sensor readings with mixed data types
data_stream = ['23', 'invalid', '45', '76', 'error', '12']
result = process_data(data_stream)
print(f"Result: {result}")