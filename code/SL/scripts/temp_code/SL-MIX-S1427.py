signal_amplitude = 42
noise_floor = 10
saturation_level = 100

# Check if signal is above noise and not saturated
is_above_noise = (signal_amplitude % 7 == 0)
is_below_saturation = (signal_amplitude < saturation_level)
meets_basic_criteria = is_above_noise and is_below_saturation

# Additional quality check using logical NOT
interference_check = not (signal_amplitude % 3 != 0)
quality_flag = meets_basic_criteria or interference_check

print(f"Result: {int(quality_flag)}")