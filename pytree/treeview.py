"""
PyTree launcher script
wrappers for viewing tree types in the book, plus test cases/gui;
ported to Python 3.1 for the 4th edition of this book, June 2010;
"""
     
from tkinter import *
from treeview_wrappers import TreeWrapper, TreeViewer
import btree
import parser2
     
###################################################################
# binary tree wrapper
###################################################################
     
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

    def onInputLine(self, line, viewer):       # on test entry at bottom
        items = line.split()                   # make tree from text input
        t = btree.BinaryTree()                 # draw resulting btree
        for x in items: t.insert(x)            # no onClick handler here
        viewer.drawTree(t.tree)
     
###################################################################
# binary tree extension
###################################################################
     
class BinaryTree(btree.BinaryTree):
    def __init__(self, viewer):                # embed viewer in tree
        btree.BinaryTree.__init__(self)        # but viewer has a wrapper
        self.viewer  = viewer

    def view(self):
        self.viewer.drawTree(self.tree)
     
###################################################################
# parse tree wrapper
###################################################################
     
class ParseTreeWrapper(TreeWrapper):
    def __init__(self):                        # embed parse tree in viewer
        self.dict = {}                         # adds viewer protocols

    def children(self, node):
        try:
            return [node.left, node.right]
        except:
            try:
                return [node.var, node.val]
            except: 
                return None

    def label(self, node):
        for attr in ['label', 'num', 'name']:
            if hasattr(node, attr):
                return str(getattr(node, attr))
        return 'set'

    def onClick(self, node):                        # on tree label click
        try:                                        # tree-specific action
            result = node.apply(self.dict)          # evaluate subtree
            return 'Value = ' + str(result)         # show result in popup
        except:
            return 'Value = <error>'

     
###################################################################
# canned test cases (or type new nodelists/exprs in input field)
###################################################################
     
     
def test1_binary():                         # tree type is binary wrapper
    nodes = [3, 1, 9, 2, 7]                 # make a binary tree
    tree  = BinaryTree(viewer)              # embed viewer in tree
    for i in nodes: tree.insert(i)            
    tree.view()                             # sketch tree via embedded viewer
     
     
     
     
###################################################################
# build viewer with extra widgets to test tree types
###################################################################
     
if __name__ == '__main__':
    root = Tk()                             # build a single viewer gui
    bwrapper = BinaryTreeWrapper()          # add extras: input line, test btns
    pwrapper = ParseTreeWrapper()           # make wrapper objects
    viewer   = TreeViewer(bwrapper, root)   # start out in binary mode
     
     
    var = StringVar()
    var.set('btree')
    
     
    test1_binary()                          
    root.geometry("600x600+100+100") 
    root.mainloop()                                       # start up the gui
