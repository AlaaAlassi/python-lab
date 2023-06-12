import py_trees as pt

# Define the actions (leaf nodes)
class ActionA(pt.behaviour.Behaviour):
    def __init__(self, name):
        super(ActionA, self).__init__(name)

    def update(self):
        # Perform action A
        print("Performing Action A")
        return pt.common.Status.SUCCESS


class ActionB(pt.behaviour.Behaviour):
    def __init__(self, name):
        super(ActionB, self).__init__(name)

    def update(self):
        # Perform action B
        print("Performing Action B")
        return pt.common.Status.FAILURE


class ActionC(pt.behaviour.Behaviour):
    def __init__(self, name):
        super(ActionC, self).__init__(name)

    def update(self):
        # Perform action C
        print("Performing Action C")
        return pt.common.Status.SUCCESS


# Define the behavior tree
root = pt.composites.Sequence("Root", False)
#root = pt.composites.Selector("Root",False)
#root = pt.composites.Parallel("Root", policy=pt.common.ParallelPolicy.SUCCESS_ON_ALL)

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
