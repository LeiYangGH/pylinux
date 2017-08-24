"""
#########################################################################
# PyTree: sketch arbitrary tree data structures in a scrolled canvas;
# this version uses tree wrapper classes embedded in the viewer gui 
# to support arbitrary trees (i.e.. composition, not viewer subclassing);
# also adds tree node label click callbacks--run tree specific actions;
# see treeview_subclasses.py for subclass-based alternative structure;
# subclassing limits one tree viewer to one tree type, wrappers do not;
# see treeview_left.py for an alternative way to draw the tree object;
# see and run treeview.py for binary and parse tree wrapper test cases;
#########################################################################
"""
  
from tkinter import *
from tkinter.messagebox import showinfo
     
Width, Height = 600, 400                    # start canvas size (reset per tree)
Rowsz = 100                                 # pixels per tree row
Colsz = 100                                 # pixels per tree col

class TreeWrapper:          # embed binary tree in viewer
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

    def value(self, treenode):
        return ''

###########$######################
# tree view gui, tree independent
##################################
     
class TreeViewer(Frame):
    def __init__(self, wrapper, parent=None, tree=None, bg='brown', fg='beige'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(bg)                    # build gui: scrolled canvas
        self.master.title('PyTree 1.0')         # assume I'm run standalone
        self.wrapper = wrapper                  # embed a TreeWrapper object
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
        wrapper = self.wrapper
        levels, maxrow = self.planLevels(tree, wrapper)
        self.canvas.config(scrollregion=(                     # scrollable area
            0, 0, (Colsz * maxrow), (Rowsz * len(levels)) ))  # upleft, lowright
        self.drawLevels(levels, maxrow, wrapper)
     
    def planLevels(self, root, wrap):
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
                    children = wrap.children(node)             # list of nodes
                    if not children:
                        nextlevel.append((None, None))         # leave a hole
                    else:
                        for child in children:
                            nextlevel.append((child, node))    # parent link
            currlevel = nextlevel
        return levels, maxrow
     
    def drawLevels(self, levels, maxrow, wrap):
        rowpos = 0                                         # draw tree per plan
        for level in levels:                               # set click handlers
            colinc = (maxrow * Colsz) // (len(level) + 1)  # levels is treenodes
            colpos = 0                                     # 3.X: // floor int div
            for (node, parent) in level:
                colpos += colinc
                if node != None:
                    text = wrap.label(node)
                    more = wrap.value(node)
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
