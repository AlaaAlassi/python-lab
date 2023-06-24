# behavioral_tree.py
import yaml
import py_trees
from task_factory import TaskFactory

# Load the YAML file
with open('mission.yaml', 'r') as file:
    behavioral_tree_yaml = yaml.safe_load(file)

# Create the behavior tree
root = py_trees.composites.Sequence("Root")

task_factory = TaskFactory()

for group_key, group_tasks in behavioral_tree_yaml['root'][0].items():
    if isinstance(group_tasks, list):
        for task_info in group_tasks:
            task_name = task_info['name']
            task_params = task_info.get('params', {})
            task = task_factory.create_task(task_name, **task_params)
            root.add_child(task)

# Create the behavior tree manager
tree = py_trees.trees.BehaviourTree(root)

# Execute the behavior tree
for _ in range(5):  # Run for 5 ticks
    tree.tick_tock(500)