"a valueless binary search tree"

class BinaryTree:
    def __init__(self):       self.tree = EmptyNode()
    def lookup(self, value):  return self.tree.lookup(value)
    def insert(self, value):  self.tree = self.tree.insert(value)

class EmptyNode:
    def __repr__(self):
        return '*'
    def lookup(self, value):                      # fail at the bottom
        return False
    def insert(self, value):
        return BinaryNode(self, value, self)      # add new node at bottom
    def children(self):                  # adds viewer protocols
        return None

    def label(self):
        return str(self)

    def value(self):
        return ''

class BinaryNode:
    def __init__(self, left, value, right):
        self.data, self.left, self.right  =  value, left, right

    def lookup(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            return self.left.lookup(value)               # look in left
        else:
            return self.right.lookup(value)              # look in right

    def insert(self, value):
        if self.data > value:
            self.left = self.left.insert(value)          # grow in left
        elif self.data < value:
            self.right = self.right.insert(value)        # grow in right
        return self

    def children(self):                  # adds viewer protocols
        return [self.left, self.right]

    def label(self):
        return str(self.data)

    def value(self):
        return ''

from tkinter import *
from tkinter.messagebox import showinfo
     
Width, Height = 600, 400                    # start canvas size (reset per tree)
Rowsz = 100                                 # pixels per tree row
Colsz = 100                                 # pixels per tree col

class TreeViewer(Frame):
    def __init__(self, parent=None, tree=None, bg='brown', fg='beige'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(bg)                    # build gui: scrolled canvas
        self.master.title('PyTree 1.0')         # assume I'm run standalone
        self.fg = fg                            # setTreeType changes wrapper 
        if tree:
           self.drawTree(tree)
     
    def makeWidgets(self, bg):
        self.title = Label(self, text='PyTree 1.0')
        self.canvas = Canvas(self, bg=bg, borderwidth=0)
     
        self.title.pack(side=TOP, fill=X)
        self.canvas.pack(side=TOP, fill=BOTH, expand=YES)
     
        self.canvas.config(height=Height, width=Width)  # viewable area size
     
     
    def drawTree(self, tree):
        levels, maxrow = self.planLevels(tree)
        self.canvas.config(scrollregion=(                     # scrollable area
            0, 0, (Colsz * maxrow), (Rowsz * len(levels)) ))  # upleft, lowright
        self.drawLevels(levels, maxrow)
     
    def planLevels(self, root):
        levels = []
        maxrow = 0                                       # traverse tree to 
        currlevel = [(root, None)]                       # layout rows, cols
        while currlevel:
            levels.append(currlevel)
            size = len(currlevel)
            if size > maxrow: maxrow = size
            nextlevel = []
            for (node, parent) in currlevel:
                if node != None:
                    children = node.children()             # list of nodes
                    if not children:
                        nextlevel.append((None, None))         # leave a hole
                    else:
                        for child in children:
                            nextlevel.append((child, node))    # parent link
            currlevel = nextlevel
        return levels, maxrow
     
    def drawLevels(self, levels, maxrow):
        rowpos = 0                                         # draw tree per plan
        for level in levels:                               # set click handlers
            colinc = (maxrow * Colsz) // (len(level) + 1)  # levels is treenodes
            colpos = 0                                     # 3.X: // floor int div
            for (node, parent) in level:
                colpos += colinc
                if node != None:
                    text = node.label()
                    more = node.value()
                    if more: text = text + '=' + more
                    win = Label(self.canvas, text=text, 
                                             bg=self.fg, bd=3, relief=RAISED)
                    win.pack()

                    self.canvas.create_window(colpos, rowpos, anchor=NW, 
                                window=win, width=Colsz*.5, height=Rowsz*.5)
                    if parent != None:
                        self.canvas.create_line(
                            parent.__colpos + Colsz*.25,    # from x-y, to x-y
                            parent.__rowpos + Rowsz*.5,
                            colpos + Colsz*.25, rowpos, arrow='last', width=1)
                    node.__rowpos = rowpos
                    node.__colpos = colpos          # mark node, private attrs
            rowpos += Rowsz

root = Tk()                             # build a single viewer gui
nodes = [3, 1, 9, 2, 7]                 # make a binary tree
tree  = BinaryTree()             # embed viewer in tree
for i in nodes: tree.insert(i)            
TreeViewer(root,tree.tree)   # start out in binary mode
     
                         
root.mainloop()  
