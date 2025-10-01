#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_VAL 1000

struct DataPoint {
    int x;
    double y;
    struct DataPoint* next;
};

double compute_power_log(double base, int exp) {
    if (exp == 0) return 1.0;
    double powered = pow(base, exp);
    return log(powered + 1.0); // Adding 1 to avoid log(0)
}

int main() {
    int values[5] = {3, 7, 2, 9, 4};
    double results[5];
    
    struct DataPoint points[5];
    struct DataPoint* head = &points[0];
    
    // Initialize linked list nodes
    for(int i=0; i<5; i++) {
        points[i].x = values[i];
        points[i].y = sqrt((double)values[i]);
        if(i < 4) {
            points[i].next = &points[i+1];
        } else {
            points[i].next = NULL;
        }
    }
    
    // Process each node
    struct DataPoint* current = head;
    int index = 0;
    while(current != NULL) {
        double temp = compute_power_log((double)current->x, 3);
        results[index] = temp * sin(temp);
        current = current->next;
        index++;
    }
    
    // Perform reduction operation with bit shifting
    double accumulator = 0.0;
    for(int j=0; j<5; j++) {
        int shifted = (int)(results[j]) << (j % 3);
        accumulator += shifted * cos(results[j]);
    }
    
    // Apply final transformation
    long long intermediate = (long long)(accumulator);
    long long mask = 0xF0F0F0F0LL;
    long long masked_value = intermediate & mask;
    
    int final_result = (int)((masked_value >> 4) ^ (masked_value & 0xFF));
    
    printf("Result: %d\n", final_result);
    return 0;
}