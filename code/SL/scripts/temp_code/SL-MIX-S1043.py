import re
from collections import deque
from statistics import mean, variance

def calculate_anomaly_score(packet_log):
    # Parse packet sizes from log entries using regex
    packet_sizes = [int(re.search(r'size:(\d+)', entry).group(1)) for entry in packet_log]
    
    # Initialize sliding window as a deque with maximum length 5
    window = deque(maxlen=5)
    anomaly_scores = []
    
    for size in packet_sizes:
        window.append(size)
        
        # Only calculate when window is full
        if len(window) == 5:
            window_mean = mean(window)
            window_variance = variance(window)
            
            # Anomaly condition: variance exceeds threshold or mean outside normal range
            if window_variance > 1000 or not (500 <= window_mean <= 1500):
                anomaly_scores.append(1)
            else:
                anomaly_scores.append(0)
    
    # Final anomaly score is sum of all anomalies weighted by position
    return sum(score * (i + 1) for i, score in enumerate(anomaly_scores))

# Simulated packet log entries
packet_log_entries = [
    "[INFO] Packet src:192.168.1.1 dst:10.0.0.1 size:1024",
    "[INFO] Packet src:192.168.1.2 dst:10.0.0.1 size:512",
    "[WARN] Packet src:192.168.1.3 dst:10.0.0.1 size:2048",
    "[INFO] Packet src:192.168.1.4 dst:10.0.0.1 size:768",
    "[INFO] Packet src:192.168.1.5 dst:10.0.0.1 size:1024",
    "[ALERT] Packet src:192.168.1.6 dst:10.0.0.1 size:4096",
    "[INFO] Packet src:192.168.1.7 dst:10.0.0.1 size:256",
    "[INFO] Packet src:192.168.1.8 dst:10.0.0.1 size:512"
]

anomaly_score = calculate_anomaly_score(packet_log_entries)
print(f"Result: {anomaly_score}")