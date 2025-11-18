import heapq
import statistics

def detect_anomalies(packet_sizes, window_size=5):
    min_heap = []
    max_heap = []
    anomalies = []
    
    def add_number(num):
        # Max heap (negate values)
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        
        # Rebalance heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    def find_median():
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        return -max_heap[0] if len(max_heap) > len(min_heap) else min_heap[0]
    
    window_data = []
    for i, size in enumerate(packet_sizes):
        window_data.append(size)
        add_number(size)
        
        if len(window_data) > window_size:
            old_val = window_data.pop(0)
            # Remove old_val from heaps (simplified approach)
            # In practice, we'd use an indexed priority queue
            max_heap.clear()
            min_heap.clear()
            for val in window_data:
                add_number(val)
        
        if len(window_data) == window_size:
            median = find_median()
            mean_val = statistics.mean(window_data)
            std_dev = statistics.stdev(window_data) if len(window_data) > 1 else 0
            
            # Anomaly detection: Z-score based
            if std_dev > 0:
                z_score = abs((size - mean_val) / std_dev)
                if z_score > 1.5:  # Threshold for anomaly
                    anomalies.append(z_score)
    
    return sum(anomalies) if anomalies else 0

# Firewall packet sizes (in bytes)
firewall_logs = [128, 256, 512, 64, 1024, 32, 2048, 4096, 16, 8192, 128, 256, 512]
anomaly_score = detect_anomalies(firewall_logs, window_size=6)
print(f"Result: {anomaly_score}")