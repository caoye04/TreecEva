#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class DataProcessor {
private:
    std::vector<int> data;
    int base;

public:
    DataProcessor(int b) : base(b) {}
    
    void addData(int value) {
        data.push_back(value);
    }
    
    int process() {
        int sum = 0;
        for (int i = 0; i < data.size(); i++) {
            sum += data[i] * pow(base, i);
        }
        return sum;
    }
};

struct Complex {
    double real;
    double imag;
    
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    
    Complex operator*(const Complex& other) const {
        return Complex(real * other.real - imag * other.imag,
                      real * other.imag + imag * other.real);
    }
    
    double magnitude() const {
        return sqrt(real*real + imag*imag);
    }
};

int main() {
    DataProcessor processor(3);
    processor.addData(2);
    processor.addData(5);
    processor.addData(1);
    
    int partial_result = processor.process();
    
    // Create a 3x3 matrix with values
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    
    // Calculate determinant of 3x3 matrix
    int det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) -
              matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) +
              matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]);
    
    // Perform bitwise operations
    int bitwise_result = (partial_result & 0xF) | (det << 2);
    
    // Work with complex numbers
    Complex c1(3, 4);
    Complex c2(1, 2);
    Complex c3 = c1 * c2;
    double magnitude = c3.magnitude();
    
    // String manipulation
    std::string text = "COMPUTATION";
    int char_sum = 0;
    for (char c : text) {
        char_sum += static_cast<int>(c);
    }
    
    // Final calculation
    int result = static_cast<int>(
        (bitwise_result ^ static_cast<int>(magnitude)) + 
        (char_sum % 100) - det
    );
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}