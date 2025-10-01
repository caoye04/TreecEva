#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
public:
    static int process(int x) {
        return (x % 7 == 0) ? (x / 7) : (x * 3 + 1);
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
    std::vector<int> nums = {15, 28, 9, 42, 11, 77, 33, 50};
    std::vector<Point> points = {Point(0,0), Point(3,4), Point(1,1), Point(5,12)};
    
    int sum = 0;
    for (size_t i = 0; i < nums.size(); ++i) {
        int val = DataProcessor::process(nums[i]);
        sum += (val & 0x1) ? (val ^ 0xF) : (val >> 1);
    }
    
    double maxDist = 0;
    for (size_t i = 0; i < points.size(); ++i) {
        for (size_t j = i+1; j < points.size(); ++j) {
            double d = points[i].distance(points[j]);
            if (d > maxDist) maxDist = d;
        }
    }
    
    std::string s = "COMPUTATION";
    int charSum = 0;
    for (char c : s) {
        charSum += (c - 'A' + 1);
    }
    
    int result = static_cast<int>(maxDist) * (sum % 10) + (charSum & 0x1F);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}