from tkinter import *
from treeview_wrappers import TreeWrapper, TreeViewer
import btree
     
root = Tk()                             # build a single viewer gui
bwrapper = TreeWrapper()          # add extras: input line, test btns
viewer   = TreeViewer(bwrapper, root)   # start out in binary mode

nodes = [3, 1, 9, 2, 7]                 # make a binary tree
tree  = btree.BinaryTree()             # embed viewer in tree
for i in nodes: tree.insert(i)            
viewer.drawTree(tree.tree)
     
                         
root.mainloop()                                       # start up the gui
