# Track positions of runners in a race
runners = ['Alex', 'Beth', 'Carlos', 'Diana', 'Ethan']
finish_times = {'Alex': '4:32.15', 'Beth': '4:05.89', 'Carlos': '4:15.22', 
              'Diana': '4:10.67', 'Ethan': '4:22.34'}

# Convert time strings to seconds for accurate sorting
time_seconds = {}
for runner, time_str in finish_times.items():
    minutes, rest = time_str.split(':')
    seconds, milliseconds = rest.split('.')
    total_seconds = int(minutes) * 60 + int(seconds) + int(milliseconds) / 100
    time_seconds[runner] = total_seconds

# Sort runners by their finish times
sorted_runners = sorted(runners, key=lambda x: time_seconds[x])

# Calculate positions (1st place, 2nd place, etc.)
sorted_positions = [i + 1 for i in range(len(sorted_runners))]

# Find the middle position
middle_index = len(sorted_positions) // 2
final_position = sorted_positions[middle_index]

print(f"Result: {final_position}")