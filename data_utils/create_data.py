from __future__ import print_function
from create_tree import *
import numpy as np
import random


DATA_DIR = "../data/"

def curriculum_depth(i, num_examples, max_depth):
    curriculum_max_depth= int((max_depth*i)/num_examples)
    #print(i, curriculum_max_depth,)
    if curriculum_max_depth > 0:
       random_depth = 2 + np.random.randint(curriculum_max_depth)
    else:
        random_depth = 2
    #print("DEPTH = ", random_depth)
    return random_depth
        


def copy_t2t(depth):
    my_tree = generate_data(depth-1)
    change_nts(my_tree)

    my_list = convert_to_list_inorder(my_tree,[])
    infix_tree = ' '.join(str(e) for e in my_list)

    #print my_tree
    return ([infix_tree, infix_tree])

def create_examples(num_examples, max_depth, function):
    data = []
    for i in range(num_examples):
        depth = max_depth
        if np.random.randint(2) == 0:
            depth = curriculum_depth(i, num_examples, max_depth)
        data.append(function(depth))
    return data


if __name__ == "__main__":

    num_examples = 1000
    max_depth = 5
    data_subset = "train"
    t2t_operation = "COPY"
    seed = 0
    
    #NOTE: we need both -- for reproducible trees...
    #numpy.random.seed(seed)
    #random.seed(seed)
    
    if t2t_operation == "COPY":
        data = create_examples(num_examples,max_depth, function=copy_t2t)
        trans = open(DATA_DIR + data_subset + '.copy', 'w')
    elif t2t_operation == "RELABEL_1":
        data = create_examples(num_examples,max_depth, function=copy_t2t)
        trans = open(DATA_DIR + data_subset + '.copy', 'w')
        
    
    orig  = open(DATA_DIR + data_subset + '.orig', 'w')
    
    for i in range(num_examples):
        print(data[i][0], file=orig)
        print(data[i][1], file=trans)
    
    #orig_vocab  = open(DATA_DIR + 'vocab.train.orig', 'w')
    #trans_vocab = open(DATA_DIR + 'vocab.train.copy', 'w')

    #max_num = 256
    #operators = ['+','-','*','/']
    
    #for i in range(1, max_num+1):
    #    print >> orig_vocab, i, i
    #    print >> trans_vocab, i, i

    #for i in range(len(operators)):
    #    print >> orig_vocab, operators[i], max_num+i+1
    #    print >> trans_vocab, operators[i], max_num+i+1

    #print >> orig_vocab, '(', max_num + len(operators) + 1
    #print >> orig_vocab, ')', max_num + len(operators) + 2
    #print >> trans_vocab, '(', max_num + len(operators) + 1
    #print >> trans_vocab, ')', max_num + len(operators) + 2
