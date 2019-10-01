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

    rep = []
    for r in range(4):
        row = []
        for c in range(4):
            row.append(tkinter.StringVar())
        rep.append(row)


    state = engine.get_next()
    for r in range(4):
        for c in range(4):
            l = tkinter.Label(top, padx=30, pady=30, textvariable=rep[r][c]).grid(row=r,column=c)

    # for r in range(4):
    #     for c in range(4):
    #         f = tkinter.Frame(top, width=100, height=100, padx = 20, pady = 20).grid(row=r,column=c)
    #         l = tkinter.Label(f, textvariable=rep[r][c])

    while True:
        state = engine.get_next()
        for r in range(4):
            for c in range(4):
                rep[r][c].set(str(state[r][c]))
        top.update_idletasks()
        top.update()
        
        time.sleep(0.5)

run(MockEngine())