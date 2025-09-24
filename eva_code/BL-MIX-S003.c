#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Task
{
    int id;
    int priority;
    int estimated_time;
    int *dependencies;
    int dep_count;
    int remaining_time;
    struct Task *next;
} Task;

typedef struct
{
    Task **priority_queues;
    int *queue_sizes;
    int max_priority;
    int *resource_pool;
    int resource_count;
    int completed_tasks;
    int active_tasks;
    int total_time;
} Scheduler;

Scheduler *init_scheduler(int max_priority, int resources)
{
    Scheduler *s = malloc(sizeof(Scheduler));
    s->priority_queues = malloc(max_priority * sizeof(Task *));
    s->queue_sizes = calloc(max_priority, sizeof(int));
    s->resource_pool = malloc(resources * sizeof(int));

    for (int i = 0; i < max_priority; i++)
    {
        s->priority_queues[i] = NULL;
    }
    for (int i = 0; i < resources; i++)
    {
        s->resource_pool[i] = 0; // 0 = free, 1 = busy
    }

    s->max_priority = max_priority;
    s->resource_count = resources;
    s->completed_tasks = 0;
    s->active_tasks = 0;
    s->total_time = 0;
    return s;
}

int check_dependencies(Task *task, int *completed_task_ids, int completed_count)
{
    for (int i = 0; i < task->dep_count; i++)
    {
        int found = 0;
        for (int j = 0; j < completed_count; j++)
        {
            if (completed_task_ids[j] == task->dependencies[i])
            {
                found = 1;
                break;
            }
        }
        if (!found)
            return 0;
    }
    return 1;
}

int allocate_resource(Scheduler *s)
{
    for (int i = 0; i < s->resource_count; i++)
    {
        if (s->resource_pool[i] == 0)
        {
            s->resource_pool[i] = 1;
            return i;
        }
    }
    return -1;
}

void add_task_to_queue(Scheduler *s, Task *task)
{
    int priority_idx = task->priority - 1;
    if (priority_idx >= s->max_priority)
        priority_idx = s->max_priority - 1;

    task->next = s->priority_queues[priority_idx];
    s->priority_queues[priority_idx] = task;
    s->queue_sizes[priority_idx]++;
}

Task *get_highest_priority_task(Scheduler *s, int *completed_ids, int completed_count)
{
    for (int p = s->max_priority - 1; p >= 0; p--)
    {
        Task *current = s->priority_queues[p];
        Task *prev = NULL;

        while (current != NULL)
        {
            if (check_dependencies(current, completed_ids, completed_count))
            {
                if (prev == NULL)
                {
                    s->priority_queues[p] = current->next;
                }
                else
                {
                    prev->next = current->next;
                }
                s->queue_sizes[p]--;
                current->next = NULL;
                return current;
            }
            prev = current;
            current = current->next;
        }
    }
    return NULL;
}

int simulate_complex_scheduling(int *priorities, int task_count)
{
    Scheduler *s = init_scheduler(5, 3);
    Task **tasks = malloc(task_count * sizeof(Task *));
    int *completed_ids = malloc(task_count * sizeof(int));
    Task **running_tasks = malloc(s->resource_count * sizeof(Task *));
    int *resource_timers = malloc(s->resource_count * sizeof(int));

    // Initialize tasks with complex dependencies
    for (int i = 0; i < task_count; i++)
    {
        tasks[i] = malloc(sizeof(Task));
        tasks[i]->id = i;
        tasks[i]->priority = priorities[i];
        tasks[i]->estimated_time = (priorities[i] * 2) + (i % 3) + 1;
        tasks[i]->remaining_time = tasks[i]->estimated_time;

        // Create circular dependencies pattern
        if (i > 0)
        {
            tasks[i]->dependencies = malloc(sizeof(int));
            tasks[i]->dependencies[0] = (i - 1) % task_count;
            tasks[i]->dep_count = 1;
        }
        else
        {
            tasks[i]->dependencies = NULL;
            tasks[i]->dep_count = 0;
        }

        add_task_to_queue(s, tasks[i]);
    }

    // Initialize running task tracking
    for (int i = 0; i < s->resource_count; i++)
    {
        running_tasks[i] = NULL;
        resource_timers[i] = 0;
    }

    int simulation_time = 0;
    int max_simulation_time = 100;

    while (s->completed_tasks < task_count && simulation_time < max_simulation_time)
    {
        simulation_time++;

        // Process currently running tasks
        for (int r = 0; r < s->resource_count; r++)
        {
            if (running_tasks[r] != NULL)
            {
                running_tasks[r]->remaining_time--;
                resource_timers[r]++;

                if (running_tasks[r]->remaining_time <= 0)
                {
                    // Task completed
                    completed_ids[s->completed_tasks] = running_tasks[r]->id;
                    s->completed_tasks++;
                    s->resource_pool[r] = 0; // Free resource
                    running_tasks[r] = NULL;
                    resource_timers[r] = 0;
                    s->active_tasks--;
                }
            }
        }

        // Try to schedule new tasks
        for (int attempt = 0; attempt < s->resource_count; attempt++)
        {
            int resource_id = allocate_resource(s);
            if (resource_id == -1)
                break;

            Task *next_task = get_highest_priority_task(s, completed_ids, s->completed_tasks);
            if (next_task == NULL)
            {
                s->resource_pool[resource_id] = 0; // Free unused resource
                break;
            }

            running_tasks[resource_id] = next_task;
            s->active_tasks++;
        }

        // Dynamic priority adjustment based on waiting time
        if (simulation_time % 5 == 0)
        {
            for (int p = 0; p < s->max_priority - 1; p++)
            {
                Task *current = s->priority_queues[p];
                if (current != NULL && s->queue_sizes[p] > 2)
                {
                    // Promote one task to higher priority
                    s->priority_queues[p] = current->next;
                    s->queue_sizes[p]--;
                    current->next = s->priority_queues[p + 1];
                    s->priority_queues[p + 1] = current;
                    s->queue_sizes[p + 1]++;
                    break;
                }
            }
        }
    }

    return s->completed_tasks;
}

int main()
{
    int priorities[] = {3, 1, 4, 1, 5, 2};
    int result = simulate_complex_scheduling(priorities, 6);
    printf("Completed tasks: %d\n", result);
    return 0;
}