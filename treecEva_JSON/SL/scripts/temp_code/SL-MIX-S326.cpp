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
    
    int computeWeightedSum() {
        int sum = 0;
        for (size_t i = 0; i < data.size(); ++i) {
            sum += data[i] * static_cast<int>(pow(-1, i));
        }
        return sum;
    }
    
    void transformData() {
        for (auto& val : data) {
            val = val ^ 0xF;
        }
    }
};

struct Point {
    double x, y;
    Point(double x = 0, double y = 0) : x(x), y(y) {}
    
    double distanceFrom(const Point& other) const {
        return sqrt(pow(x - other.x, 2) + pow(y - other.y, 2));
    }
    
    Point operator+(const Point& other) const {
        return Point(x + other.x, y + other.y);
    }
};

int main() {
    // Initialize data processor with values
    std::vector<int> initialValues = {5, 12, 7, 8, 3, 15};
    DataProcessor processor(initialValues);
    
    // Perform weighted sum before transformation
    int preTransformSum = processor.computeWeightedSum();
    
    // Transform the data
    processor.transformData();
    
    // Compute sum after transformation
    int postTransformSum = processor.computeWeightedSum();
    
    // Calculate difference between sums
    int diff = abs(postTransformSum - preTransformSum);
    
    // Work with points
    Point p1(3.0, 4.0);
    Point p2(0.0, 0.0);
    Point p3 = p1 + p2;
    
    double dist1 = p3.distanceFrom(p2);
    int roundedDist = static_cast<int>(round(dist1));
    
    // Bitwise operations
    int bitOpResult = (diff & 0xFF) | (roundedDist << 2);
    
    // Mathematical computation
    double angle = M_PI / 4;
    double sinVal = sin(angle);
    double cosVal = cos(angle);
    int trigProduct = static_cast<int>((sinVal * cosVal) * 1000);
    
    // Final complex calculation
    int final_result = ((bitOpResult ^ trigProduct) + (preTransformSum | postTransformSum)) % 1000;
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}