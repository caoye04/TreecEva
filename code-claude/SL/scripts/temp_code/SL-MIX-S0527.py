def calculate_hash(text):
    # Hash calculation (distractor function)
    hash_value = 0
    for char in text:
        hash_value = (hash_value * 31 + ord(char)) % 997
    return hash_value

def analyze_network_traffic(packets):
    # Network analysis (distractor function)
    total_bytes = sum(len(p) for p in packets)
    unique_packets = len(set(packets))
    return total_bytes * unique_packets // 8

def calculate_final_strength(data):
    # Main calculation function - this is relevant
    base_value = len(data)
    if base_value == 0:
        return 0
    
    # Extract digits from the data
    digits = [int(c) for c in data if c.isdigit()]
    if not digits:
        digits = [5, 7, 2]  # Default values
    
    # Security metrics (distractions)
    entropy_score = sum(ord(c) for c in data) % 100
    redundancy_factor = len(set(data)) / max(1, len(data))
    vulnerability_index = calculate_hash(data[:5]) if len(data) > 5 else 42
    
    # Core calculation (relevant)
    strength_factor = (digits[0] * 10 + digits[-1]) ^ (digits[1] if len(digits) > 1 else 3)
    
    # Misleading calculations (distractions)
    potential_keys = {"high": 255, "medium": 127, "low": 63}
    security_class = "medium" if entropy_score > 50 else "low"
    if vulnerability_index < 30:
        security_class = "high"
    
    # This branch is never taken due to the data structure
    if isinstance(data, dict) and "priority" in data:
        return data["priority"] * 100
    
    # Misleading operation that doesn't affect the result
    if len(digits) > 3:
        strength_factor = strength_factor | (digits[2] << 2)
    
    # Final calculation (relevant)
    result = (strength_factor & 0xFF) + (base_value % 10)
    
    return result

# Network simulation data (distraction)
network_packets = ["TCP:192.168.1.1", "UDP:10.0.0.1", "TCP:192.168.1.1"]
network_load = analyze_network_traffic(network_packets)

# Data preparation (relevant for final answer)
raw_data = "CyberSec2023"
processed_data = raw_data.lower().replace("cyber", "c") + "45"

# Misleading variables (distractions)
potential_strength = calculate_hash(raw_data)
security_threshold = network_load // 10
encryption_modes = {"AES": 256, "DES": 56, "3DES": 168}

# Key calculation (this is the critical step)
encryption_strength = calculate_final_strength(processed_data)

# More distractions
if security_threshold > encryption_strength:
    recommended_algorithm = "AES"
else:
    recommended_algorithm = "3DES"

# Further processing that doesn't affect the result
final_config = {
    "algorithm": recommended_algorithm,
    "key_length": encryption_modes[recommended_algorithm],
    "strength": encryption_strength,
    "network_status": "secure" if network_load < 100 else "vulnerable"
}

print(f"Result: {encryption_strength}")