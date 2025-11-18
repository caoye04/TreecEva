import heapq
from collections import defaultdict

def calculate_package_score(weight, loyalty):
    base = (weight << 2) ^ loyalty
    return base % 100

class DeliveryManager:
    def __init__(self):
        self.request_heap = []
        heapq.heapify(self.request_heap)
        self.customer_profiles = defaultdict(int)
    
    def add_request(self, customer_id, weight):
        self.customer_profiles[customer_id] += 1
        loyalty_points = self.customer_profiles[customer_id] * 5
        score = calculate_package_score(weight, loyalty_points)
        heapq.heappush(self.request_heap, (-score, customer_id))
        if len(self.request_heap) > 5:
            heapq.heappop(self.request_heap)
    
    def process_requests(self):
        total_priority = 0
        while self.request_heap:
            priority, cust_id = heapq.heappop(self.request_heap)
            if cust_id & 1 == 0:  # Even customer IDs get bonus
                total_priority += (-priority) << 1
            else:
                total_priority += (-priority)
        return total_priority

dm = DeliveryManager()
requests = [(101, 12), (102, 8), (103, 15), (104, 6), (105, 20), (102, 10)]
for req in requests:
    dm.add_request(req[0], req[1])
total_priority = dm.process_requests()
print(f"Result: {total_priority}")