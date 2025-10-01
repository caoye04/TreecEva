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
    
    int computeXOR() const {
        int result = 0;
        for (size_t i = 0; i < data.size(); ++i) {
            result ^= data[i];
        }
        return result;
    }
    
    double computeGeometricMean() const {
        if (data.empty()) return 0;
        long long product = 1;
        for (int val : data) {
            product *= val;
        }
        return pow(static_cast<double>(product), 1.0 / data.size());
    }
};

struct ComplexNumber {
    double real;
    double imag;
    
    ComplexNumber(double r = 0, double i = 0) : real(r), imag(i) {}
    
    ComplexNumber operator+(const ComplexNumber& other) const {
        return ComplexNumber(real + other.real, imag + other.imag);
    }
    
    double magnitude() const {
        return sqrt(real*real + imag*imag);
    }
};

int main() {
    // Initialize data
    std::vector<int> values = {3, 7, 2, 8, 5};
    DataProcessor processor(values);
    
    // Step 1: Compute XOR of all elements
    int xor_result = processor.computeXOR();
    
    // Step 2: Perform bit shifting operations
    int shifted_xor = (xor_result << 2) | (xor_result >> 1);
    
    // Step 3: Mathematical computation using trigonometric functions
    double angle_rad = M_PI / 4.0;
    double sin_val = sin(angle_rad);
    double cos_val = cos(angle_rad);
    double trig_result = round((sin_val * cos_val * 1000));
    
    // Step 4: Work with complex numbers
    ComplexNumber c1(3.0, 4.0);
    ComplexNumber c2(1.0, 2.0);
    ComplexNumber c_sum = c1 + c2;
    double magnitude = c_sum.magnitude();
    
    // Step 5: String manipulation
    std::string prefix = "RESULT_";
    std::string suffix = std::to_string(static_cast<int>(magnitude));
    std::string combined = prefix + suffix;
    int string_length = static_cast<int>(combined.length());
    
    // Step 6: Final computation combining all results
    int intermediate = static_cast<int>(trig_result) ^ string_length;
    double geometric_mean = processor.computeGeometricMean();
    int final_result = (intermediate & 0xFF) + static_cast<int>(geometric_mean) + shifted_xor;
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}