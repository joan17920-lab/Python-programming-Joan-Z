import math
def cathetus (a, c):
  if a >= c:
    print ("Hypotus must > cathetus ")
  else:
   return math.sqrt (c**2 - a**2)

print (cathetus(5, 7))