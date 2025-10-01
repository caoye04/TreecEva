#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>

class DataProcessor {
private:
    std::vector<std::vector<int>> matrix;
    int size;

public:
    DataProcessor(int n) : size(n) {
        matrix.resize(n, std::vector<int>(n, 0));
        // Initialize matrix with specific pattern
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = (i + 1) * (j + 1) + (i ^ j);
            }
        }
    }
    
    int getDiagonalProduct() {
        int product = 1;
        for (int i = 0; i < size; i++) {
            product *= matrix[i][i];
        }
        return product;
    }
    
    int getBitwiseSum() {
        int sum = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                sum += (matrix[i][j] & 0xF) | ((matrix[i][j] >> 4) & 0xF);
            }
        }
        return sum;
    }
    
    double getGeometricMean() {
        double product = 1.0;
        int count = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (matrix[i][j] > 0) {
                    product *= matrix[i][j];
                    count++;
                }
            }
        }
        return pow(product, 1.0/count);
    }
};

int complexFunction(int x, int y) {
    if (x <= 0 || y <= 0) return 0;
    int result = 0;
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            result += (i * j) ^ (i | j);
        }
    }
    return result;
}

int main() {
    DataProcessor processor(4);
    
    int diagonal = processor.getDiagonalProduct();
    int bitwise = processor.getBitwiseSum();
    double geometric = processor.getGeometricMean();
    
    int funcResult = complexFunction(diagonal % 10, static_cast<int>(geometric) % 7);
    
    // Perform bit rotation
    unsigned int rotated = (funcResult << 5) | (funcResult >> (32 - 5));
    
    // Apply mathematical transformation
    double transformed = sqrt(abs(static_cast<double>(rotated))) * sin(geometric);
    
    // Final calculation sequence
    int result = 0;
    for (int i = 1; i <= 6; i++) {
        result += static_cast<int>(pow(transformed, 1.0/i)) ^ (i * bitwise);
    }
    
    // TARGET_VARIABLE
    result = (result & 0xFF) ^ (diagonal >> 2);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}