from tkinter import*
import random
from random import shuffle
import pygame
pygame.init()
root=Tk()
root.title("who wants to be a millionaire")
root.geometry("1352*635+0+0")
root.configure(background="black")
questions_1 = {
    1:"""Who is considered the father of BIGBANG?
    A: blah blah B: guy from belgium C: sania mirza D: tom cruise""",
    2:"""what is a correct python syntax
    A: print('hello world') B:  """
}
q1 = input(random)