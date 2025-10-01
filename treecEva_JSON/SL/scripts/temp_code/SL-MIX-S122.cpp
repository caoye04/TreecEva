#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
public:
    static int process(int x, int y) {
        return (x * 2 + y) ^ (x & y);
    }
};

struct Point {
    double x, y;
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    double distance(const Point& other) const {
        return sqrt(pow(x - other.x, 2) + pow(y - other.y, 2));
    }
};

int main() {
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int a = 5, b = 3;
    int temp = DataProcessor::process(a, b);
    
    Point p1(3.0, 4.0);
    Point p2(0.0, 0.0);
    double dist = p1.distance(p2);
    
    std::string s = "hello";
    s += " world";
    int str_length = s.length();
    
    int result = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            if ((i + j) % 2 == 0) {
                result += matrix[i][j] * temp;
            } else {
                result -= static_cast<int>(dist) * matrix[i][j];
            }
        }
    }
    
    result = result ^ str_length;
    result = result & 0xFF;
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}