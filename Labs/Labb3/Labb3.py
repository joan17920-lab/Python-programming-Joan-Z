import numpy as np
import matplotlib.pyplot as plt

# Läs in data 
unlabelled = np.loadtxt("../Python-programming-Joan-Z/Labs/Labb3/unlabelled_data.csv", delimiter=",")

#  Skriv linjes ekvation enligt ögonmått
x_line = np.linspace(min(unlabelled[:, 0]), max(unlabelled[:, 0]), 100)
y_line = -0.9*x_line + 0.5

# Importera funktion och klassifiera punkterna 
import classified
x_above, y_above, x_below, y_below,above_idx,below_idx = classified.classified(unlabelled[:, 0], unlabelled[:, 1], -0.9, 0.5)

# Sätta label till punkterna och skriva in en ny fil
labels = np.empty(len(unlabelled),dtype= int)
labels[above_idx] = 1
labels[below_idx] = 0
labeled = np.column_stack((unlabelled, labels))
np.savetxt("../Python-programming-Joan-Z/Labs/Labb3/labelled_data.csv",labeled, delimiter=",", fmt=["%.16f", "%.16f", "%d"])

# Plotta alla punkterna enligt label och dra linje enligt ekvation
plt.figure(figsize=(6,6), dpi = 100)
plt.title("Klassificering av punkter")
plt.plot (x_line,y_line, label = 'y = -0,9x + 0,5')
plt.scatter(x_above,y_above,c="red", label = "Label 1 above ")
plt.scatter(x_below,y_below,c="blue", label = "Label 0 below")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.grid(True)
plt.show()