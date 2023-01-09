"""
demo of matplotlib
"""
# import packages
import matplotlib.pyplot as plt

# create list of numbers for base of plot
base = [e for e in range(1, 21)]
# create list of squares
square = [e * e for e in base]
# create list of cubes
cube = [e * e * e for e in base]

# display the lists
print("base numbers: ", base)
print("squares: ", square)
print("cubes: ", cube)

# build plot
plt.plot(base, square, label="square")
plt.plot(base, cube, label="cube")
plt.title("example plot of squares and cubes")
plt.xlabel("base")
plt.ylabel("values")
plt.legend()
plt.show()
