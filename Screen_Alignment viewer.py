import re, sys, os, threading, tkinter as tk
from tkinter import Toplevel, Canvas
from screeninfo import get_monitors
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    global DEBUG
    if DEBUG == False:
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    else:
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
            edited_base_path = base_path + "/Logitech GHub Battery Percentage Viewer"
            unedited_path = os.path.join(edited_base_path, relative_path)
            edited_path = unedited_path.replace('\\' , '/')
        return edited_path
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")
   
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass    
sys.stdout = Logger()
DEBUG = True    # Defines what values to use for the location of files 
""" Set DEBUG to False when freezing code """
lastClickX = 0
lastClickY = 0
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))
root = tk.Tk()
root.attributes('-topmost', True)
def refresh():
    threading.Timer(1.0, refresh).start()
    canvas.delete("all")
    #Get the current screen width and height
    monitorlist = []
    for m in get_monitors():        # Gets monitor info
        print(m)        # Prints monitor info
        monitorlist.append(m)        # Adds monitor info to a list
    print(monitorlist)        # Prints the list containing the monitor info
    monlistlen = len(monitorlist)        # Gets the length of the list containing the monitor info
    level = -1
    newmonlist = []
    dislist = []
    monwidth = []
    monheight = []
    screenwidth = []
    screenheight = []
    for i in range(monlistlen):        # Repeat the following code as many times as there are items in the list containing the monitor info
        level = level + 1
        dislisttext = "Display " + str(level)
        dislist.append(dislisttext)
        print(dislisttext)           # Print
        print(dislist)           # Print
        monlistitem = str(monitorlist[level])
        sep = ", width_mm="
        stripped = monlistitem.split(sep, 1)[0]        # Separates an item from the list containing the monitor info and removes any unnecessary data
        newmonlist.append(stripped)        # Adds the separated necessary data to a list
        print(stripped)        # Prints the data the necessary data the was spearated
        newitems = re.findall(r'-?\d+', stripped)      # Extract all numbers into a list
        monwidth.append(str(newitems[0]))   
        monheight.append(str(newitems[1]))   
        screenwidth.append(str(newitems[2]))   
        screenheight.append(str(newitems[3]))
    print(monwidth)
    print(monheight)
    print(screenwidth)
    print(screenheight)
    def smallest_num_in_list( list ):
        min = list[ 0 ]
        for a in list:
            if a < min:
                min = a
        return min
    def biggest_num_in_list( list ):
        max = list[ 0 ]
        for a in list:
            if a > max:
                max = a
        return max
    print(biggest_num_in_list(screenheight))
    x = 1
    curlevel = 0
    for i in screenwidth:
        x += (int(screenwidth[curlevel])/10)
        curlevel += 1
    print(smallest_num_in_list(monwidth))
    print(smallest_num_in_list(monheight))
    print(smallest_num_in_list(screenwidth))
    print(smallest_num_in_list(screenheight))
    monheightmin = '{:}'.format(abs(int(smallest_num_in_list(monwidth))))
    monwidthmin = '{:}'.format(abs(int(smallest_num_in_list(monheight))))
    screenheightmin = '{:}'.format(abs(int(smallest_num_in_list(screenwidth))))
    screenwidthmin = '{:}'.format(abs(int(smallest_num_in_list(screenheight))))
    print(monheightmin)
    print(monwidthmin)
    print(screenheightmin)
    print(screenwidthmin)
    curlevel = 0
    for i in monwidth:
        # Calculate X values for line points on canvas
        item = int(monwidth[curlevel])
        item += int(monheightmin)
        print(item)
        monwidth[curlevel] = item/10
        # Calculate Y values for line points on canvas
        item = int(monheight[curlevel])
        item += int(monwidthmin)
        print(item)
        monheight[curlevel] = item/10
        # Calculate second X values for line points on canvas
        screenwidth[curlevel] = float(monwidth[curlevel])+(float(screenwidth[curlevel])/10)
        # Calculate second Y values for line points on canvas
        screenheight[curlevel] = float(monheight[curlevel])+float(screenheight[curlevel])/10
        curlevel += 1
    y = (int(biggest_num_in_list(screenheight))+2)
    print(monwidth)
    print(monheight)
    print(screenwidth)
    print(screenheight)
    canvas.config(width=x, height=y)
    loc1 = 0
    monlen = len(monwidth)
    linecolour = []
    linecolour.append('#FF0000')
    linecolour.append('#FFFF00')
    linecolour.append('#00FFFF')
    listcur = 0
    for i in range(monlen):
        canvas.create_line(monwidth[listcur], monheight[listcur], screenwidth[listcur], screenheight[listcur], width=1, fill=linecolour[listcur])
        canvas.create_line(monwidth[listcur], monheight[listcur], monwidth[listcur], screenheight[listcur], width=1, fill='#39ff14')
        canvas.create_line(monwidth[listcur], monheight[listcur], screenwidth[listcur], monheight[listcur], width=1, fill='#39ff14')
        canvas.create_line(monwidth[listcur], screenheight[listcur], screenwidth[listcur], screenheight[listcur], width=1, fill='#39ff14')
        canvas.create_line(screenwidth[listcur], monheight[listcur], screenwidth[listcur], screenheight[listcur], width=1, fill='#39ff14')
        listcur += 1
    canvas.pack()
root.overrideredirect(True)
root.configure(background='black') #39ff14
canvas = Canvas(root, width=5, height=5, bg='black', highlightthickness=0)
# Define an event to close the window
def close_win(e):
   root.destroy()
# Bind the ESC key with the callback function
root.bind('<Escape>', lambda e: close_win(e))
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
refresh()
root.mainloop()