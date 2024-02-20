import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colormaps
import time

def dead_state(height, width):
    board = [[0 for i in range(width)] for j in range(height)]
    return board

def random_state(height, width):
    state = dead_state(height, width)
    for i in range(len(state)):
        for j in range(len(state[0])):
            rand_num = random.random()
            if rand_num > 0.5:
                state[i][j] = 1
    return state


def next_state(initial_state):
  height = len(initial_state)
  width = len(initial_state[0])
  new_state = dead_state(height, width)
  for r in range(height):
    for c in range(width):
      if r == 0:
        if c == 0:
          s = initial_state[r+1][c] + initial_state[r+1][c+1] + initial_state[r][c+1]
        elif c == width -1:
          s = initial_state[r][c-1] + initial_state[r+1][c-1] + initial_state[r+1][c]
        else:
          s = initial_state[r][c-1] + initial_state[r+1][c-1] + initial_state[r+1][c]+ initial_state[r+1][c+1] + initial_state[r][c+1]
      elif r == height -1:
        if c == 0:
          s = initial_state[r-1][c] + initial_state[r-1][c+1] + initial_state[r][c+1]
        elif c == width -1:
          s = initial_state[r][c-1] + initial_state[r-1][c-1] + initial_state[r-1][c]
        else:
          s = initial_state[r][c-1] + initial_state[r-1][c-1] + initial_state[r-1][c] + initial_state[r-1][c+1] + initial_state[r][c+1]
      else:
        if c == 0:
          s = initial_state[r-1][c] + initial_state[r-1][c+1] + initial_state[r][c+1] + initial_state[r+1][c+1] + initial_state[r+1][c]
        elif c == width -1:
          s = initial_state[r+1][c] + initial_state[r+1][c-1] + initial_state[r][c-1] + initial_state[r-1][c-1] + initial_state[r-1][c]
        else:
          s = initial_state[r][c-1] + initial_state[r-1][c-1] + initial_state[r-1][c] + initial_state[r-1][c+1] + initial_state[r][c+1] + initial_state[r+1][c+1] + initial_state[r+1][c] + initial_state[r+1][c-1]
     
      if s <= 1: #dead cells don't come alive and live cells die do to underpop
        new_state[r][c] = 0
      elif s == 2: #live cells live but dead cells don't come alive
        new_state[r][c] = 0 + initial_state[r][c]
      elif s == 3: #live cells live and dead cells become alive
        new_state[r][c] = 1
      elif s > 3: #live cells die due to overpop and dead cells don't come alive
        new_state[r][c] = 0
  return new_state

def update_forever(init_state):
  new_state = init_state
  plt.ion()
  fig = plt.figure()
  ax = fig.add_subplot(111)
  h = ax.imshow(new_state,interpolation= 'none', cmap = mpl.colormaps['Greys'])
  t = 0 
  while t < 100: 
    new_state = next_state(new_state)
    h.set_data(new_state)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.25)
    t += 1


if __name__ == "__main__":
  ini_state = random_state(30, 30)
  #ini_state = []
  update_forever(ini_state)


