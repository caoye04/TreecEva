#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct DataPoint {
    int x;
    double y;
    char label[20];
};

typedef struct {
    struct DataPoint points[5];
    int count;
} DataSet;

int complex_operation(int a, int b) {
    return (a * b) + (a ^ b) - (a << 1);
}

double compute_average(DataSet* ds) {
    double sum = 0;
    for (int i = 0; i < ds->count; i++) {
        sum += ds->points[i].y;
    }
    return sum / ds->count;
}

int main() {
    DataSet dataset;
    dataset.count = 4;
    
    // Initialize data points
    dataset.points[0].x = 10;
    dataset.points[0].y = 3.5;
    strcpy(dataset.points[0].label, "PointA");
    
    dataset.points[1].x = 20;
    dataset.points[1].y = 7.2;
    strcpy(dataset.points[1].label, "PointB");
    
    dataset.points[2].x = 15;
    dataset.points[2].y = 4.8;
    strcpy(dataset.points[2].label, "PointC");
    
    dataset.points[3].x = 25;
    dataset.points[3].y = 9.1;
    strcpy(dataset.points[3].label, "PointD");
    
    // Perform operations
    int intermediate = complex_operation(dataset.points[1].x, dataset.points[2].x);
    
    // Bitwise manipulation
    int mask = 0xF0;
    intermediate = (intermediate & mask) >> 2;
    
    // Mathematical operations
    double avg = compute_average(&dataset);
    double trig_result = sin(avg) * cos(avg);
    
    // String operation effect
    int label_length = strlen(dataset.points[0].label);
    
    // Final calculation
    int final_result = (int)(trig_result * 1000) + intermediate + label_length;
    
    printf("Result: %d\n", final_result);
    return 0;
}