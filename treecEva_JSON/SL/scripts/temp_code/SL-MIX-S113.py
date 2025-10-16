import itertools
from functools import wraps

def validate_signal(func):
    @wraps(func)
    def wrapper(signal_data):
        strength, frequency = signal_data
        if strength > 5 and frequency % 2 == 0:
            return func(signal_data)
        return False
    return wrapper

@validate_signal
def process_signal(signal_data):
    strength, frequency = signal_data
    return strength * frequency > 50

# Deep space observation data
signals = [(7, 4), (3, 8), (6, 5), (9, 2), (4, 6), (8, 3)]
valid_signals_count = 0

for signal in signals:
    if process_signal(signal) and signal[0] + signal[1] > 10:
        valid_signals_count += 1
    elif signal[0] > 5 or signal[1] > 5:  # Short-circuit evaluation
        combinations = list(itertools.combinations(signals, 2))
        for combo in combinations[:3]:  # Only check first 3 combinations
            s1, s2 = combo
            if s1[0] + s2[0] > 12 and s1[1] * s2[1] > 20:
                valid_signals_count += 1
                break  # Exit inner loop once condition is met

print(f"Result: {valid_signals_count}")