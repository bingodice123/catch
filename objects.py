from tkinter import *
import random


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x600')

        self.image1 = PhotoImage(file='image.png')

        self.canvas = Canvas(self.root, width=500, height=500, bg='white')
        self.canvas.pack()
        self.player_image = self.canvas.create_image(250,450,image=self.image1)
        self.images = []
        self.speeds = []
        self.score_label = Label(self.root, text=0, font=("Sans Serif", 40))
        self.score_label.place(x=250,y=520)

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
        collision = False
        playerBbox = list(self.canvas.bbox(self.player_image))

        if self.new_image is not None:
            enemyBbox = self.canvas.bbox(self.new_image)

            if enemyBbox:  # Check that bbox is not None and is a valid list
                x_overlap = (playerBbox[2] >= enemyBbox[0] and playerBbox[0] <= enemyBbox[2])
                y_overlap = (playerBbox[3] >= enemyBbox[1] and playerBbox[1] <= enemyBbox[3])

                if x_overlap and y_overlap:
                    collision = True
                    self.score += 1
                    self.score_label.config(text=self.score)

                    # Remove the enemy object from the canvas
                    self.canvas.delete(self.new_image)
                    self.new_image = None

        self.root.after(1, self.check_collisions)
