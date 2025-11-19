import math
from collections import defaultdict

class RobotNavigator:
    def __init__(self):
        self.position = {'radius': 0, 'theta': 0}
        self.theta_delta = 0
        self.state = 'INIT'
        self.movement_log = defaultdict(list)
    
    def update_position(self, radius_change, theta_change):
        old_theta = self.position['theta']
        self.position['radius'] += radius_change
        self.position['theta'] = (self.position['theta'] + theta_change) % (2 * math.pi)
        self.theta_delta += abs(self.position['theta'] - old_theta)
        
    def navigate(self):
        # State machine for robot navigation
        steps = [
            (3, math.pi/4),
            (2, math.pi/2),
            (-1, -math.pi/3),
            (4, math.pi),
            (0, math.pi/6)
        ]
        
        for i, (r_delta, t_delta) in enumerate(steps):
            if i % 2 == 0:
                if self.position['radius'] > 5:
                    self.state = 'FAR'
                    r_delta *= 0.5
                else:
                    self.state = 'NEAR'
            else:
                if self.position['theta'] > math.pi:
                    self.state = 'UPPER_HALF'
                    t_delta *= -1
                else:
                    self.state = 'LOWER_HALF'
            
            self.update_position(r_delta, t_delta)
            self.movement_log[self.state].append((r_delta, t_delta))
            
            # Additional calculation based on current state
            if self.state == 'FAR' and len(self.movement_log['FAR']) >= 1:
                correction = math.log(max(1, self.position['radius']))
                self.position['theta'] = (self.position['theta'] + correction) % (2 * math.pi)
                self.theta_delta += correction

robot = RobotNavigator()
robot.navigate()
print(f"Target result: {round(robot.theta_delta, 6)}")