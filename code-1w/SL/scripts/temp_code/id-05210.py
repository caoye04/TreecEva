def analyze_efficiency(metrics):
    adjusted = [x * 1.1 for x in metrics if x > 50]
    baseline = sum(metrics) / len(metrics)
    excess = [val for val in adjusted if val > baseline * 1.2]
    return len(excess)

metrics_data = [45, 60, 70, 55, 80, 90, 40]

productivity = 0
for val in metrics_data:
    if val >= 60:
        productivity += val * 0.3

temp_buffer = []
for i in range(len(metrics_data)):
    temp_buffer.append(metrics_data[i] + i * 2)

snapshot = temp_buffer[::2]
dummy_sum = sum(x for x in snapshot if x % 3 == 0)

size_factor = len([x for x in metrics_data if x < 50])
risk_factor = 0.5 if size_factor > 2 else 1.0

intermediate = analyze_efficiency(metrics_data)
bonus_weight = intermediate * 0.25

if bonus_weight > 2:
    productivity *= 1.1
else:
    productivity *= 0.95

scaling_factor = 1 + bonus_weight / 10
productivity *= scaling_factor

# Irrelevant transformation chain
counterfeit_index = 0
while counterfeit_index < 5:
    counterfeit_index += 1
    dummy_calc = (counterfeit_index ** 2) % 7

final_score = evaluate_performance(productivity, risk_factor)

# Dummy function to simulate distraction
def evaluate_performance(output, risk):
    if risk < 0.7:
        return int(output * 1.3)
    else:
        return int(output * 1.15)

print(f"Result: {final_score}")