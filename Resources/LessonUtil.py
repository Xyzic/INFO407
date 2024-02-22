def add(a,b):
  counters[add] += 1
  return a + b
  
def div(a,b):
  counters[div] += 1
  return a/b
  
def get_count(fn):
  return counters[fn]
  
#using functions as keys in a dictionary!
counters = {add:0,div:0}
def clear():
  for k in counters.keys():
    counters[k] = 0

