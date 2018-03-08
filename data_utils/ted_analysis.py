from create_tree import *
from zss import simple_distance
import numpy as np

x={}

for i in range(2,6):
    for j in range(1000):
        my_tree = generate_data(i)
        tmp = convert(my_tree)
        my_tree2 = convert(tmp)
        #change_nts(my_tree)
        l = my_tree2.left
        r = my_tree2.right
        my_tree2.left = my_tree.right
        my_tree2.right = my_tree.left
        # pprint(my_tree)
        #my_tree2 = generate_data(i)
        #change_nts(my_tree)
        # pprint(my_tree2)
        if not x.has_key(i):
            x[i] = []
        x[i].append(simple_distance((my_tree), (my_tree2), Node.get_children, Node.get_label))

    print np.average(x[i])
    
print simple_distance((my_tree), (my_tree2), Node.get_children, Node.get_label)
