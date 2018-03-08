from binarytree import Node, setup, tree, pprint
import copy 

# Define your own null/sentinel value
my_null = None

class MyNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = -1
        self.balance = -3

    def rebalance(self):
        """
        Rebalance tree. After inserting or deleting a node, 
        it is necessary to check each of the node's ancestors for consistency with the rules of AVL
        """

        # Check if we need to rebalance the tree
        #   update height
        #   balance tree
        self.update_heights(recursive=True)
        self.update_balances(True)

        # For each node checked, 
        while self.balance < -1 or self.balance > 1: 
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Case -> rotate y,z to the left
                if self.left.balance < 0:
                    #     x               x
                    #    / \             / \
                    #   y   D           z   D
                    #  / \        ->   / \
                    # A   z           y   C
                    #    / \         / \
                    #   B   C       A   B
                    self.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                # Left Left Case -> rotate z,x to the right
                #       x                 z
                #      / \              /   \
                #     z   D            y     x
                #    / \         ->   / \   / \
                #   y   C            A   B C   D 
                #  / \ 
                # A   B
                self.rotate_right()
                self.update_heights()
                self.update_balances()
            
            # Right subtree is larger than left subtree
            if self.balance < -1:
                
                # Right Left Case -> rotate x,z to the right
                if self.right.balance > 0:
                    #     y               y
                    #    / \             / \
                    #   A   x           A   z
                    #      / \    ->       / \
                    #     z   D           B   x
                    #    / \                 / \
                    #   B   C               C   D
                    self.right.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()

                # Right Right Case -> rotate y,x to the left
                #       y                 z
                #      / \              /   \
                #     A   z            y     x
                #        / \     ->   / \   / \
                #       B   x        A   B C   D 
                #          / \ 
                #         C   D
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height

        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self: 
            if recursive: 
                if self.left != None: 
                    self.left.update_heights()
                if self.right != None:
                    self.right.update_heights()
            
            if self.left != None  and self.right != None:
                self.height = 1 + max(self.left.height, self.right.height)
            else:
                self.height = 1
        else: 
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor

        The balance factor is calculated as follows: 
            balance = height(left subtree) - height(right subtree). 
        """
        if self:
            if recursive:
                if self.left != None:
                    self.left.update_balances()
                if self.right != None:
                    self.right.update_balances()

            if self.left != None  and self.right != None:
                self.balance = self.left.height - self.right.height
            elif self.left == None  and self.right == None:
                self.balance = 0
            elif self.right != None:
                self.balance = - self.right.height
            elif self.left != None:
                self.balance = self.left.height 
        else:
            self.balance = 0 

            
    def rotate_right(self):
        """
        Right rotation
            set self as the right subtree of left subree
        """
        print "rotate right"
        new_root = self.left
        new_left_sub = self.left.right
        old_root = self

        self = new_root
        print " --- new root --- "
        print self
        print " --- old root --- "
        print old_root
        old_root.left = new_left_sub
        new_root.right = old_root

    def rotate_left(self):
        """
        Left rotation
            set self as the left subtree of right subree
        """
        print "rotate left"
        new_root = copy.deepcopy(self.right)
        new_left_sub = copy.deepcopy(new_root.left)
        old_root = self

        self = new_root
        old_root.right = new_left_sub
        new_root.left = old_root

# Call setup in the beginning to apply your specification
setup(
    node_init_func=lambda v: MyNode(v),
    node_class=MyNode,
    null_value=my_null,
    value_attr='value',
    left_attr='left',
    right_attr='right'
)
my_custom_tree = tree()

