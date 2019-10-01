import tkinter
import time

class MockEngine:
    def __init__(self):
        self.count = 0

    def get_next(self):
        self.count += 1
        return [[self.count]*4]*4

def run(engine):
    top = tkinter.Tk()

    top.configure(background="lightblue")
    

    labels = []
    for r in range(4):
        row = []
        for c in range(4):
            row.append(tkinter.StringVar())
        labels.append(row)


    state = engine.get_next()
    # for r in range(4):
    #     for c in range(4):
    #         l = tkinter.Label(top, padx=30, pady=30, textvariable=rep[r][c]).grid(row=r,column=c)

    frames = []

    for r in range(4):
        for c in range(4):
            f = tkinter.LabelFrame(top, height=100, width=100, padx = 20, pady = 20, bg='red')
            f.grid(row=r,column=c)
            l = tkinter.Label(f, textvariable=labels[r][c], bg=None).pack()


    while True:
        state = engine.get_next()
        for r in range(4):
            for c in range(4):
                labels[r][c].set(str(state[r][c]))
        top.update_idletasks()
        top.update()
        
        time.sleep(0.5)

run(MockEngine())