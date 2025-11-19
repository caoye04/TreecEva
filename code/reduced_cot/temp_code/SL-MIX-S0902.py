import heapq

fresh_bakery_orders = []
heapq.heappush(fresh_bakery_orders, -85)  # Sourdough popularity
heapq.heappush(fresh_bakery_orders, -92)  # Baguette popularity
heapq.heappush(fresh_bakery_orders, -78)  # Ciabatta popularity

heapq.heappop(fresh_bakery_orders)  # Remove most popular

most_popular_remaining = -fresh_bakery_orders[0]
print(f'Result: {most_popular_remaining}')