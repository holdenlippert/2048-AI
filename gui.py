import tkinter
import time

class MockEngine:
    def __init__(self):
        self.count = 0

    def get_next(self):
        self.count += 1
        return [[self.count]*4]*4

def color_from_num(num):
    val = int(num)

    if val == 0:
        return "snow3"
    elif val <= 2:
        return "snow1"
    elif val <= 4:
        return "pale goldenrod"
    elif val <= 8:
        return "salmon1"
    elif val <= 16:
        return "coral1"
    elif val <= 32:
        return "salmon"
    elif val <= 64:
        return "red"
    else:
        return "gold"



def run(engine):
    top = tkinter.Tk()

    top.configure(background="lightblue")
    

    labels = []
    for r in range(4):
        row = []
        for c in range(4):
            row.append(tkinter.StringVar())
        labels.append(row)


    state = engine.get_next() #initial state
    frames = []
    for r in range(4):
        row = []
        for c in range(4):
            row.append(None)
        frames.append(row)

    for r in range(4):
        for c in range(4):
            f = tkinter.LabelFrame(top, height=100, width=100, padx = 20, pady = 20, bg='snow3')
            f.grid(row=r,column=c)
            l = tkinter.Label(f, textvariable=labels[r][c]).pack()
            frames[r][c] = f


    while True:
        state = engine.get_next()
        for r in range(4):
            for c in range(4):
                labels[r][c].set(str(state[r][c]))
                frames[r][c].configure(bg=color_from_num(state[r][c]))

        top.update_idletasks()
        top.update()
        
        time.sleep(0.5)

run(MockEngine())