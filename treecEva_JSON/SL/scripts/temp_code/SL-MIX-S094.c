#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define NUM_STATES 4
#define NUM_COMMANDS 5

typedef enum { STATE_IDLE, STATE_PROCESSING, STATE_PAUSED, STATE_ERROR } state_t;
typedef struct {
    state_t current_state;
    int *action_list;
    int action_count;
} state_info_t;

// Transition table: [current_state][command] -> next_state
state_t transition_table[NUM_STATES][NUM_COMMANDS] = {
    // CMD0  CMD1  CMD2  CMD3  CMD4
    {   1,    0,    2,    3,    0   },  // STATE_IDLE
    {   1,    2,    1,    3,    0   },  // STATE_PROCESSING
    {   0,    1,    2,    2,    3   },  // STATE_PAUSED
    {   3,    3,    3,    3,    3   }   // STATE_ERROR
};

// Action lists for each state
int actions_idle[] = {10, 20, 30, 40, 50};
int actions_processing[] = {15, 25, 35};
int actions_paused[] = {12, 22, 32, 42};
int actions_error[] = {99};

state_info_t states[NUM_STATES] = {
    {STATE_IDLE,       actions_idle,       5},
    {STATE_PROCESSING, actions_processing, 3},
    {STATE_PAUSED,     actions_paused,     4},
    {STATE_ERROR,      actions_error,      1}
};

int binary_search(int *arr, int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    state_t current_state = STATE_IDLE;
    int commands[] = {2, 1, 3, 0, 4};
    int cmd_count = sizeof(commands)/sizeof(commands[0]);
    
    // Process commands through state machine
    for (int i = 0; i < cmd_count; i++) {
        int cmd = commands[i];
        state_t next_state = *(*(transition_table + current_state) + cmd);
        current_state = next_state;
    }
    
    // Get action list for final state
    state_info_t *final_state_info = states + current_state;
    int *action_ptr = final_state_info->action_list;
    int action_size = final_state_info->action_count;
    
    // Perform binary search for value 35
    int search_result = binary_search(action_ptr, action_size, 35);
    
    // Calculate final action code
    int final_action_code = (search_result >= 0) ? 
        *(action_ptr + search_result) : 
        *(action_ptr + (action_size - 1));
    
    printf("Result: %d\n", final_action_code);
    return 0;
}