import heapq

class Package:
    def __init__(self, id, urgency):
        self.id = id
        self.urgency = urgency
    
    def __lt__(self, other):
        return self.urgency < other.urgency

packages = [
    Package('PKG001', 15),
    Package('PKG002', 7),
    Package('PKG003', 22),
    Package('PKG004', 3),
    Package('PKG005', 11),
    Package('PKG006', 19),
    Package('PKG007', 2),
    Package('PKG008', 14)
]

# Create a min-heap from the packages based on urgency
heap = []
for pkg in packages:
    heapq.heappush(heap, pkg)

batch_sums = []
while heap:
    batch_sum = 0
    for _ in range(min(3, len(heap))):  # Process up to 3 packages per batch
        pkg = heapq.heappop(heap)
        batch_sum += pkg.urgency
    batch_sums.append(batch_sum)

total_batch_sum = sum(batch_sums)
print(f"Result: {total_batch_sum}")