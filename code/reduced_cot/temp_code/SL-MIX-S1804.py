import statistics

# State definitions
IDLE, ACTIVE, REPORT = 0, 1, 2
current_state = IDLE

# Batch data: speeds in km/h
batches = [
    [60, 70, 80, 90],
    [55, 65, 75, 85, 95],
    [50, 60, 70]
]

exceed_count = 0

for batch in batches:
    current_state = ACTIVE
    avg_speed = statistics.mean(batch)
    exceeds = [speed > avg_speed for speed in batch]
    exceed_count += sum(exceeds)
    current_state = REPORT

print(f"Result: {exceed_count}")