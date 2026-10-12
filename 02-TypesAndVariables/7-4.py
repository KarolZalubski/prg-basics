import math
circumference = int(input("Enter tree circumference in cm: "))
diameter = circumference/math.pi
if diameter >=50:
    print("Tree can be cut down: ", True)
else:
    print("Tree can be cut down: ", False)