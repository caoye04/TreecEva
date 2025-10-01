#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#define M_PI 3.14159265358979323846

struct DataPoint {
    double x, y;
    int id;
};

double complexFunction(double a, double b, int n) {
    double sum = 0.0;
    for (int i = 1; i <= n; ++i) {
        sum += pow(a, (double)i/n) * sin(b * M_PI * i / n);
    }
    return sum / n;
}

int main() {
    std::vector<std::vector<DataPoint>> grid(3, std::vector<DataPoint>(3));
    
    // Initialize grid with values
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            grid[i][j] = {static_cast<double>(i+1), static_cast<double>(j+1), i*3+j};
        }
    }
    
    double accumulator = 0.0;
    int counter = 0;
    
    for (auto& row : grid) {
        for (auto& point : row) {
            if ((point.id % 2 == 0) && (point.x + point.y > 3.0)) {
                accumulator += complexFunction(point.x, point.y, point.id + 1);
                counter++;
            } else if (point.id % 2 != 0) {
                accumulator -= sqrt(point.x * point.y) * log(point.id + 2);
            }
        }
    }
    
    int bitPattern = 0b10101101;
    int mask = 0b11110000;
    int maskedValue = (bitPattern & mask) >> 2;
    
    double trigResult = sin(accumulator) + cos(maskedValue * M_PI / 16);
    
    std::vector<int> sequence = {3, 1, 4, 1, 5, 9, 2, 6};
    int seqProduct = 1;
    for (size_t i = 0; i < sequence.size(); ++i) {
        if (i % 2 == 0) {
            seqProduct *= sequence[i] ^ (maskedValue & 0xF);
        } else {
            seqProduct += sequence[i] | (counter << 1);
        }
    }
    
    double result = trunc((trigResult * seqProduct + accumulator) * 1000.0) / 1000.0;
    
    // QUERY_POINT
    
    std::cout << "Result: " << result << std::endl;
    
    return 0;
}