import itertools
import string

def decode_network_packets(packets, noise_level=3):
    # Initialize tracking variables
    active_signals = set()
    noise_signals = set()
    signal_strength = 0
    packet_count = len(packets)
    
    # Process packet data
    for i, packet in enumerate(packets):
        # Extract packet components
        packet_id = i + 1
        packet_chars = set(packet.lower())
        
        # Track signal characters
        if packet_id % noise_level == 0:
            # These are noise packets - misleading calculation
            noise_signals.update(packet_chars)
            potential_strength = sum(ord(c) for c in packet_chars)
            signal_strength -= potential_strength // 10
        else:
            # Real signal packets
            active_signals.update(packet_chars)
            signal_strength += sum(ord(c) - 96 for c in packet_chars if c.isalpha())
    
    # Calculate signal-to-noise ratio (distraction calculation)
    signal_noise_ratio = len(active_signals) / (len(noise_signals) or 1)
    
    # Unused function for distraction
    def calculate_packet_entropy(p):
        char_freq = {}
        for c in p:
            char_freq[c] = char_freq.get(c, 0) + 1
        return sum(-freq/len(p) * (freq/len(p)) for freq in char_freq.values())
    
    # More distraction variables
    all_ascii = set(string.ascii_lowercase)
    missing_chars = all_ascii - active_signals
    redundant_chars = active_signals.intersection(noise_signals)
    
    # Key signal processing - this is what matters
    signal_chars = set(c for c in active_signals if ord(c) % 2 == 1)  # Odd ASCII values
    base_value = sum(1 for c in signal_chars if c.isalpha())
    
    # More distractions
    potential_combinations = list(itertools.combinations(signal_chars, min(3, len(signal_chars))))
    combination_value = len(potential_combinations) if potential_combinations else 0
    
    # This doesn't affect the final result
    if combination_value > 10:
        signal_strength += combination_value // 2
    elif combination_value > 0:
        signal_strength += combination_value
        
    # Critical calculation - the actual answer derivation
    common_chars = active_signals.intersection(set('networkpacket'))
    filtered_common_chars = len([c for c in common_chars if c in signal_chars])
    
    # Red herring final calculations
    final_score = signal_strength * signal_noise_ratio
    adjusted_score = final_score // (packet_count or 1)
    
    return {
        "signal_strength": signal_strength,
        "noise_ratio": signal_noise_ratio,
        "active_signals": len(active_signals),
        "key_signal_count": filtered_common_chars,
        "final_score": adjusted_score
    }

# Test data
packets = ["Network", "Protocol", "Analysis", "TCP", "Packet", "Data"]
result = decode_network_packets(packets)
print(f"Result: {result['key_signal_count']}")