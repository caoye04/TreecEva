#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

class DataProcessor {
private:
    std::vector<std::vector<int>> matrix;
    std::string key;

public:
    DataProcessor(const std::vector<std::vector<int>>& m, const std::string& k) : matrix(m), key(k) {}
    
    int computeChecksum() {
        int sum = 0;
        for (const auto& row : matrix) {
            for (int val : row) {
                sum += val * static_cast<int>(key[val % key.length()]);
            }
        }
        return sum;
    }
    
    std::vector<int> getColumnSums() {
        std::vector<int> colSums(matrix[0].size(), 0);
        for (const auto& row : matrix) {
            for (size_t i = 0; i < row.size(); ++i) {
                colSums[i] += row[i];
            }
        }
        return colSums;
    }
};

struct ComplexData {
    std::vector<int> values;
    double factor;
    bool flag;
    
    ComplexData(std::vector<int> v, double f, bool fl) : values(v), factor(f), flag(fl) {}
    
    int transformedSum() {
        int result = 0;
        for (int val : values) {
            if (flag) {
                result += static_cast<int>(std::pow(val, factor));
            } else {
                result += static_cast<int>(std::log(val + 1) * factor);
            }
        }
        return result;
    }
};

int main() {
    // Initialize data structures
    std::vector<std::vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    std::string key = "SECRET_KEY";
    DataProcessor processor(matrix, key);
    
    // Perform checksum computation
    int checksum = processor.computeChecksum();
    
    // Get column sums
    std::vector<int> colSums = processor.getColumnSums();
    
    // Create complex data object
    ComplexData data(colSums, 1.5, checksum % 2 == 0);
    
    // Perform transformation
    int transformed = data.transformedSum();
    
    // Bitwise operations
    int bitwise_result = (checksum & 0xFF) ^ (transformed >> 2);
    
    // Final calculation
    int final_result = static_cast<int>(std::sqrt(bitwise_result * checksum)) + (transformed % 7);
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}