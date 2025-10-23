from collections import Counter

def transform_symbol(symbol_code, depth=3):
    if depth == 0:
        return symbol_code
    # Recursive backtracking with modular arithmetic
    next_code = (symbol_code * 3 + 7) % 31
    return transform_symbol(next_code, depth - 1) ^ (symbol_code << 1)

def process_symbols(symbol_sequence):
    # Initialize frequency counter
    freq_counter = Counter(symbol_sequence)
    
    # Symbol to 5-bit code mapping
    symbol_map = {'A': 0b10011, 'B': 0b01100, 'C': 0b11010}
    
    # Process each unique symbol
    encoded_values = []
    for symbol, count in freq_counter.items():
        base_code = symbol_map[symbol]
        # Apply transformation based on frequency
        transformed = transform_symbol(base_code) & 0b11111
        # Combine with frequency using XOR
        encoded_value = transformed ^ (count << 2)
        encoded_values.append(encoded_value)
    
    # Calculate final signal strength using XOR reduction
    encoded_signal_strength = 0
    for val in encoded_values:
        encoded_signal_strength ^= val
    
    return encoded_signal_strength

# Process the given symbol sequence
symbol_sequence = ['A', 'B', 'C', 'A', 'B', 'A']
encoded_signal_strength = process_symbols(symbol_sequence)
print(f'Result: {encoded_signal_strength}')