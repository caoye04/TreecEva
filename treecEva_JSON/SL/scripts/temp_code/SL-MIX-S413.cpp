#define _USE_MATH_DEFINES
#include <iostream>

class RoboticArm {
private:
    int position;
    int state;
    int fib_prev;
    int fib_curr;

public:
    RoboticArm() : position(0), state(0), fib_prev(0), fib_curr(1) {}
    
    // Operator overloading for movement
    RoboticArm& operator+=(int increment) {
        position += increment;
        return *this;
    }
    
    // Move constructor
    RoboticArm(RoboticArm&& other) noexcept 
        : position(other.position), state(other.state), 
          fib_prev(other.fib_prev), fib_curr(other.fib_curr) {
        other.position = 0;
        other.state = 0;
    }
    
    int get_position() const { return position; }
    int get_state() const { return state; }
    
    void update_fibonacci() {
        int temp = fib_curr;
        fib_curr = fib_prev + fib_curr;
        fib_prev = temp;
    }
    
    int get_fibonacci() const { return fib_curr; }
    
    void transition_state(bool sensor_A, bool sensor_B) {
        // State transition logic using boolean operations
        if ((sensor_A && !sensor_B) || (state == 0)) {
            state = 1;
        } else if ((!sensor_A && sensor_B) && state != 2) {
            state = 2;
        } else if (!(sensor_A || sensor_B)) {
            state = 3;
        } else {
            state = 0;
        }
    }
};

int main() {
    RoboticArm arm;
    int final_position = 0;
    
    // Controller sequence
    for (int i = 0; i < 5; ++i) {
        bool sensor_A = (i % 2 == 0);
        bool sensor_B = (i % 3 == 0);
        
        arm.transition_state(sensor_A, sensor_B);
        arm.update_fibonacci();
        
        // Move based on state and fibonacci value
        if (arm.get_state() == 1 || arm.get_state() == 2) {
            arm += arm.get_fibonacci();
        } else if (arm.get_state() == 3) {
            arm += (arm.get_fibonacci() * 2);
        }
    }
    
    final_position = arm.get_position();
    std::cout << "Result: " << final_position << std::endl;
    return 0;
}