from collections import defaultdict
import statistics

def decode_sensor_data(raw_data):
    states = {'START': 0, 'READING': 1, 'END': 2}
    current_state = states['START']
    decoded_values = []
    buffer = ''
    
    for char in raw_data:
        if current_state == states['START']:
            if char == '[':
                current_state = states['READING']
                buffer = ''
        elif current_state == states['READING']:
            if char == ']':
                current_state = states['END']
                try:
                    decoded_values.append(int(buffer, 16))
                except ValueError:
                    pass
            elif char.isdigit() or char.lower() in 'abcdef':
                buffer += char
            else:
                buffer = ''
        elif current_state == states['END']:
            if char == '[':
                current_state = states['READING']
                buffer = ''
    return decoded_values

sensor_readings = [
    "[1a][2b][3c][4d][5e][6f][7g][8h][9i][aj]",
    "[ff][ee][dd][cc][bb][aa][99][88][77][66]",
    "[0][10][20][30][40][50][60][70][80][90]"
]

decoded_temperatures = defaultdict(list)
for idx, reading in enumerate(sensor_readings):
    decoded_temperatures[idx] = decode_sensor_data(reading)

anomaly_count = 0
for sensor_id, temps in decoded_temperatures.items():
    if len(temps) > 1:
        mean_temp = statistics.mean(temps)
        stdev_temp = statistics.stdev(temps) if len(temps) > 1 else 0
        for temp in temps:
            if abs(temp - mean_temp) > 2 * stdev_temp:
                anomaly_count += 1

print(f"Result: {anomaly_count}")