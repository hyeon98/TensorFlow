from tkinter import *
from random import randint

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")

    def move_ball(self):
        deltax = randint(-5,5)
        deltay = randint(-5,5)
        self.canvas.move(self.ball, deltax, deltay)
        ballX1 = self.x1
        ballX2 = self.x2
        ballY1 = self.y1
        ballY2 = self.y2
        if ballX1 < 0:
            self.x1 = self.x1 + deltax
            self.x2 = self.x2 + deltax
        if ballX2 > 300:
            self.x1 = self.x1 - deltax
            self.x2 = self.x2 - deltax
        if ballY1 < 0:
            self.y1 = self.y1 + deltay
            self.y2 = self.y2 + deltay
        if ballY2 > 300:
            self.y1 = self.y1 - deltay
            self.y2 = self.y2 - deltay
        self.canvas.after(50, self.move_ball)

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

# create two ball objects and animate them
ball1 = Ball(canvas, 10, 10, 30, 30)
ball2 = Ball(canvas, 60, 60, 80, 80)

ball1.move_ball()
ball2.move_ball()

root.mainloop()