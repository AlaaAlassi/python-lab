import py_trees as pt
import random

# Define the actions (leaf nodes)
class ActionA(pt.behaviour.Behaviour):
    def __init__(self, name):
        super(ActionA, self).__init__(name)

    def update(self):
        # Simulate high success rate
        success = random.random() < 0.8
        if success:
            print("Performing Action A - Success")
            return pt.common.Status.SUCCESS
        else:
            print("Performing Action A - Failure")
            return pt.common.Status.FAILURE


class ActionB(pt.behaviour.Behaviour):
    def __init__(self, name):
        super(ActionB, self).__init__(name)

    def update(self):
        # Simulate high success rate
        success = random.random() < 0.9
        if success:
            print("Performing Action B - Success")
            return pt.common.Status.SUCCESS
        else:
            print("Performing Action B - Failure")
            return pt.common.Status.FAILURE


class ActionC(pt.behaviour.Behaviour):
    def __init__(self, name):
        super(ActionC, self).__init__(name)

    def update(self):
        # Simulate lower success rate
        success = random.random() < 0.5
        if success:
            print("Performing Action C - Success")
            return pt.common.Status.SUCCESS
        else:
            print("Performing Action C - Failure")
            return pt.common.Status.FAILURE


# Define the behavior tree
root = pt.composites.Parallel("Root", policy=pt.common.ParallelPolicy.SUCCESS_ON_ONE)

task_a = ActionA("Task A")
task_b = ActionB("Task B")
task_c = ActionC("Task C")

root.add_child(task_a)
root.add_child(task_b)
root.add_child(task_c)

# Create a behavior tree and tick it
tree = pt.trees.BehaviourTree(root)

# Run the behavior tree
tree.setup(timeout=15)
tree.tick_tock(500)
