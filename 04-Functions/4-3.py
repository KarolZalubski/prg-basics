###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    area = (a+b+c)/2
    return area

triangle = triangle_area(5,3,4)
print(f'The area of ​​a triangle with sides 5,3,4 is {triangle}')
triangle2 = triangle_area(10,20,21)
print(f'The area of ​​a triangle with sides 10, 20, 21 is {triangle2}')
