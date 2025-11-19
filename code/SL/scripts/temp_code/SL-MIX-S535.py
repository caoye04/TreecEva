from collections import namedtuple

def tokenize_and_process(signal_data):
    Token = namedtuple('Token', ['frequency', 'amplitude'])
    tokens = [Token(int(x), int(y)) for x, y in zip(signal_data[::2], signal_data[1::2])]
    
    def band_transform(token):
        return (token.frequency << 2) ^ (token.amplitude & 0xF)
    
    processed_bands = list(map(band_transform, tokens))
    return processed_bands

def aggregate_signal(bands):
    aggregate = 0
    for i, band in enumerate(bands):
        if i % 2 == 0:
            aggregate += band
        else:
            aggregate ^= band
    return aggregate

# Main processing pipeline
raw_signal = ['3', '5', '7', '2', '11', '1']
frequency_bands = tokenize_and_process(raw_signal)
processed_signal = aggregate_signal(frequency_bands)
print(f'Result: {processed_signal}')