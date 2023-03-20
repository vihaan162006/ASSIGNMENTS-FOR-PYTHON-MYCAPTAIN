#Task 1#
radius=float(input("Input the radius of the circle: "))
area=radius*radius*3.142
print("The area of the circle with radius",radius,"is",area)

#Task 2#
filename = input("Input the Filename: ")
extension = filename.split(".")[-1]
print("The extension of the file is: '{}'".format(extension))
