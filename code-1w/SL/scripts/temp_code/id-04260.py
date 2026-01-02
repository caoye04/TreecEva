def preprocess_metrics(raw_data, window_size=3):
    smoothed = []
    for i in range(len(raw_data) - window_size + 1):
        window = raw_data[i:i+window_size]
        smoothed.append(sum(window) / window_size)
    return [x for x in smoothed if x > 0.5]

# Irrelevant signal processing function (decoy)
def compute_fourier_components(signal):
    result = 0
    for i in range(len(signal)):
        result += signal[i] * (i % 7)
    return result % 100

# Unused helper (dead code path)
def validate_checksum(data_block):
    total = 0
    for b in data_block:
        total ^= b
    return total == 0xFF

# Complex state tracker with distractors
class SystemStateTracker:
    def __init__(self):
        self.history = []
        self.alert_level = 0
        self.suppressed_events = 0  # Distractor

    def update(self, value):
        self.history.append(value)
        if value > 80:
            self.alert_level += 1
        elif value < 10:
            self.suppressed_events += 1  # Never used

    def get_trend(self):
        if len(self.history) < 2:
            return 0
        return self.history[-1] - self.history[0]

# Main analysis function
def analyze_system_state(signature, log_entries):
    tracker = SystemStateTracker()
    
    # Bit manipulation block (partially relevant)
    bit_analysis = 0
    for val in signature:
        bit_analysis ^= (val * 3) & 0xFF
        bit_analysis = (bit_analysis << 1) | (bit_analysis >> 7)
        bit_analysis &= 0xFF
    
    # Dictionary-based frequency counting (core concept)
    event_freq = {}
    for entry in log_entries:
        category = entry % 5
        event_freq[category] = event_freq.get(category, 0) + 1
    
    # Simulate decoy statistical analysis
    mean_val = sum(log_entries) / len(log_entries) if log_entries else 0
    variance_proxy = sum(abs(x - mean_val) for x in log_entries) / len(log_entries) if log_entries else 0
    
    # Inject irrelevant sorting operation
    sorted_entries = sorted(log_entries, reverse=True)
    mid_point = len(sorted_entries) // 2
    # Use only one element from sorted list (minimal relevance)
    pivot_contribution = sorted_entries[mid_point] if mid_point % 2 == 0 else 0
    
    # Process entries through tracker (relevant)
    for val in log_entries:
        tracker.update(val % 100)
    
    # Character counting analog (modular arithmetic as character proxy)
    char_code_sum = 0
    for num in signature:
        char_code_sum += (num % 26) + ord('A')
    
    # Multiple red herrings and intermediate values
    decoy_result = (variance_proxy * 1000) % 777
    false_indicator = compute_fourier_components([1, 2, 3, 4, 5])
    unused_diagnostic = preprocess_metrics([0.1, 0.8, 0.3, 0.9, 0.2])
    
    # Core logic chain with dependencies
    base_score = tracker.get_trend()
    freq_bonus = 0
    for k, v in event_freq.items():
        if v > 2:
            freq_bonus += k * v
    
    # Final computation - depends on multiple paths
    final_diagnostic = (base_score * 17) \
                     + (freq_bonus * 3) \
                     + (bit_analysis % 23) \
                     + pivot_contribution \
                     - (char_code_sum // 1000)
    
    # Critical execution point
    final_diagnostic = analyze_system_state(quantum_signature, system_log)
    
    return int(final_diagnostic)

# Input data setup
quantum_signature = [42, 17, 255, 89, 12, 203]
system_log = [85, 12, 93, 8, 44, 77, 15, 93, 52, 8, 85]

# Execute and print result
target_variable = analyze_system_state(quantum_signature, system_log)
print(f"Result: {target_variable}")