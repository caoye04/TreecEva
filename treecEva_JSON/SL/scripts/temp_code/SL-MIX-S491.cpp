#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
private:
    std::vector<int> data;
    int multiplier;

public:
    DataProcessor(std::vector<int> d, int m) : data(d), multiplier(m) {}
    
    int process() {
        int sum = 0;
        for (size_t i = 0; i < data.size(); ++i) {
            if (i % 2 == 0) {
                sum += data[i] * multiplier;
            } else {
                sum -= static_cast<int>(std::pow(data[i], 2));
            }
        }
        return sum;
    }
};

struct ComplexStruct {
    int x;
    double y;
    std::string z;
    
    ComplexStruct(int a, double b, const std::string& c) : x(a), y(b), z(c) {}
    
    bool operator>(const ComplexStruct& other) const {
        return (x * y) > (other.x * other.y);
    }
};

int main() {
    std::vector<int> numbers = {3, 4, 5, 6, 7};
    DataProcessor processor(numbers, 2);
    int intermediate_result = processor.process();
    
    ComplexStruct s1(2, 3.5, "first");
    ComplexStruct s2(3, 2.0, "second");
    
    bool comparison_result = s1 > s2;
    
    int bit_result = (intermediate_result & 0xF) | (static_cast<int>(s1.y) << 2);
    
    double trig_result = std::sin(M_PI / 6) * 100; // sin(30 degrees)
    
    std::string text = "Hello" + std::to_string(static_cast<int>(trig_result));
    
    int final_result = 0;
    if (comparison_result) {
        final_result = bit_result ^ static_cast<int>(text.length());
    } else {
        final_result = bit_result + static_cast<int>(std::ceil(trig_result));
    }
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}