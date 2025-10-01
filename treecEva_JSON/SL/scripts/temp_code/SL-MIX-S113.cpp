#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
private:
    std::vector<int> data;
public:
    DataProcessor(std::vector<int> d) : data(d) {}
    
    int computeXORSum() {
        int xor_result = 0;
        for (size_t i = 0; i < data.size(); ++i) {
            xor_result ^= data[i];
        }
        return xor_result;
    }
    
    double computeGeometricMean() {
        double product = 1.0;
        for (size_t i = 0; i < data.size(); ++i) {
            product *= static_cast<double>(data[i]);
        }
        return pow(product, 1.0 / data.size());
    }
};

struct Point {
    double x, y;
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    
    double distanceFrom(const Point& other) const {
        double dx = x - other.x;
        double dy = y - other.y;
        return sqrt(dx*dx + dy*dy);
    }
};

int main() {
    // Initialize data
    std::vector<int> numbers = {3, 7, 11, 15, 19};
    DataProcessor processor(numbers);
    
    // Step 1: Compute XOR sum
    int xor_sum = processor.computeXORSum();
    
    // Step 2: Compute geometric mean
    double geometric_mean = processor.computeGeometricMean();
    
    // Step 3: Perform bit shifting
    int shifted_value = (xor_sum << 2) | (static_cast<int>(geometric_mean) >> 1);
    
    // Step 4: Create points and calculate distances
    Point p1(3.0, 4.0);
    Point p2(0.0, 0.0);
    double distance = p1.distanceFrom(p2);
    
    // Step 5: String manipulation
    std::string code = "COMPLEX";
    int char_sum = 0;
    for (char c : code) {
        char_sum += static_cast<int>(c);
    }
    
    // Step 6: Complex calculation combining all values
    double temp = pow(distance, 3) + sin(char_sum) * cos(shifted_value);
    int intermediate = static_cast<int>(temp) % 100;
    
    // Step 7: Final calculation
    int result = (intermediate & 0xF) * (shifted_value | 0x7) - static_cast<int>(geometric_mean);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}