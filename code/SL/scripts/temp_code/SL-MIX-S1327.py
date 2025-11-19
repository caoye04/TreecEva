from functools import reduce
from collections import namedtuple

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def is_valid_color(rgb_tuple):
    return all(0 <= c <= 255 for c in rgb_tuple)

def calculate_luminance(rgb_tuple):
    return sum(c * w for c, w in zip(rgb_tuple, [0.299, 0.587, 0.114]))

class TextileProcessor:
    def __init__(self):
        self.quality_score = 0
        self.batch_weights = [1.0, 1.2, 0.8]
    
    def process_batch(self, hex_patterns, batch_index):
        ColorSegment = namedtuple('ColorSegment', ['hex_code', 'rgb', 'luminance'])
        segments = []
        
        # Tokenize and parse patterns
        for pattern in hex_patterns:
            tokens = [pattern[i:i+6] for i in range(0, len(pattern), 6)]
            for token in tokens:
                if len(token) == 6:
                    try:
                        rgb_val = hex_to_rgb(token)
                        if is_valid_color(rgb_val):
                            lum = calculate_luminance(rgb_val)
                            segments.append(ColorSegment(token, rgb_val, lum))
                    except ValueError:
                        pass
        
        # State machine for quality assessment
        state = 'INIT'
        batch_quality = 0
        
        for segment in segments:
            if state == 'INIT':
                if segment.luminance > 100:
                    state = 'BRIGHT_COLOR'
                    batch_quality += segment.luminance * 1.5
                else:
                    state = 'DIM_COLOR'
                    batch_quality += segment.luminance * 0.8
            elif state == 'BRIGHT_COLOR':
                if segment.luminance < 50:
                    state = 'TRANSITION'
                    batch_quality += segment.luminance * 2.0
                else:
                    batch_quality += segment.luminance * 1.1
            elif state == 'DIM_COLOR':
                if segment.luminance > 150:
                    state = 'BRIGHT_COLOR'
                    batch_quality += segment.luminance * 1.7
                else:
                    batch_quality += segment.luminance * 0.9
            elif state == 'TRANSITION':
                batch_quality += segment.luminance
                state = 'INIT'
        
        self.quality_score += batch_quality * self.batch_weights[batch_index]

# Main processing
processor = TextileProcessor()

batch1 = ['#FF5733CCF5D6', '#1A2B3C4D5E6F']
batch2 = ['#ABCDEF000000', '#FFFFFF123456']
batch3 = ['#7890ABCD34EF', '#000000CCCCCC']

processor.process_batch(batch1, 0)
processor.process_batch(batch2, 1)
processor.process_batch(batch3, 2)

print(f"Result: {int(processor.quality_score)}")