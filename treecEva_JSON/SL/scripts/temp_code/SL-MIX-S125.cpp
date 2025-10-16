#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <regex>
#include <set>
#include <string>
#include <cmath>

using namespace std;

class Point {
public:
    double x, y;
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    
    // Operator overloading for point addition
    Point operator+(const Point& other) const {
        return Point(x + other.x, y + other.y);
    }
    
    // Operator overloading for equality
    bool operator==(const Point& other) const {
        return abs(x - other.x) < 1e-9 && abs(y - other.y) < 1e-9;
    }
};

// Custom hash function for Point to use in unordered_set
namespace std {
    template<> struct hash<Point> {
        size_t operator()(const Point& p) const {
            return hash<double>()(p.x) ^ (hash<double>()(p.y) << 1);
        }
    };
}

int main() {
    // Matrix representing movement vectors
    vector<vector<double>> movements = {{1.0, 2.0}, {3.0, -1.0}, {0.0, 2.5}, {-2.0, 1.0}, {1.5, 0.5}};
    
    // Starting position
    Point current_pos(0.0, 0.0);
    
    // Target pattern regex (looks for coordinates with integer parts)
    regex pattern(R"(\b\d+\.0\b)");
    
    // History of visited positions
    set<Point> visited;
    
    // Counter for matched positions
    int matched_positions = 0;
    
    for (const auto& move : movements) {
        // Move the robot
        Point movement_vector(move[0], move[1]);
        current_pos = current_pos + movement_vector;
        
        // Add to visited positions
        visited.insert(current_pos);
        
        // Check if current position matches the pattern
        string coord_str = to_string(current_pos.x) + "," + to_string(current_pos.y);
        if (regex_search(coord_str, pattern)) {
            matched_positions++;
        }
    }
    
    cout << "Result: " << matched_positions << endl;
    return 0;
}