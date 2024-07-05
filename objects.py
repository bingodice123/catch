from tkinter import *

class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')

        image1 = PhotoImage(file='image.png')

        self.canvas = Canvas(self.root, width=500, height=500, bg='white')
        self.canvas.pack()
        self.imageFinal = self.canvas.create_image(100, 100, image=image1)
        self.speed_y = 0

        self.update_gravity()
        self.root.mainloop()

    def update_gravity(self):
        self.speed_y += 2
        self.canvas.move(self.imageFinal, 0, self.speed_y)
        self.canvas.update()
        self.root.after(50, self.update_gravity)
