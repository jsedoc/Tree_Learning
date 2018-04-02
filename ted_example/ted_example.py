from create_tree import *
from zss import simple_distance
import numpy as np

i=3    
my_tree = generate_data(i)
tmp = convert(my_tree)
my_tree2 = convert(tmp)
pprint(my_tree)
my_tree2 = generate_data(i)
change_nts(my_tree)
pprint(my_tree2)
l = my_tree2.left
r = my_tree2.right
my_tree2.left = my_tree.right
my_tree2.right = my_tree.left

print simple_distance((my_tree), (my_tree2), Node.get_children, Node.get_label)
