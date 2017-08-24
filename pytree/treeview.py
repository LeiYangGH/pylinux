from tkinter import *
from treeview_wrappers import TreeWrapper, TreeViewer
import btree
     
root = Tk()                             # build a single viewer gui
bwrapper = TreeWrapper()          # add extras: input line, test btns

nodes = [3, 1, 9, 2, 7]                 # make a binary tree
tree  = btree.BinaryTree()             # embed viewer in tree
for i in nodes: tree.insert(i)            
TreeViewer(bwrapper, root,tree.tree)   # start out in binary mode
     
                         
root.mainloop()                                       # start up the gui
