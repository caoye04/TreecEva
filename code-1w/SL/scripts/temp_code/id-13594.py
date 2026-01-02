from collections import defaultdict, Counter
import math

# System parameters (some are red herrings)
base_frequency = 440.0
harmonic_dampener = 0.87
max_iterations = 150
threshold = 0.001
dummy_flag = True
payload_size = 2048
overhead_ratio = 0.12

# Irrelevant audio synthesis variables
note_sequence = ['C4', 'E4', 'G4', 'B4']
audio_buffer = [0.0] * 512
modulation_depth = 0.6

# Network channel configuration (core data)
channel_noise = [0.05, 0.08, 0.03, 0.12, 0.07, 0.09, 0.04, 0.11]
bandwidth_pool = [120, 95, 150, 88, 134, 97, 110, 142]
snr_ratios = [math.log(1 + (bw / noise)) for bw, noise in zip(bandwidth_pool, channel_noise)]

# Misleading signal processing function (never called)
def apply_fourier_transform(signal):
    result = []
    for i in range(len(signal)):
        component = 0
        for j in range(len(signal)):
            angle = 2 * math.pi * i * j / len(signal)
            component += signal[j] * (math.cos(angle) - 1j * math.sin(angle))
        result.append(component)
    return result

# Unused error correction tables
ecc_matrix = [[(i + j) % 256 for j in range(16)] for i in range(16)]
redundancy_pattern = bytearray([i ^ 0xAA for i in range(256)])

# Core optimization logic with distractors embedded
def evaluate_spectral_efficiency(snr_list, weights=None):
    if weights is None:
        weights = [1.0] * len(snr_list)
    
    # Distraction: complex weighting that gets overridden
    temp_weights = [w * 0.95 for w in weights]
    adjusted_snr = [snr * math.sqrt(w) for snr, w in zip(snr_list, temp_weights)]
    
    # Actual relevant computation
    efficiency = sum(math.log2(1 + snr) for snr in snr_list)  # Shannon-Hartley basis
    return efficiency

# Data structure manipulation with decoy paths
def process_channel_metadata(metadata_strings):
    meta_counter = Counter()
    path_trie = defaultdict(dict)
    
    for s in metadata_strings:
        prefix = s[:3]
        suffix = s[-3:]
        meta_counter[prefix] += 1
        if suffix not in path_trie[prefix]:
            path_trie[prefix][suffix] = []
        path_trie[prefix][suffix].append(s)
    
    # This slice operation is critical later
    key_segment = meta_counter.most_common()[1:4]  # slicing irrelevant here but looks important
    return path_trie, key_segment

# Another decoy function with bit manipulation red herring
def scramble_bits(value, shift=3):
    """Unused obfuscation function"""
    scrambled = ((value << shift) & 0xFF) | ((value >> (8 - shift)) & 0xFF)
    return scrambled ^ 0x5A

# Main optimization algorithm
channels_active = [True, False, True, True, False, True, True, False]
def optimize_channel_capacity():
    # Local configuration
    config_map = {'gain': 1.8, 'attenuation': 0.75, 'boost': 2.0}
    
    # Distractor: unused nested dictionary construction
    performance_log = {}
    for idx in range(len(channel_noise)):
        if f'chan_{idx}' not in performance_log:
            performance_log[f'chan_{idx}'] = {}
        for metric in ['jitter', 'drift', 'skew']:
            performance_log[f'chan_{idx}'][metric] = 0.0
    
    # Critical data filtering masked among distractions
    active_indices = [i for i, active in enumerate(channels_active) if active]
    filtered_bandwidth = [bandwidth_pool[i] for i in active_indices]  # 120, 150, 88, 97, 110
    filtered_snr = [snr_ratios[i] for i in active_indices]  # Corresponding SNR values
    
    # Decoy statistical calculation
    mean_bandwidth = sum(filtered_bandwidth) / len(filtered_bandwidth)
    variance = sum((bw - mean_bandwidth) ** 2 for bw in filtered_bandwidth) / len(filtered_bandwidth)
    std_dev = math.sqrt(variance)
    
    # Red herring: string manipulation that seems important
    status_codes = ['OK', 'ERR', 'OK', 'OK', 'ERR', 'OK', 'OK', 'ERR']
    code_stats = ''.join(status_codes).count('OK')
    
    # Another distraction: fake packet simulation
    packet_stream = []
    for i in range(payload_size // 64):
        packet = f"PKT:{i:04d}:{status_codes[i % len(status_codes)]}:END"
        packet_stream.append(packet)
    
    # Real computation begins: spectral efficiency evaluation
    efficiency_score = evaluate_spectral_efficiency(filtered_snr)
    
    # Metadata processing with side effect on answer
    metadata_tags = [
        'CHN-A01-UP', 'CHN-B12-DN', 'CHN-C03-UP', 'CHN-D04-UP',
        'CHN-E05-DN', 'CHN-F06-UP', 'CHN-G07-UP', 'CHN-H08-DN'
    ]
    _, segment_data = process_channel_metadata(metadata_tags)
    
    # Extract numeric influence from metadata (looks like it's not used, but it is)
    influence_value = sum(item[1] for item in segment_data)  # 1+1+1 = 3
    
    # Final capacity calculation - this is where answer comes from
    raw_capacity = efficiency_score * config_map['gain'] * config_map['boost']
    adjusted_capacity = raw_capacity - (influence_value * 0.5)
    final_bandwidth = int(round(adjusted_capacity * 10)) * 10  # Scale to integer
    
    # Dead code path - never executed
    if dummy_flag and False:
        fallback = 0
        for ch in audio_buffer:
            fallback += int(abs(ch) * 100)
        final_bandwidth = fallback
    
    return final_bandwidth

# Execution point of interest
target_result = optimize_channel_capacity()
print(f"Target result: {target_result}")