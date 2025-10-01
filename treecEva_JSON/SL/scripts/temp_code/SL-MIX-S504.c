#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 10

struct Node {
    int value;
    struct Node* next;
};

struct DataContainer {
    int matrix[3][3];
    double vector[4];
    struct Node* head;
};

int bitwise_transform(int a, int b) {
    return (a << 2) ^ (b >> 1) & 0xFF;
}

double calculate_norm(double* vec, int size) {
    double sum = 0;
    for (int i = 0; i < size; i++) {
        sum += vec[i] * vec[i];
    }
    return sqrt(sum);
}

int determinant_3x3(int matrix[3][3]) {
    return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
           matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
           matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
}

int main() {
    struct DataContainer container;
    
    // Initialize matrix with fibonacci sequence values
    int fib[9] = {1, 1, 2, 3, 5, 8, 13, 21, 34};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            container.matrix[i][j] = fib[i * 3 + j];
        }
    }
    
    // Initialize vector with trigonometric values
    container.vector[0] = sin(M_PI / 6);   // 0.5
    container.vector[1] = cos(M_PI / 3);   // 0.5
    container.vector[2] = tan(M_PI / 4);   // 1.0
    container.vector[3] = atan(1.0) * 4;   // PI
    
    // Create linked list with prime numbers
    struct Node nodes[5];
    int primes[5] = {2, 3, 5, 7, 11};
    
    for (int i = 0; i < 5; i++) {
        nodes[i].value = primes[i];
        if (i < 4) {
            nodes[i].next = &nodes[i+1];
        } else {
            nodes[i].next = NULL;
        }
    }
    container.head = &nodes[0];
    
    // Complex calculation sequence
    int det = determinant_3x3(container.matrix);
    double norm = calculate_norm(container.vector, 4);
    
    // Traverse linked list and perform operations
    struct Node* current = container.head;
    int list_product = 1;
    int list_sum = 0;
    
    while (current != NULL) {
        list_product *= current->value;
        list_sum += current->value;
        current = current->next;
    }
    
    // Perform bitwise transformations
    int bitwise_result = bitwise_transform(det, list_sum);
    
    // Apply mathematical transformations
    double transformed_norm = pow(norm, 3) - log(norm + 1);
    
    // Calculate final result through complex formula
    int intermediate = (int)(transformed_norm * 100) % 256;
    int target_result = bitwise_result ^ (intermediate << 1) - list_product % 100;
    
    /* Execution point Y */
    
    printf("Result: %d\n", target_result);
    
    return 0;
}