#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct Node {
    int speed;
    struct Node* next;
} Node;

void push(Node** head, int speed) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->speed = speed;
    newNode->next = *head;
    *head = newNode;
}

int pop(Node** head) {
    if (*head == NULL) return -1;
    Node* temp = *head;
    int speed = temp->speed;
    *head = (*head)->next;
    free(temp);
    return speed;
}

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void buildMaxHeap(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
}

int main() {
    Node* vehicle_queue = NULL;
    
    // Simulate vehicle speeds using linked list
    push(&vehicle_queue, 65);
    push(&vehicle_queue, 72);
    push(&vehicle_queue, 58);
    push(&vehicle_queue, 80);
    push(&vehicle_queue, 67);
    
    int speeds[5];
    int count = 0;
    
    // Extract speeds from queue
    while (vehicle_queue != NULL && count < 5) {
        speeds[count++] = pop(&vehicle_queue);
    }
    
    // Build max heap
    buildMaxHeap(speeds, count);
    
    // Extract top 3 speeds
    int top_speeds[3];
    for (int i = 0; i < 3; i++) {
        top_speeds[i] = speeds[0];
        speeds[0] = speeds[count - 1 - i];
        heapify(speeds, count - 1 - i, 0);
    }
    
    // Calculate mean
    double mean = (top_speeds[0] + top_speeds[1] + top_speeds[2]) / 3.0;
    
    // Calculate variance
    double variance = ((top_speeds[0] - mean) * (top_speeds[0] - mean) +
                      (top_speeds[1] - mean) * (top_speeds[1] - mean) +
                      (top_speeds[2] - mean) * (top_speeds[2] - mean)) / 3.0;
    
    int speed_variance = (int)round(variance);
    printf("Result: %d\n", speed_variance);
    
    return 0;
}