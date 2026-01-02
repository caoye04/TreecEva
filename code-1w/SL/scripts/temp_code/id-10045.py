def analyze_phases():
    signals = [0.3, 0.5, 0.7, 0.2, 0.9, 0.1]
    thresholds = [0.6, 0.4, 0.8]
    total_phase = 0
    temp_offset = 0.0

    for i, signal in enumerate(signals):
        temp_offset = (signal * 2) % 1
        if temp_offset > thresholds[i % len(thresholds)]:
            total_phase += int(temp_offset * 10)
        else:
            if signal < 0.25:
                break
    return total_phase

result = analyze_phases()
print(f"Result: {result}")