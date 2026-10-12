import math
# Calculation of circle area and circumference 
#
promien = int(input("Podaj r: "))
# determine radius and PI values
area = promien * math.pi**2
circumference = 2 * promien * math.pi
print(f"circumfence = {circumference}")
print(f"area = {area}")