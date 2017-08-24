from tkinter import *
from treeview_wrappers import TreeWrapper, TreeViewer
import btree
     
class BinaryTreeWrapper(TreeWrapper):          # embed binary tree in viewer
    def children(self, node):                  # adds viewer protocols
        try:                                   # to interface with tree
            return [node.left, node.right]
        except: 
            return None

    def label(self, node):
        try:    
            return str(node.data)
        except: 
            return str(node)

root = Tk()                             # build a single viewer gui
bwrapper = BinaryTreeWrapper()          # add extras: input line, test btns
viewer   = TreeViewer(bwrapper, root)   # start out in binary mode

nodes = [3, 1, 9, 2, 7]                 # make a binary tree
tree  = btree.BinaryTree()             # embed viewer in tree
for i in nodes: tree.insert(i)            
viewer.drawTree(tree.tree)
     
                         
root.mainloop()                                       # start up the gui
