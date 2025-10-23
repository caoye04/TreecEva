from itertools import permutations, combinations
from functools import reduce

def signal_transformer(signal):
    return ''.join(chr((ord(c) - 65 + 3) % 26 + 65) if 'A' <= c <= 'Z' else c for c in signal)

def signal_evaluator(signals):
    transformed_signals = [signal_transformer(s) for s in signals]
    pattern_score = 0
    
    for perm in permutations(transformed_signals, 2):
        if perm[0][:2] == perm[1][-2:]:
            pattern_score += 1
    
    return pattern_score

cosmic_bursts = ['ALPHA', 'BETA', 'GAMMA', 'DELTA']
cosmic_combinations = list(combinations(cosmic_bursts, 3))
transformed_combinations = []

for combo in cosmic_combinations:
    temp_list = []
    for signal in combo:
        transformed_signal = ''.join(chr((ord(c) - 65 + 5) % 26 + 65) for c in signal)
        temp_list.append(transformed_signal)
    transformed_combinations.append(temp_list)

scores = list(map(signal_evaluator, transformed_combinations))
cosmic_signature = reduce(lambda x, y: x ^ y, scores, 0)

match cosmic_signature % 4:
    case 0:
        cosmic_signature += 10
    case 1:
        cosmic_signature *= 2
    case 2:
        cosmic_signature -= 5
    case 3:
        cosmic_signature = cosmic_signature ** 2

print(f"Result: {cosmic_signature}")