import numpy as np

print("This tool will convert Radians to Degrees.")
inp = int(float(input("Please enter input: ")))
res = ((inp * 180)/np.pi)
print(str(inp) + " Radians is equal to " + str(res) + " Degrees.")