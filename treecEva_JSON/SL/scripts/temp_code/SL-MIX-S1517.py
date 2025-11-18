import math

temperature_data = [
    [12.3, 14.7, 16.2, 18.1, 21.3, 25.6, 27.8, 26.5, 23.4, 19.2, 15.7, 13.4],  # Region 1
    [8.9, 10.2, 12.5, 15.6, 19.8, 23.7, 26.9, 25.1, 21.7, 17.3, 12.8, 9.6],   # Region 2
    [14.2, 15.8, 17.9, 20.1, 24.3, 28.7, 30.2, 29.1, 25.6, 21.4, 17.8, 15.1], # Region 3
    [6.5, 8.3, 11.2, 14.5, 18.7, 22.9, 25.8, 24.3, 20.1, 15.9, 10.7, 7.8]     # Region 4
]

yearly_averages = []
for region in temperature_data:
    total = 0.0
    for temp in region:
        total += temp
    yearly_avg = total / len(region)
    yearly_averages.append(yearly_avg)

# Count how many yearly averages are above the threshold
threshold = 15.0
above_threshold_count = sum(map(lambda avg: avg > threshold, yearly_averages))

print(f"Result: {above_threshold_count}")