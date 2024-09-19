# Recursive Task Scheduler Implementation with Time and Space Complexity Analysis

def schedule_tasks(task_hierarchy):
    """
    Recursive function to schedule tasks based on their priorities and dependencies.
    
    Parameters:
    - task_hierarchy: A dictionary representing the task and its subtasks.

    Returns:
    - A list of tasks in the order they should be scheduled.
    """
    global recursive_calls
    global total_tasks

    # Count each task processed
    total_tasks += 1

    # Base case: If no subtasks, schedule this task and return
    if not task_hierarchy.get('subtasks', []):
        return [task_hierarchy]

    # Schedule parent task first
    scheduled_tasks = [task_hierarchy]

    # Sort subtasks by priority (higher priority tasks first)
    subtasks = sorted(task_hierarchy['subtasks'], key=lambda x: x.get('priority', 0), reverse=True)

    # Recursively schedule subtasks
    for subtask in subtasks:
        recursive_calls += 1
        scheduled_tasks.extend(schedule_tasks(subtask))

    return scheduled_tasks


def analyze_complexity():
    """
    Analyze the total recursive calls and tasks processed, 
    serving as a proxy for time complexity.
    
    Returns:
    A dictionary with the counts of recursive calls and total tasks.
    """
    return {
        'total_recursive_calls': recursive_calls,
        'total_tasks_processed': total_tasks,
        'time_complexity': f'O({total_tasks} log {total_tasks})',
        'space_complexity': f'O({total_tasks})'
    }

# Initialize global counters for tracking recursion depth and task count
recursive_calls = 0
total_tasks = 0

# Testing the Task Scheduler Function
if __name__ == "__main__":
    task_hierarchy = {
        'id': 1,
        'name': 'Main Task',
        'priority': 1,
        'subtasks': [
            {
                'id': 2,
                'name': 'Subtask 1',
                'priority': 3,
                'subtasks': []
            },
            {
                'id': 3,
                'name': 'Subtask 2',
                'priority': 2,
                'subtasks': [
                    {
                        'id': 4,
                        'name': 'Subtask 2.1',
                        'priority': 1,
                        'subtasks': []
                    }
                ]
            }
        ]
    }

    # Schedule tasks and display the order
    scheduled = schedule_tasks(task_hierarchy)
    for task in scheduled:
        print(f"Task ID: {task['id']}, Name: {task['name']}, Priority: {task.get('priority', 'N/A')}")

    # Analyze and display time and space complexity
    complexity_analysis = analyze_complexity()
    print("\nComplexity Analysis:")
    for key, value in complexity_analysis.items():
        print(f"{key}: {value}")
