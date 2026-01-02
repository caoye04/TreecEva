def analyze_text_compression(text_blocks):
    total_chars = sum(len(block) for block in text_blocks)
    all_chars = ''.join(text_blocks)
    char_frequency = {char: all_chars.count(char) for char in set(all_chars)}
    unique_chars = len(char_frequency)
    avg_frequency = total_chars / unique_chars if unique_chars else 0
    compression_ratio = total_chars / unique_chars if unique_chars else 0
    return compression_ratio

# Simulated log data from system diagnostics
text_data = [
    "ERROR: Disk failure detected",
    "WARNING: High memory usage",
    "INFO: System reboot initiated",
    "DEBUG: Fan speed increased"
]

result = analyze_text_compression(text_data)
print(f"Result: {result}")