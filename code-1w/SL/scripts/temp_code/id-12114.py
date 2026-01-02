import itertools

# Simulated sensor readings with noise and metadata
temperature_reads = [23.5, 24.1, 25.0, 22.8, 26.3, 25.9, 24.7]
humidity_reads = [45, 47, 50, 44, 55, 53, 49]
pressure_reads = [1013, 1012, 1015, 1010, 1008, 1009, 1011]

# Irrelevant transformation: normalize unrelated metric
def normalize(val_list):
    min_val, max_val = min(val_list), max(val_list)
    return [(v - min_val) / (max_val - min_val) for v in val_lists]

# Dead function: never called but looks important
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    return -sum((count/total) * log(count/total) for count in freq.values())

# Distractor: complex-looking but unused filter
class DataFilter:
    def __init__(self, threshold):
        self.threshold = threshold
        self.cache = []

    def apply(self, x):
        return x > self.threshold

# Misleading intermediate calculations
deviation_scores = []
for i in range(len(temperature_reads)):
    dev = abs(temperature_reads[i] - sum(temperature_reads)/len(temperature_reads))
    deviation_scores.append(round(dev * 100))

# Unused smoothing operation
smoothed = list(itertools.starmap(lambda x, y: (x + y) / 2, zip(temperature_reads[:-1], temperature_reads[1:])))

# Real processing begins: group every two readings
paired_data = []
for i in range(0, len(temperature_reads) - 1, 2):
    paired_data.append((temperature_reads[i], humidity_reads[i], pressure_reads[i]))

# Bit manipulation red herring
def scramble(value, key=7):
    return (value ^ key) << 1

# Actual aggregation logic (buried among distractions)
aggregated = 0
for idx, (temp, hum, pres) in enumerate(paired_data):
    # Only use temperature and pressure; humidity is a distractor
    if idx % 2 == 0:
        contribution = (temp * 10) + (pres % 100)
        aggregated += int(contribution)
    else:
        contribution = temp + (pres // 100)
        aggregated -= int(contribution)

# Decoy checksum function (never used)
def quick_checksum(data):
    return sum(data) % 1000

# Finalization with conditional logic
mode_flags = {'strict': True, 'loose': False}

def finalize_result(value, mode="loose"):
    result = value
    if mode_flags[mode]:
        result = (result ^ 0xAA) + 33
        result = (result * 2) - (result // 10)  # Complex adjustment
    return abs(result)

# Critical execution point
calibration_offset = sum(deviation_scores[:3])  # Red herring
reference_key = scramble(calibration_offset)      # More distraction
temp_buffer = list(zip(smoothed, deviation_scores))  # Unused structure

# Key statement
checksum = finalize_result(aggregated, mode="strict")

# Output required format
print(f"Result: {checksum}")