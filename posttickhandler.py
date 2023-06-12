import py_trees as pt
import functools
import py_trees.display

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
root = pt.composites.Sequence("Root")

task_a = ActionA("Task A")
task_b = ActionB("Task B")
task_c = ActionC("Task C")

root.add_child(task_a)
root.add_child(task_b)
root.add_child(task_c)

# Create a behavior tree
tree = pt.trees.BehaviourTree(root)

# Define the post-tick handler
def post_tick_handler(snapshot_visitor, behaviour_tree):
    print(pt.display.ascii_tree(behaviour_tree.root,
                          snapshot_information=snapshot_visitor))

# Add the post-tick handler to the behavior tree
snapshot_visitor = pt.visitors.SnapshotVisitor()
tree.add_post_tick_handler(
    functools.partial(post_tick_handler, snapshot_visitor)
)
tree.visitors.append(snapshot_visitor)

# Run the behavior tree
tree.setup(timeout=15)
tree.tick_tock(500)
