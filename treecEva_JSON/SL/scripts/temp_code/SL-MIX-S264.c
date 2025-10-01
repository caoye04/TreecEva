#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

int main() {
    // Initialize complex data structures
    int matrix[3][3] = {{2, 7, 1}, {8, 4, 3}, {5, 9, 6}};
    char text[] = "COMPUTATION";
    double values[4] = {3.14159, 2.71828, 1.41421, 0.57721};
    
    // Variable declarations
    int i, j, sum = 0, product = 1;
    double accumulator = 0.0;
    int indices[3];
    int temp_matrix[3][3];
    int result;
    
    // Step 1: Process matrix diagonals
    for(i = 0; i < 3; i++) {
        sum += matrix[i][i];
        product *= matrix[i][2-i];
    }
    
    // Step 2: Manipulate array values using mathematical operations
    for(i = 0; i < 4; i++) {
        accumulator += sin(values[i]) * cos(values[i]);
    }
    
    // Step 3: String processing with bitwise operations
    int char_sum = 0;
    for(i = 0; i < strlen(text); i++) {
        char_sum ^= (text[i] & 0x1F);
    }
    
    // Step 4: Complex conditional assignment with nested operations
    if((sum > product) && (accumulator > 0)) {
        for(i = 0; i < 3; i++) {
            indices[i] = (int)(matrix[i][0] * pow(-1, i) + ceil(accumulator));
        }
    } else {
        for(i = 0; i < 3; i++) {
            indices[i] = (int)(matrix[0][i] * fabs(accumulator) + floor(sum / 2.0));
        }
    }
    
    // Step 5: Matrix transformation using indices
    for(i = 0; i < 3; i++) {
        for(j = 0; j < 3; j++) {
            temp_matrix[i][j] = matrix[j][i] ^ (indices[i] & indices[j]);
        }
    }
    
    // Step 6: Final calculation combining all processed data
    result = 0;
    for(i = 0; i < 3; i++) {
        result += (temp_matrix[i][i] << (i+1)) | (char_sum >> i);
    }
    
    // Apply final transformation
    result = (result & 0xFF) ^ ((int)(accumulator * 100) % 32);
    
    printf("Result: %d\n", result);
    return 0;
}