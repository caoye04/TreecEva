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
    
    int computeXOR() const {
        int res = 0;
        for(int val : data) res ^= val;
        return res;
    }
    
    double computeGeometricMean() const {
        double product = 1.0;
        for(int val : data) product *= val;
        return pow(product, 1.0/data.size());
    }
};

struct ComplexData {
    std::vector<std::vector<int>> matrix;
    std::string key;
    
    int trace() const {
        int sum = 0;
        for(size_t i=0; i<matrix.size() && i<matrix[i].size(); ++i)
            sum += matrix[i][i];
        return sum;
    }
};

int main() {
    // Initialize complex nested data structure
    ComplexData cd;
    cd.matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    cd.key = "SECRET_KEY";
    
    // Perform trace calculation
    int diagonalSum = cd.trace();
    
    // Bitwise manipulation sequence
    unsigned int a = 0xF0F0F0F0;
    unsigned int b = 0x0F0F0F0F;
    unsigned int c = (a & b) | ((a ^ b) << 4);
    
    // Mathematical transformations
    double x = log(static_cast<double>(diagonalSum));
    double y = sin(x) * cos(x);
    long long z = static_cast<long long>(exp(y) * 1000);
    
    // String processing
    std::string s = cd.key;
    int charSum = 0;
    for(char ch : s) charSum += static_cast<int>(ch);
    
    // Vector operations with custom class
    std::vector<int> primes = {2, 3, 5, 7, 11};
    DataProcessor processor(primes);
    int xorValue = processor.computeXOR();
    double geoMean = processor.computeGeometricMean();
    
    // Final computation combining all results
    long long intermediate = (z * xorValue) + static_cast<long long>(geoMean * 100);
    int result = (intermediate & c) % 10000;
    
    // Adjust based on string processing
    result = result ^ (charSum & 0xFF);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}