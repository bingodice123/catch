from tkinter import *
import random


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')

        self.image1 = PhotoImage(file='image.png')

        self.canvas = Canvas(self.root, width=500, height=500, bg='white')
        self.canvas.pack()
        self.player_image = self.canvas.create_image(250,450,image=self.image1)
        self.images = []
        self.speeds = []

        self.score = 0

        self.update_gravity()
        self.schedule_cloning()
        self.check_collisions()
        self.root.bind('<Left>', self.move_player_left)
        self.root.bind('<Right>', self.move_player_right)
        self.root.mainloop()

    def update_gravity(self):
        for i in range(len(self.images)):
            self.canvas.move(self.images[i], 0, self.speeds[i])
            self.speeds[i] += 2  # Gravity accelerates the object downward
        self.canvas.update()
        self.root.after(50, self.update_gravity)  # Schedule the next update

    def clone_image(self):
        x = random.randint(0, 500)
        y = 0
        self.new_image = self.canvas.create_image(x, y, image=self.image1)
        self.images.append(self.new_image)
        self.speeds.append(0)

    def schedule_cloning(self):
        self.clone_image()
        self.root.after(2000, self.schedule_cloning)  # Schedule the next cloning in 2 seconds

    def move_player_left(self, event):
        self.canvas.move(self.player_image, -20, 0)

    def move_player_right(self, event):
        self.canvas.move(self.player_image, 20, 0)

    def check_collisions(self):
        xCheck = False
        yCheck = False
        collision = False
        playerBbox = list(self.canvas.bbox(self.player_image))
        enemyBbox = list(self.canvas.bbox(self.new_image))
        if enemyBbox[2] >= playerBbox[0] >= enemyBbox[2] + 50:
            xCheck = True
        if enemyBbox[3] >= playerBbox[1] >= enemyBbox[3] + 50:
            yCheck = True
        if xCheck == True and yCheck == True:
            collision = True
            self.score += 1
        self.root.after(1, self.check_collisions)
