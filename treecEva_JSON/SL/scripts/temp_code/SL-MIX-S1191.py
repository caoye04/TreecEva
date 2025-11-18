def process_transactions():
    transaction_ids = ['TXN001A', 'TXN002B', 'TXN003C', 'TXN004D']
    weights = {char: idx+1 for idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    adjustments = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    
    def calculate_code_value(code):
        numeric_part = int(code[3:6])
        letter_part = code[6]
        base_value = numeric_part * weights[letter_part]
        adjusted_value = base_value + adjustments.get(letter_part, 0)
        return adjusted_value
    
    checksum_components = []
    for tid in transaction_ids:
        value = calculate_code_value(tid)
        if value % 2 == 0:
            value = value >> 1  # Right shift by 1 (equivalent to dividing by 2)
        else:
            value = value << 1  # Left shift by 1 (equivalent to multiplying by 2)
        checksum_components.append(value)
    
    # Compute final checksum using XOR
    final_checksum = 0
    for component in checksum_components:
        final_checksum ^= component
    
    return final_checksum

result = process_transactions()
print(f"Result: {result}")