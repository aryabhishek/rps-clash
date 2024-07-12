from turtle import Turtle, Screen, register_shape
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
import tkinter

ROCK = "./imgs/stone.gif"
PAPER = "./imgs/paper.gif"
SCISSOR = "./imgs/scissor.gif"

# ------------------------------------------------------------Classes----------------------------------------------------------#


class FreeParticle(Turtle):
    def __init__(self, x, y, img=None):
        super().__init__()
        self.penup()
        self.goto(x, y)
        if img:
            register_shape(img)
            self.shape(img)


# ------------------------------------------------------------Functions----------------------------------------------------------#


def make_box(pen):
    pen = Turtle()
    pen.hideturtle()
    pen.color("white")
    pen.penup()
    pen.goto(-350, 225)
    pen.pendown()
    pen.goto(-350, -300)
    pen.goto(350, -300)
    pen.goto(350, 225)
    pen.goto(-350, 225)


def make_input_area(pen: Turtle, r, p, s):
    pen.goto(-300, 250)
    pen.color("white")
    pen.pendown()
    pen.write(f"Rocks: {r}")
    pen.up()
    pen.goto(-50, 250)
    pen.down()
    pen.write(f"Papers: {p}")
    pen.up()
    pen.goto(250, 250)
    pen.down()
    pen.write(f"Scissors: {s}")
    pen.hideturtle()


def take_input():
    rocks = papers = scissors = 0
    tk_win = CTk()
    tk_win.geometry("400x400")
    tk_win.title("Rock-Paper-Scissors Input")
    tk_win.configure(bg="black")
    tk_win.resizable(False, False)

    rock_label = CTkLabel(master=tk_win, text="Rocks: ")
    paper_label = CTkLabel(text="Papers: ")
    scissors_label = CTkLabel(text="Scissors: ")

    rock_entry = CTkEntry()
    paper_entry = CTkEntry()
    scissors_entry = CTkEntry()

    def start():
        nonlocal rocks, papers, scissors
        rocks = rock_entry.get()
        papers = paper_entry.get()
        scissors = scissors_entry.get()
        tk_win.destroy()

    start_button = CTkButton(text="Start!", command=start)

    rock_label.grid(row=0, column=0)
    paper_label.grid(row=1, column=0)
    scissors_label.grid(row=2, column=0)
    rock_entry.grid(row=0, column=1)
    paper_entry.grid(row=1, column=1)
    scissors_entry.grid(row=2, column=1)
    start_button.grid(row=3, column=0, columnspan=2)

    tk_win.mainloop()
    return rocks, papers, scissors


def start_game():
    rocks, papers, scissors = take_input()
    win = Screen()
    win.title("Rock-Paper-Scrissors Clash!")
    win.setup(800, 700)
    win.bgcolor("black")
    win.tracer(0)
    writer = Turtle()

    make_box(writer)
    make_input_area(writer, rocks, papers, scissors)

    rock_obj = FreeParticle(-100, 0, ROCK)
    paper_obj = FreeParticle(0, 0, PAPER)
    scissor_obj = FreeParticle(100, 0, SCISSOR)

    win.update()
    win.mainloop()


# Logic
# stone x scissor = stone
# stone x paper = paper
# paper x scissor = scissor

# -----------------------------------------------------------Main-----------------------------------------------------------#

if __name__ == "__main__":
    start_game()
