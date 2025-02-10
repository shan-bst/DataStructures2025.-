# Example 2: Using Queue for Task Scheduling
class TaskScheduler:
    def __init__(self):
        self.tasks = deque()
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def process_task(self):
        return self.tasks.popleft() if self.tasks else "No tasks to process"
    
    def display_tasks(self):
        return list(self.tasks)

# Demonstrating Task Scheduler
scheduler = TaskScheduler()
scheduler.add_task("Process Data")
scheduler.add_task("Send Email")
print("Tasks in queue:", scheduler.display_tasks())
print("Processing task:", scheduler.process_task())
print("Remaining tasks:", scheduler.display_tasks())