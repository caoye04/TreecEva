#define M_PI 3.14159265358979323846
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

struct ComplexData {
    struct DataPoint points[3];
    int count;
    double aggregate;
};

int process_data(struct ComplexData* data) {
    int i;
    double sum = 0;
    for (i = 0; i < data->count; i++) {
        double val = pow(data->points[i].x, 2) + sqrt(fabs(data->points[i].y));
        sum += val;
    }
    data->aggregate = sum;
    return (int)(sum / data->count);
}

int main() {
    struct ComplexData dataset;
    dataset.count = 3;
    
    dataset.points[0].x = 4;
    dataset.points[0].y = -9.0;
    strcpy(dataset.points[0].label, "PointA");
    
    dataset.points[1].x = -3;
    dataset.points[1].y = 16.0;
    strcpy(dataset.points[1].label, "PointB");
    
    dataset.points[2].x = 5;
    dataset.points[2].y = -25.0;
    strcpy(dataset.points[2].label, "PointC");
    
    int intermediate = process_data(&dataset);
    
    char buffer[MAX_LEN];
    snprintf(buffer, MAX_LEN, "Aggr: %.2f", dataset.aggregate);
    
    int len = strlen(buffer);
    int bit_mask = 0xF0;
    int shifted = (len << 2) & bit_mask;
    
    double trig_val = sin(M_PI / 6); // 30 degrees
    int trig_scaled = (int)(trig_val * 1000);
    
    int final_result = ((intermediate ^ trig_scaled) + shifted) % 256;
    
    printf("Result: %d\n", final_result);
    return 0;
}