temperature = 37.5
pressure = 98.7
energy_level = int(temperature * 2 + pressure)
threshold = 170
system_status = (energy_level ** 0.5) * 3.1
backup_status = energy_level / 2.5
energy_threshold = system_status + 10
final_diagnostic = system_status if energy_level > threshold else backup_status
energy_threshold = final_diagnostic * 0.8
Result: {energy_threshold}