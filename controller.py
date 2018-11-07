import model, sys, pygame, GridBox, view, pygame

model = model.Board()
model.start_game()

view = view.py4view(model)

view.run_game()

