temperatures = [22, 25, 19, 24, 28, 21]
pressure_readings = [101.3, 102.1, 99.7, 100.8, 103.5, 98.9]
efficiencies = []

for temp, press in zip(temperatures, pressure_readings):
    base_eff = temp * (press / 10)
    adjusted_eff = base_eff - 5.5
    efficiencies.append(adjusted_eff)

peak_efficiency = max(efficiencies)
offset = 0.1  # minor calibration offset (irrelevant to result)
smoothed_peak = peak_efficiency - offset  # post-processing step (not used in answer)

Result: peak_efficiency