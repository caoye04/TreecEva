from collections import Counter

# Simulate daily lab equipment bookings over a week
equipment_bookings = ['microscope', 'centrifuge', 'microscope', 'spectrometer', 'centrifuge', 'microscope', 'incubator']
booking_counts = Counter(equipment_bookings)

total_devices = 5
peak_usage = booking_counts.most_common(1)[0][1]  # highest booking count

# Calculate available slots based on device availability and peak demand
used_slots = total_devices - (peak_usage // 2)
available_slots = used_slots if used_slots > 0 else 0
default = 10

final_capacity = max(available_slots, default=0)
print(f"Result: {final_capacity}")