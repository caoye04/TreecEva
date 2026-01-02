import math

# System configuration parameters (some are red herrings)
MAX_BUFFER_SIZE = 1024
timeout_delay = 0.25
retry_attempts = 3
DEBUG_MODE = False

# Network node simulation with mixed signal processing
network_nodes = [
    {'id': 'A1', 'signal': 144, 'active': True, 'mode': 'PRIME'},
    {'id': 'B2', 'signal': 25, 'active': False, 'mode': 'EVEN'},
    {'id': 'C3', 'signal': 64, 'active': True, 'mode': 'SQUARE'},
    {'id': 'D4', 'signal': 49, 'active': True, 'mode': 'PRIME'},
    {'id': 'E5', 'signal': 169, 'active': False, 'mode': 'SQUARE'}
]

# Irrelevant utility function (decoy)
def validate_checksum(data):
    return sum(len(str(x)) for x in data) % 7 == 0

# Misleading transformation chain
class SignalProcessor:
    def __init__(self, base_factor):
        self.base_factor = base_factor
        self.history = []

    def transform(self, val):
        temp = int(math.sqrt(val) * self.base_factor)
        self.history.append(temp)
        return temp + 1 if temp % 2 == 0 else temp

processor = SignalProcessor(3)

# Distractor: Unused but plausible signal analysis
potential_signals = [n['signal'] for n in network_nodes if n['mode'] == 'PRIME']
avg_potential = sum(potential_signals) / len(potential_signals) if potential_signals else 0
decay_rate = math.log(avg_potential) if avg_potential > 0 else 0.1

# Real computation begins here — complex data transformation
prime_mask = [1 if i > 1 and all(i % p != 0 for p in range(2, int(i**0.5)+1)) else 0 for i in range(200)]

# Bit manipulation red herring
obfuscation_key = 0
for i in range(8):
    obfuscation_key ^= (i * 13) & 0b1101

# List comprehension with filtering and transformation (core concept)
processed_values = [
    processor.transform(node['signal']) 
    for node in network_nodes 
    if node['active'] and prime_mask[node['signal']]
]

# Secondary distractor: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Dead code path (never executed due to condition)
system_diagnostic = None
if DEBUG_MODE and retry_attempts > 5:
    system_diagnostic = [fibonacci(x % 10) for x in processed_values]

# Conditional mutation based on hidden logic
threshold = 20
adjusted_values = []
for val in processed_values:
    if val > threshold:
        adjusted_values.append(val // 2)
    else:
        adjusted_values.append(val)

# Core aggregation logic buried in distractions
def aggregate_transform(nodes):
    active_squares = [
        n['signal'] for n in nodes 
        if n['active'] and int(math.sqrt(n['signal']))**2 == n['signal']
    ]
    
    # This part is actually irrelevant but looks important
    dummy_accum = 0
    for n in nodes:
        if n['mode'] == 'EVEN':
            dummy_accum += n['signal'] * 2
    
    # Real calculation: sum of processed adjusted values minus square root of first active square
    base_sum = sum(adjusted_values)
    correction = int(math.sqrt(active_squares[0])) if active_squares else 0
    return base_sum - correction

# Key execution point
final_flux = aggregate_transform(network_nodes)

# Output the result as required
print(f"Result: {final_flux}")