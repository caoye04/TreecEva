def temperature_correction(func):
    def wrapper(temp):
        corrected = func(temp)
        return corrected + 2.5
    return wrapper

@temperature_correction
def raw_temperature(temp):
    return temp

hourly_readings = [20, 22, 19, 25, 24]
corrected_readings = list(map(raw_temperature, hourly_readings))
valid_readings = list(filter(lambda x: x > 22, corrected_readings))
corrected_average = sum(valid_readings) / len(valid_readings) if valid_readings else 0
print(f"Result: {corrected_average}")