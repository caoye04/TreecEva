import math

def calculate_byte_risk(byte_val):
    return math.log(byte_val + 1) if byte_val > 0 else 0

def process_packet_headers(headers):
    # Convert hex strings to byte values
    byte_values = [int(b, 16) for b in headers]
    
    # Calculate initial risks using map and lambda
    initial_risks = list(map(lambda x: calculate_byte_risk(x), byte_values))
    
    # Apply exponential weighting to every other byte
    weighted_risks = [
        risk * math.exp(0.1 * i) if i % 2 == 0 else risk
        for i, risk in enumerate(initial_risks)
    ]
    
    # Filter out low-risk values (< 1.0)
    significant_risks = list(filter(lambda x: x >= 1.0, weighted_risks))
    
    # Compute base score as sum of significant risks
    base_score = sum(significant_risks)
    
    # Adjust score based on packet length
    length_adjustment = len(headers) / 10.0
    adjusted_score = base_score * (1.0 + length_adjustment)
    
    # Final risk score with ternary-based thresholding
    final_risk_score = adjusted_score if adjusted_score > 10.0 else adjusted_score * 2.0
    
    return final_risk_score

# Packet header data in hexadecimal
packet_data = ['FF', '0A', 'C3', '1F', '7B', '00', 'E5', '2D']

final_risk_score = process_packet_headers(packet_data)
print(f"Result: {final_risk_score}")