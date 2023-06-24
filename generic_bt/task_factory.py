import py_trees

# Task implementations
class Task1(py_trees.behaviour.Behaviour):
    def __init__(self, name, parameter,flag):
        super().__init__(name)
        self.parameter = parameter

    def update(self):
        # Implement the logic for Task1 using self.parameter
        print(f"Executing Task1 with parameter: {self.parameter}")
        return py_trees.common.Status.SUCCESS

class Task2(py_trees.behaviour.Behaviour):
    def __init__(self, name, parameter,flag):
        super().__init__(name)
        self.parameter = parameter

    def update(self):
        # Implement the logic for Task2 using self.parameter
        print(f"Executing Task2 with parameter: {self.parameter}")
        return py_trees.common.Status.SUCCESS

# Task factory interface
class TaskFactoryInterface:
    def create_task(self, task_name, **kwargs):
        raise NotImplementedError

# Task factory implementation
class TaskFactory(TaskFactoryInterface):
    def create_task(self, task_name, **kwargs):
        if task_name == 'Task1':
            parameter = kwargs.pop('parameter', None)
            print(parameter)
            flag = kwargs.pop('flag', False)
            return Task1(task_name, parameter, flag)
        elif task_name == 'Task2':
            parameter = kwargs.pop('parameter', None)
            flag = kwargs.pop('flag', False)
            return Task2(task_name, parameter, flag)
        else:
            raise ValueError(f"Unknown task: {task_name}")
