#define _USE_MATH_DEFINES
#include <iostream>
#include <variant>
#include <cmath>

typedef std::variant<int, float> SignalType;

enum State { LOW, MED, HIGH };

float process_signal(SignalType input, int mask) {
    float result = 0.0f;
    State current_state = LOW;
    
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(std::holds_alternative<int>(input)) {
                int value = std::get<int>(input);
                int masked = value & (mask >> i);
                
                switch(current_state) {
                    case LOW:
                        result += masked * 1.5f;
                        current_state = (masked > 10) ? MED : LOW;
                        break;
                    case MED:
                        result -= masked >> 2;
                        current_state = (masked < 5) ? LOW : HIGH;
                        break;
                    case HIGH:
                        result *= masked ^ 0xF;
                        current_state = LOW;
                        break;
                }
            } else {
                float value = std::get<float>(input);
                int converted = static_cast<int>(std::floor(value));
                result += converted & (mask | (1 << j));
            }
        }
    }
    
    return result;
}

int main() {
    SignalType signal = 42;
    int filter_mask = 0b1101;
    float processed_signal = process_signal(signal, filter_mask);
    std::cout << "Result: " << processed_signal << std::endl;
    return 0;
}