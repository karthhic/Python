from Tkinter import *
import time
import os, sys
x = 0
class carrier:
    def __init__(self, width, height, speed, size):
        self.x_max = size[0]
        self.y_max = size[1]
        self.speed = speed
        self.width = width
        self.height = height
        self.margin = 10
        self.center = [width/2,height/2]
        self.xOffset = width/2
        self.yOffset = height/2
        if self.width > size[0] or self.height > size[1]:
            print 'Canvas size is smaller than carrier size. Change it "Example: (20,20,0.005,[500,700])"'
            sys.exit(0)
        animation = Tk()
        animation.wm_title("Monorail Carrier Simulation")
        canvas = Canvas(animation, width=(self.width+self.x_max), height=(self.height+self.y_max))
        canvas.pack()
        canvas.create_rectangle((self.margin-5),(self.margin-5),(self.margin+self.width+5),(self.margin+self.width+5), fill = "grey")
        _ems= canvas.create_rectangle(self.margin,self.margin,(self.margin+self.width),(self.margin+self.width), fill = "white")
        canvas.create_rectangle((self.margin+self.xOffset),(self.margin+self.yOffset),(self.x_max),(self.y_max), fill = None)
        length= (((self.x_max+self.y_max)*2)-((self.margin+self.xOffset)+(self.margin+self.yOffset)))
        start = (self.margin+self.xOffset+self.yOffset+10)

        def load(who):
            canvas.itemconfig(who, fill="green")

        def unload(who):
            canvas.itemconfig(who, fill="white")


        def run(n):
            for x in range(start, length):
                pos = canvas.coords(n)
                if (pos[1] == self.margin and pos[0] in range(self.margin,(self.x_max-(self.xOffset)))):
                    canvas.move(n,1,0)
                elif (pos[0] == (self.x_max-self.xOffset) and pos[1] in range(self.margin,(self.y_max-self.yOffset))):
                    canvas.move(n,0,1)
                elif (pos[1] == (self.y_max-self.yOffset) and pos[0] in range((self.margin+1),(self.x_max-(self.margin-1)))):
                    canvas.move(n,-1,0)
                elif (pos[0] == (self.margin) and pos[1] in range((self.margin-1),(self.y_max-(self.margin-1)))):
                    canvas.move(n,0,-1)
                else:
                    print (self.y_max-self.margin)
                    print (self.x_max-self.margin)
                    sys.exit(0)
                if (pos[1] == self.margin and pos[0] == (self.x_max-(self.xOffset))/2):
                    load(_ems)
                    time.sleep(2)
                    print("first")
                elif (pos[0] == (self.x_max-self.xOffset) and pos[1] == (self.y_max-self.yOffset)/2):
                    unload(_ems)
                    time.sleep(2)
                    print("Second")
                elif (pos[1] == (self.y_max-self.yOffset) and pos[0] == (self.x_max-(self.margin-1))/2):
                    load(_ems)
                    time.sleep(2)
                    print("three")
                elif (pos[0] == (self.margin) and pos[1] == (self.y_max-(self.margin-1))/2):
                    unload(_ems)
                    time.sleep(2)
                    print("four")
                animation.update()
                time.sleep(self.speed)
                print (canvas.coords(n))
        stat = run(2)
        label=Label(animation, text="Run Simulation"). pack()
        stat = run(2)
        button=Button(animation, text="Run",command=stat).pack()
        animation.mainloop()
        #run()
class takeInput(object):

    def __init__(self,requestMessage):
        self.root = Tk()
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)

    def acceptInput(self,requestMessage):
        r = self.frame

        k = Label(r,text=requestMessage)
        k.pack(side='left')
        self.e = Entry(r,text='Name')
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r,text='okay',command=self.gettext)
        b.pack(side='right')

    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()

def getText(requestMessage):
    msgBox = takeInput(requestMessage)
    msgBox.waitForInput()
    return msgBox.getString()

var = getText('Enter the parameters')
if var == '':
    print "No data"
    var = "80,80,100,900,600"
var = var.split(",")
print "Var:", var
speedper = 0.005
print speedper
ems=carrier(int(var[0]),int(var[1]),speedper,[int(var[3]),int(var[4])])
print speedper
#ems = carrier(20,20,0.005,[500,300])
#20,20,100,500,300
#50,50,100,500,300
#80,80,100,500,300
