vehicle_states = {'V001': 'idle', 'V002': 'cruising', 'V003': 'braking', 'V004': 'accelerating'}
speed_changes = {'V001': 15, 'V002': -5, 'V003': -10, 'V004': 20}
proximity_alerts = {'V001': False, 'V002': True, 'V003': True, 'V004': False}

transition_rules = {
    'idle': lambda spd, alert: 'accelerating' if spd > 0 else 'idle',
    'accelerating': lambda spd, alert: 'cruising' if spd == 0 and not alert else ('braking' if spd < 0 or alert else 'accelerating'),
    'cruising': lambda spd, alert: 'braking' if spd < 0 or alert else 'cruising',
    'braking': lambda spd, alert: 'idle' if spd == 0 and not alert else ('accelerating' if spd > 0 and not alert else 'braking')
}

state_transitions = {vid: transition_rules[state](speed_changes[vid], proximity_alerts[vid]) for vid, state in vehicle_states.items()}

state_energy_costs = {'idle': 0, 'accelerating': 3, 'cruising': 1, 'braking': 2}
total_energy = sum(state_energy_costs[state] for state in state_transitions.values())

active_vehicles = len([s for s in state_transitions.values() if s != 'idle'])
fleet_efficiency_score = (active_vehicles * 100) - (total_energy * 5)

print(f'Result: {fleet_efficiency_score}')