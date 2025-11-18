from functools import reduce
from math import cos, radians

def base7_to_base10(s):
    return int(s, 7)

def signal_transform(x):
    return round(cos(radians(x)) * 100)

stellar_codes = ['123', '214', '156', '320', '245']
processed_signals = list(map(signal_transform, map(base7_to_base10, stellar_codes)))
valid_signals = [s for s in processed_signals if 20 <= s <= 80]
cosmic_checksum = reduce(lambda a, b: a * b, valid_signals, 1)
print(f"Result: {cosmic_checksum}")