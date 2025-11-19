from collections import deque

class DayNode:
    def __init__(self, duration):
        self.duration = duration
        self.next = None

def create_linked_list(durations):
    if not durations:
        return None
    head = DayNode(durations[0])
    current = head
    for duration in durations[1:]:
        current.next = DayNode(duration)
        current = current.next
    return head

daily_durations = deque([10, 15, 12, 8, 20, 18, 22])
checkout_history = []

for _ in range(len(daily_durations)):
    day_duration = daily_durations.popleft()
    checkout_history.append(day_duration)

linked_days = create_linked_list(checkout_history)
weekly_total = 0
current_day = linked_days

while current_day:
    weekly_total += current_day.duration
    current_day = current_day.next

print(f"Result: {weekly_total}")