from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic logic
def collect_readings():
    raw_samples = [18, 23, 17, 45, 22, 38, 41, 16, 27, 33]
    offset_map = defaultdict(int)
    for idx, val in enumerate(raw_samples):
        offset_map[val % 7] += idx
    
    # Irrelevant transformation (distractor)
    temp_analysis = [math.log(x) * 1.5 for x in raw_samples if x > 20]
    normalization_factor = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 1
    
    # Core relevant computation path
    filtered = [x for x in raw_samples if x % 2 == 1]
    entropy_buffer = []
    for num in filtered:
        bit_entropy = bin(num).count('1')
        if bit_entropy >= 3:
            entropy_buffer.append(num)
    
    return entropy_buffer

# Decoy function - looks important but unused
def compute_variance(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(squared_diffs)

# Another red herring: complex but irrelevant structure
class DataObfuscator:
    def __init__(self, size):
        self.buffer = [0] * size
        self.checksum = 0
    
    def scramble(self, values):
        for v in values:
            self.checksum ^= (v * 17) % 251
        return self.checksum

# Real analysis function (key logic)
def analyze_pattern(signal):
    if not signal:
        return -1
    
    # Set operations as required feature
    unique_signal = set(signal)
    duplicates_exist = len(signal) != len(unique_signal)
    
    # Actual answer derivation
    base_score = 0
    for val in signal:
        if val > 30:
            base_score += val // 3
        else:
            base_score += val % 19
    
    # Secondary manipulation (relevant)
    adjustment = len(unique_signal) * 2
    if duplicates_exist:
        adjustment -= 5
    
    # Dead code path (misleading)
    final_power = 0
    for _ in range(3):
        final_power += 2 ** _  # never used
    
    # Final computation
    result = base_score * adjustment
    
    # More distractors
    stats = Counter(signal)
    mode_val = max(stats, key=stats.get) if stats else 0
    outlier_count = sum(1 for x in signal if x < 20)
    
    # Key result computed here
    final_diagnostic = result + mode_val - outlier_count
    
    # Debug prints that don't affect logic (distraction)
    # print(f'Debug: mode={mode_val}, outliers={outlier_count}')
    # print(f'Power trace: {final_power}')
    
    return final_diagnostic

# Orchestration with misleading setup
def main():
    # Unused variables and irrelevant initializations
    system_status = {'active': True, 'level': 7, 'flags': [0, 0, 1]}
    audit_trail = []
    
    # Real data flow
    entropy_buffer = collect_readings()  # returns [23, 45, 17, 33, 41, 27]
    
    # Fake processing chain
    obfuscator = DataObfuscator(10)
    fake_result = obfuscator.scramble([1, 1, 2, 3, 5, 8])  # Fibonacci distraction
    
    # Critical statement
    final_diagnostic = analyze_pattern(entropy_buffer)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()