#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class ComplexDataProcessor {
private:
    std::vector<std::vector<int>> matrix;
    std::string key;

public:
    ComplexDataProcessor(int size) {
        matrix.resize(size, std::vector<int>(size, 0));
        key = "PROCESSING_KEY_" + std::to_string(size);
    }

    void populateMatrix() {
        int value = 1;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                matrix[i][j] = value++;
            }
        }
    }

    int calculateDiagonalSum() {
        int sum = 0;
        for (int i = 0; i < matrix.size(); i++) {
            sum += matrix[i][i];
        }
        return sum;
    }

    std::string getKey() {
        return key;
    }

    int getMatrixElement(int row, int col) {
        if (row >= 0 && row < matrix.size() && col >= 0 && col < matrix[0].size()) {
            return matrix[row][col];
        }
        return -1;
    }
};

struct DataBundle {
    int x;
    int y;
    double z;
    
    DataBundle(int a, int b, double c) : x(a), y(b), z(c) {}
};

int complexCalculation(int a, int b, double c) {
    return static_cast<int>(std::pow(a, 2) + std::sqrt(b) + std::floor(c));
}

int main() {
    ComplexDataProcessor processor(5);
    processor.populateMatrix();
    
    int diag_sum = processor.calculateDiagonalSum();
    
    DataBundle bundle(diag_sum, 64, 12.75);
    
    int step1 = complexCalculation(bundle.x, bundle.y, bundle.z);
    
    int arr[4] = {step1, step1/2, step1/3, step1/4};
    
    int xor_result = 0;
    for (int i = 0; i < 4; i++) {
        xor_result ^= arr[i];
    }
    
    std::string key = processor.getKey();
    int key_length = key.length();
    
    int matrix_val = processor.getMatrixElement(2, 3);
    
    double trig_result = std::sin(M_PI/6) * 100; // sin(30 degrees) * 100
    
    int final_result = ((xor_result & 0xFF) + key_length) * matrix_val + static_cast<int>(trig_result);
    
    std::cout << "Result: " << final_result << std::endl;
    
    return 0;
}