#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>

template<int N>
class PositionDecoder {
public:
    static int decode(int encoded) {
        int base = (encoded >> 8) & 0xFF;
        int offset = encoded & 0xFF;
        if (offset & 0x80) {
            offset = offset - 256;  // Sign extend for negative offsets
        }
        return base + offset;
    }
};

template<>
class PositionDecoder<0> {
public:
    static int decode(int encoded) {
        return (encoded & 0xFF) * 2;
    }
};

class RoboticArmController {
private:
    int currentPosition;
    
public:
    RoboticArmController() : currentPosition(0) {}
    
    int processMovements(const std::vector<int>& commands) {
        for (size_t i = 0; i < commands.size(); ++i) {
            int cmd = commands[i];
            int mode = (cmd >> 16) & 0xF;
            int encoded = cmd & 0xFFFF;
            
            if (mode == 0xF) {
                // Emergency stop command
                break;
            }
            
            int delta;
            if (mode == 0) {
                delta = PositionDecoder<0>::decode(encoded);
            } else {
                delta = PositionDecoder<1>::decode(encoded);
            }
            
            // Check for safety limits
            if (currentPosition + delta > 1000) {
                return currentPosition;  // Early return if limit exceeded
            }
            
            currentPosition += delta;
            
            // Special adjustment every 3 movements
            if ((i + 1) % 3 == 0) {
                currentPosition = (currentPosition / 10) * 10;  // Round to nearest 10
            }
        }
        return currentPosition;
    }
};

int main() {
    RoboticArmController arm;
    std::vector<int> movementCommands = {
        (0x1 << 16) | 0x0205,  // Mode 1: base=2, offset=5
        (0x0 << 16) | 0x000A,  // Mode 0: value=10*2=20
        (0x1 << 16) | 0x01F0,  // Mode 1: base=1, offset=-16
        (0x1 << 16) | 0x0307,  // Mode 1: base=3, offset=7
        (0xF << 16) | 0xABCD   // Emergency stop
    };
    
    int finalPosition = arm.processMovements(movementCommands);
    std::cout << "Result: " << finalPosition << std::endl;
    return 0;
}