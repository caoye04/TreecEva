def analyze_data_compression(text):
    original_data = text
    char_frequency = {char: text.count(char) for char in set(text)}
    unique_chars = len(char_frequency)
    threshold = 2
    frequent_chars = [ch for ch, freq in char_frequency.items() if freq > threshold]
    compressed_data = ''.join(frequent_chars) or 'NO_COMPRESSION'
    compression_ratio = len(original_data) / len(compressed_data)
    return compression_ratio

result = analyze_data_compression('abccddaaefgghh')
print(f"Result: {result}")