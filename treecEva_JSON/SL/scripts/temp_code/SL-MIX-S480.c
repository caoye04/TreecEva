#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ROWS 4
#define COLS 5

int main() {
    double **matrix = (double **)malloc(ROWS * sizeof(double *));
    for (int i = 0; i < ROWS; i++) {
        matrix[i] = (double *)malloc(COLS * sizeof(double));
    }
    
    // Initialize matrix with values
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            matrix[i][j] = pow(-1, i) * (i * COLS + j + 1) * M_PI;
        }
    }
    
    // Perform row operations
    for (int i = 0; i < ROWS; i++) {
        double row_sum = 0;
        for (int j = 0; j < COLS; j++) {
            row_sum += matrix[i][j];
        }
        for (int j = 0; j < COLS; j++) {
            matrix[i][j] = matrix[i][j] / row_sum * 100;
        }
    }
    
    // Apply trigonometric transformation
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            matrix[i][j] = sin(matrix[i][j]) * cos(matrix[i][j] * 0.5);
        }
    }
    
    // Calculate checksum
    double checksum = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            checksum += matrix[i][j] * (i + 1) * (j + 1);
        }
    }
    
    // Apply final transformation
    checksum = floor(checksum * 1000) / 1000;
    
    // Free allocated memory
    for (int i = 0; i < ROWS; i++) {
        free(matrix[i]);
    }
    free(matrix);
    
    printf("Result: %.3f\n", checksum);
    return 0;
}