import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import util
import scipy.stats

def perfect_dice(make_chart=False):
  
  x = [2,3,4,5,6,7,8,9,10,11,12]
  odds = np.array([1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36,3/36,2/36,1/36])
  
  assert abs (sum(odds) - 1.0) < 0.001, ' bad dice'
  
  if make_chart:
    fig, axes = plt.subplots()
    axes.bar(x, height=odds)
    import os
    plt.savefig('dice.png')
  
  rolls = []
  for idx, i in enumerate(x):
    s = x[idx]
    pct = odds[idx]
    for j in range(0, int(36*pct)):
      rolls.append(s)
      
  #Variance: 70/24 + 70/24 = 140/24 = 5.83
  #Mean: 7.0
  return np.array(rolls)
  

def descriptive_np(data, show_d=False):
  print('mean {0:.2f}'.format(np.mean(data)))
  print('med {0:.2f}'.format(np.median(data)))
  print('mode ', scipy.stats.mode(data))
  print("\n")

def descriptive_pd(s, show_d=False):
  print('mean {0:.2f}'.format(s.mean()))
  print('med {0:.2f}'.format(s.median()))
  print('mode ', s.mode() )
  print("\n")

def plot_dollars():
  df = pd.read_csv('dollar.csv')
  dollars = df['dollar']
  axes = dollars.plot.hist(bins=100, alpha=0.5)
  plt.savefig('d.png')