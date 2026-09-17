class Task:
    taskname="Test Plan Creation"

    @classmethod
    def display_task_name(cls):
        print("Task Name :",Task.taskname)

    @classmethod
    def display_task_description(cls, description):
        print("Task Description :",description)


Task.display_task_name()
Task.display_task_description("Test Plan drives all Testing Activities")