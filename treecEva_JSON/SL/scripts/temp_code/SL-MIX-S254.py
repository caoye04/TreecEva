import heapq
from dataclasses import dataclass

@dataclass
class SharkPosition:
    name: str
    longitude: float
    latitude: float

shark_data = [
    SharkPosition("Alpha", -152.37, 37.42),
    SharkPosition("Beta", -155.29, 36.81),
    SharkPosition("Gamma", -150.85, 38.22)
]

longitudes = [shark.longitude for shark in shark_data]
heap = longitudes.copy()
heapq.heapify(heap)

smallest = heapq.heappop(heap)
largest = heapq.heappop(heap)
convergence_longitude = heapq.heappop(heap)

print(f"Result: {convergence_longitude}")