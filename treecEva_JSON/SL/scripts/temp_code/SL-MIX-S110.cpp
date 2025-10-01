#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
private:
    std::vector<int> data;
public:
    DataProcessor(std::vector<int> input) : data(input) {}
    
    int computeXORSum() {
        int xor_sum = 0;
        for (size_t i = 0; i < data.size(); ++i) {
            xor_sum ^= data[i];
        }
        return xor_sum;
    }
    
    void transformData() {
        for (size_t i = 0; i < data.size(); ++i) {
            if (data[i] % 2 == 0) {
                data[i] = static_cast<int>(std::pow(data[i], 2));
            } else {
                data[i] = static_cast<int>(std::sqrt(data[i]));
            }
        }
    }
};

struct Point {
    double x, y;
    Point(double x_val, double y_val) : x(x_val), y(y_val) {}
    
    double distanceFrom(const Point& other) const {
        return std::sqrt((x - other.x)*(x - other.x) + (y - other.y)*(y - other.y));
    }
};

int main() {
    // Initialize data processor with values
    DataProcessor proc({4, 9, 16, 25, 36});
    
    // Perform initial XOR sum
    int initial_xor = proc.computeXORSum();
    
    // Transform data according to rules
    proc.transformData();
    
    // Compute transformed XOR sum
    int transformed_xor = proc.computeXORSum();
    
    // Calculate difference between XOR sums
    int diff_xor = transformed_xor - initial_xor;
    
    // Create geometric points based on calculations
    Point p1(static_cast<double>(diff_xor), std::sin(M_PI / 4));
    Point p2(std::cos(M_PI / 4), static_cast<double>(diff_xor * 2));
    
    // Calculate distance between points
    double dist = p1.distanceFrom(p2);
    
    // Perform bit shifting operations
    int shifted_left = diff_xor << 2;
    int shifted_right = shifted_left >> 1;
    
    // Apply modulo operation
    int mod_result = shifted_right % 7;
    
    // Final calculation combining all results
    int final_result = static_cast<int>(dist * 1000) + mod_result;
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}