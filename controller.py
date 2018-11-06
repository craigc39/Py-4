import model, sys, pygame, GridBox, view, pygame

model = model.Board()
model.startGame()

view = view.py4view(model)

view.runGame()

