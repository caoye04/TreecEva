from collections import defaultdict
from functools import reduce
import operator

def signal_transform(func):
    def wrapper(segment):
        transformed = func(segment)
        return [x if x > 0 else 0 for x in transformed]
    return wrapper

@signal_transform
def amplify_signal(segment):
    return [x * 3 - 2 for x in segment]

space_data_segments = [
    [2, -1, 4, 0, 3],
    [-2, 5, 1, -3, 2],
    [0, 3, -2, 4, 1],
    [1, -1, 2, -2, 3]
]

valid_segment_count = 0
segment_scores = defaultdict(int)

for idx, segment in enumerate(space_data_segments):
    if any(x > 0 for x in segment) and not all(x <= 0 for x in segment):
        valid_segment_count += 1
        processed_segment = amplify_signal(segment)
        positive_values = list(filter(lambda x: x > 0, processed_segment))
        
        if positive_values:
            segment_energy = reduce(operator.add, positive_values, 0)
            segment_scores[idx] = segment_energy

extraterrestrial_score = 0
if valid_segment_count >= 2:
    for i in range(valid_segment_count):
        for j in range(i+1, valid_segment_count):
            if segment_scores[i] > 0 and segment_scores[j] > 0:
                extraterrestrial_score += segment_scores[i] & segment_scores[j]

print(f"Result: {extraterrestrial_score}")