#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <memory>
#include <cmath>

struct Position {
    int x = 0;
    int y = 0;
};

class Robot {
private:
    std::unique_ptr<Position> pos;

public:
    Robot() : pos(std::make_unique<Position>()) {}
    
    void move(int dx, int dy) {
        pos->x += dx;
        pos->y += dy;
    }
    
    int getManhattanDistance() const {
        return std::abs(pos->x) + std::abs(pos->y);
    }
    
    Position getPosition() const { return *pos; }
};

std::string transformInstruction(const std::string& input) {
    std::string result = "";
    for (char c : input) {
        if (c >= 'A' && c <= 'Z') {
            result += static_cast<char>(c + 32); // Convert to lowercase
        } else if (c == 'l') {
            result += "left";
        } else if (c == 'r') {
            result += "right";
        } else {
            result += c;
        }
    }
    return result;
}

void executeMovement(Robot& robot, const std::string& command) {
    if (command == "north") {
        robot.move(0, 1);
    } else if (command == "south") {
        robot.move(0, -1);
    } else if (command == "east") {
        robot.move(1, 0);
    } else if (command == "west") {
        robot.move(-1, 0);
    } else if (command.substr(0, 4) == "left") {
        int steps = command.length() > 4 ? std::stoi(command.substr(4)) : 1;
        robot.move(-steps, 0);
    } else if (command.substr(0, 5) == "right") {
        int steps = command.length() > 5 ? std::stoi(command.substr(5)) : 1;
        robot.move(steps, 0);
    }
}

int main() {
    Robot rover;
    std::string raw_commands[] = {"N", "E", "L3", "R2", "S"};
    int num_commands = sizeof(raw_commands)/sizeof(raw_commands[0]);
    
    for (int i = 0; i < num_commands; ++i) {
        std::string transformed = transformInstruction(raw_commands[i]);
        executeMovement(rover, transformed);
    }
    
    int final_distance = rover.getManhattanDistance();
    std::cout << "Result: " << final_distance << std::endl;
    return 0;
}