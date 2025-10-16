#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>

class Matrix {
private:
    std::vector<std::vector<int>> data;
    size_t rows, cols;

public:
    Matrix(size_t r, size_t c) : rows(r), cols(c) {
        data.resize(rows, std::vector<int>(cols, 0));
    }
    
    int& operator()(size_t i, size_t j) {
        return data[i][j];
    }
    
    const int& operator()(size_t i, size_t j) const {
        return data[i][j];
    }
    
    Matrix operator+(const Matrix& other) const {
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i)
            for (size_t j = 0; j < cols; ++j)
                result(i,j) = data[i][j] + other(i,j);
        return result;
    }
    
    ~Matrix() = default; // RAII: automatic cleanup
};

int main() {
    Matrix grid(3, 3);
    int checksum = 0;
    bool flagA = true, flagB = false;
    
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if((i > 0 && flagA) || (!flagB && j < 2)) {
                grid(i,j) = (i+1)*(j+1);
            } else {
                grid(i,j) = -1;
            }
        }
    }
    
    Matrix identity(3, 3);
    for(int i=0; i<3; i++) identity(i,i) = 1;
    
    Matrix transformed = grid + identity;
    
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if(transformed(i,j) > 0 && (i != j || flagA)) {
                checksum += transformed(i,j);
            }
        }
    }
    
    std::cout << "Result: " << checksum << std::endl;
    return 0;
}